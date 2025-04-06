import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi
from shapely.geometry import Polygon, box
from shapely.validation import make_valid
from scipy.stats import ttest_ind, mannwhitneyu, sem, t
from scipy.stats import ks_2samp

def voronoi_finite_polygons_2d(vor, radius=1e6):
    new_regions = []
    new_vertices = vor.vertices.tolist()
    center = vor.points.mean(axis=0)

    for point_idx, region_idx in enumerate(vor.point_region):
        region = vor.regions[region_idx]
        if -1 not in region:
            new_regions.append(region)
            continue

        ridges = [r for r in vor.ridge_vertices if point_idx in r]
        region_points = []
        for (p1, p2), (v1, v2) in zip(vor.ridge_points, vor.ridge_vertices):
            if point_idx not in (p1, p2):
                continue
            if v1 == -1 or v2 == -1:
                i = v1 if v1 != -1 else v2
                tvec = vor.points[p2] - vor.points[p1]
                tvec = tvec / np.linalg.norm(tvec)
                n = np.array([-tvec[1], tvec[0]])
                far_point = vor.vertices[i] + n * radius
                new_vertices.append(far_point.tolist())
                region_points.append(i)
                region_points.append(len(new_vertices) - 1)
        new_regions.append(region_points)

    return new_regions, np.array(new_vertices)

def compute_region_areas(vor):
    areas = []
    for region_index in vor.point_region:
        region = vor.regions[region_index]
        if -1 in region or len(region) == 0:
            # Region is open (extends to infinity), skip or handle separately
            areas.append(np.nan)
            continue
        polygon = Polygon([vor.vertices[i] for i in region])
        areas.append(polygon.area)
    return np.array(areas)


def clipped_voronoi_areas(points, bounding_box=(0, 1, 0, 1)):
    vor = Voronoi(points)
    regions, vertices = voronoi_finite_polygons_2d(vor)
    bbox = box(*bounding_box)

    areas = []
    for region in regions:
        polygon = Polygon(vertices[region])
        clipped = make_valid(polygon)
        areas.append(clipped.area)
    return np.array(areas)

def confidence_interval(data, alpha=0.05):
    n = len(data)
    mean = np.mean(data)
    se = sem(data)
    margin = t.ppf(1 - alpha/2, df=n-1) * se
    return mean - margin, mean + margin

def compare_treatments_with_voronoi(samples_A, samples_B, bounding_box=(0, 1, 0, 1),
                                     stat_func=np.mean, test="t-test", plot=True):
    # Compute per-sample summary statistics
    summary_A = [stat_func(clipped_voronoi_areas(s, bounding_box)) for s in samples_A]
    summary_B = [stat_func(clipped_voronoi_areas(s, bounding_box)) for s in samples_B]

    # Statistical test
    if test == "t-test":
        stat, p = ttest_ind(summary_A, summary_B, equal_var=False)
    elif test == "mannwhitney":
        stat, p = mannwhitneyu(summary_A, summary_B, alternative='two-sided')
    else:
        raise ValueError("Unsupported test: choose 't-test' or 'mannwhitney'")

    # Confidence intervals
    ci_A = confidence_interval(summary_A)
    ci_B = confidence_interval(summary_B)

    # Plotting
    if plot:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))

        # Violin plot
        axs[0].violinplot([summary_A, summary_B], showmeans=True)
        axs[0].set_xticks([1, 2])
        axs[0].set_xticklabels(['Treatment A', 'Treatment B'])
        axs[0].set_title('Distribution of Per-Sample Statistics')
        axs[0].set_ylabel('Summary Statistic (e.g., Mean Voronoi Area)')

        # CDF plot
        for group, label, color in zip([summary_A, summary_B], ['A', 'B'], ['blue', 'green']):
            sorted_vals = np.sort(group)
            cdf = np.arange(1, len(sorted_vals)+1) / len(sorted_vals)
            axs[1].plot(sorted_vals, cdf, label=f'Treatment {label}', lw=2)
        axs[1].set_title('Empirical CDF of Summary Statistics')
        axs[1].set_xlabel('Summary Statistic')
        axs[1].set_ylabel('Cumulative Probability')
        axs[1].legend()

        plt.tight_layout()
        plt.show()

    return {
        "p_value": p,
        "mean_A": np.mean(summary_A),
        "mean_B": np.mean(summary_B),
        "ci_A": ci_A,
        "ci_B": ci_B,
        "summary_A": summary_A,
        "summary_B": summary_B
    }


def render_point_field(x,y,width=10,height=10,scale=10):
    Nx=int(width*scale)
    Ny=int(width*scale)
    
    img=np.zeros([Nx,Ny])
    
    for xx,yy in zip(x,y):
        img[int(xx*scale),int(yy*scale)]=1
        
    return img
        
def point_field(intensity=10,width=10,height=10,plot=False,ax=None,title = None, seed=42) :
    # Total expected number of points
    area = width * height
    np.random.seed(seed=seed)
    num_points = np.random.poisson(intensity * area)

    # Generate uniform random points
    x = np.random.uniform(0, width, num_points)
    y = np.random.uniform(0, height, num_points)

    # Plot
    if plot:
        if ax is None:
            fig,ax=plt.subplots(1,figsize=(6, 6))
        
        ax.scatter(x, y, s=1)
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        if title is None :
            ax.set_title(f"2D Poisson Point Field ({num_points} points)")
        else :
            ax.set_title(title)
            
        ax.set_aspect('equal')

    return np.array([x,y]).transpose()



def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(x)+1) / len(x)
    return x, y

def plot_ks_test(sample_A,sample_B, ax=None, xlim = None) :
    dcolors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    x_A, y_A = ecdf(sample_A)
    x_B, y_B = ecdf(sample_B)

    # Compute KS statistic and p-value
    D, p_value = ks_2samp(sample_A, sample_B, method='exact')

    # Find maximum vertical distance for visualization
    all_x = np.sort(np.concatenate([x_A, x_B]))
    cdf_A_interp = np.searchsorted(x_A, all_x, side='right') / len(x_A)
    cdf_B_interp = np.searchsorted(x_B, all_x, side='right') / len(x_B)
    deltas = np.abs(cdf_A_interp - cdf_B_interp)
    max_idx = np.argmax(deltas)
    x_D = all_x[max_idx]
    y_A_D = cdf_A_interp[max_idx]
    y_B_D = cdf_B_interp[max_idx]

    # Plot ECDFs and KS statistic
    if ax is None :
        fig,ax=plt.subplots(1,figsize=(8, 5))
    
    if xlim is None :
        xlim=[np.min(sample_A),np.max(sample_A)]
        
    nBins=50
    alpha=0.75
    ax.step(x_A, y_A, label='Sample A (mean={0:0.2f})'.format(sample_A.mean()), where='post')
    ax.set_xlim(xlim)
    ha,aa = np.histogram(sample_A,bins=nBins,range=xlim)
    ax.plot(aa[1:],ha/max(ha)/2,':',alpha=alpha,color=dcolors[0])
    ax.step(x_B, y_B, label='Sample B (mean={0:0.2f})'.format(sample_B.mean()), where='post')
    hb,ab = np.histogram(sample_B,bins=nBins,range=xlim)
    ax.plot(ab[1:],hb/max(hb)/2,':',alpha=alpha,color=dcolors[1])
    ax.vlines(x_D, y_A_D, y_B_D, color='red', linestyles='dashed', label=f'Max Distance D = {D:.2f}')
    ax.set(title=f'Kolmogorov–Smirnov Test: p-value = {p_value:.4f}',xlabel='Value', ylabel='ECDF')
    ax.legend()
    ax.grid(True)

def icc_calc(value_name, group_name, data_df):
    data_agg = data_df.groupby(group_name).agg({value_name: ['mean', 'var']}).reset_index()
    data_agg.columns = data_agg.columns.get_level_values(1)
    S_w = data_agg['var'].mean()
    S_a = data_agg['mean'].var()
    print('{0}: S_w={1:0.02f}, S_a={2:0.2f}'.format(value_name,S_w,S_a))
    return S_a/(S_a+S_w)

def icc(m,s) :
    return m.var()/(m.var()+s.mean()**2)


def compute_area_in_samples(samples, width,height, threshold) :
    A = []
    points = []
    for intensity in samples : 
        points.append(point_field(intensity=intensity,width=width,height=height)) 
        a=clipped_voronoi_areas(points[-1], bounding_box=(0, width, 0, height))
        a=a[a<threshold]
        A.append(a)
    return A,points

def test_samples_pvalues(vSamples, seed=42) :

    p_values=[]
    for nSamples in vSamples :
        np.random.seed(seed=seed)
        samples_control   = np.random.normal(5.75, 1, size=nSamples) 
        samples_treatment = np.random.normal(6.0, 1, size=nSamples)
        width, height = 10,10
        threshold=1.5

        A_control,p_control     = compute_area_in_samples(samples_control, width=width,height=height,threshold=threshold)
        A_treatment,p_treatment = compute_area_in_samples(samples_treatment, width=width,height=height,threshold=threshold)

        stat_func = np.mean
        avg_control = np.array([stat_func(s) for s in A_control])
        avg_treatment = np.array([stat_func(s) for s in A_treatment])

        stat, p_value = ttest_ind(avg_control, avg_treatment, equal_var=False)
        p_values.append(p_value)

    return p_values