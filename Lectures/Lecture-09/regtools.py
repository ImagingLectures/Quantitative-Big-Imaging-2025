import tensorflow as tf

def affine_transform_tf(image, theta=0.0, tx=0.0, ty=0.0, scale=1.0):
    """
    Differentiable affine transform (rotation + translation + uniform scale).
    
    Args:
        image: Tensor of shape [H, W, C] (grayscale or RGB).
        theta: Rotation angle in radians.
        tx, ty: Translation offsets (in pixels).
        scale: Uniform scaling factor.
    
    Returns:
        Transformed image of shape [H, W, C]
    """
    # Ensure input shape is [H, W, C]
    if image.ndim == 2:
        image = tf.expand_dims(image, -1)

    # H, W, C = image.shape
    H, W, C = tf.unstack(tf.shape(image))

    # Create a normalized grid [-1, 1] x [-1, 1]
    x = tf.linspace(-1.0, 1.0, W)
    y = tf.linspace(-1.0, 1.0, H)
    xx, yy = tf.meshgrid(x, y)
    grid = tf.stack([xx, yy, tf.ones_like(xx)], axis=-1)  # shape [H, W, 3]
    grid = tf.reshape(grid, [-1, 3])  # [H*W, 3]

    # Build affine transform matrix (rotation + scale + translation)
    cos_t = tf.cos(theta) * scale
    sin_t = tf.sin(theta) * scale
    tx_n = tx * 2.0 / tf.cast(W, tf.float32)  # normalize tx to [-1, 1]
    ty_n = ty * 2.0 / tf.cast(H, tf.float32)  # normalize ty to [-1, 1]

    affine = tf.stack([
        [cos_t, -sin_t, tx_n],
        [sin_t,  cos_t, ty_n]
    ])  # [2, 3]

    # Apply affine to grid
    coords = tf.matmul(grid, affine, transpose_b=True)  # [H*W, 2]
    coords = tf.reshape(coords, [H, W, 2])  # [H, W, 2]

    # Map from normalized [-1, 1] to image coordinates
    x = ((coords[..., 0] + 1.0) * 0.5) * tf.cast(W - 1, tf.float32)
    y = ((coords[..., 1] + 1.0) * 0.5) * tf.cast(H - 1, tf.float32)

    # Bilinear sampling
    x0 = tf.cast(tf.floor(x), tf.int32)
    x1 = x0 + 1
    y0 = tf.cast(tf.floor(y), tf.int32)
    y1 = y0 + 1

    x0 = tf.clip_by_value(x0, 0, W - 1)
    x1 = tf.clip_by_value(x1, 0, W - 1)
    y0 = tf.clip_by_value(y0, 0, H - 1)
    y1 = tf.clip_by_value(y1, 0, H - 1)

    Ia = tf.gather_nd(image, tf.stack([y0, x0], axis=-1), batch_dims=0)
    Ib = tf.gather_nd(image, tf.stack([y1, x0], axis=-1), batch_dims=0)
    Ic = tf.gather_nd(image, tf.stack([y0, x1], axis=-1), batch_dims=0)
    Id = tf.gather_nd(image, tf.stack([y1, x1], axis=-1), batch_dims=0)

    wa = (1 - (x - tf.cast(x0, tf.float32))) * (1 - (y - tf.cast(y0, tf.float32)))
    wb = (1 - (x - tf.cast(x0, tf.float32))) * (y - tf.cast(y0, tf.float32))
    wc = (x - tf.cast(x0, tf.float32)) * (1 - (y - tf.cast(y0, tf.float32)))
    wd = (x - tf.cast(x0, tf.float32)) * (y - tf.cast(y0, tf.float32))

    wa = tf.expand_dims(wa, -1)
    wb = tf.expand_dims(wb, -1)
    wc = tf.expand_dims(wc, -1)
    wd = tf.expand_dims(wd, -1)

    out = wa * Ia + wb * Ib + wc * Ic + wd * Id
    return out