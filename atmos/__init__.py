from constants import const as constants

from utils import (
    print_if,
    format_num,
    homedir,
    pdfmerge,
    legend_2ax,
    colorbar_multiplot,
    text,
    subplot_index,
    fmt_subplot,
    ax_lims_ticks,
    clear_axlabels,
    fmt_axlabels,
    FigGroup,
    savefigs,
    symm_colors,
    print_odict,
    odict_insert,
    odict_delete,
    makelist,
    strictly_increasing,
    strictly_decreasing,
    non_increasing,
    non_decreasing,
    find_closest,
    disptime,
    timedelta_convert,
    isleap,
    month_str,
    days_per_month,
    days_this_month,
    season_months,
    season_days,
    jday_to_mmdd,
    mmdd_to_jday,
    pentad_to_jday,
)

from xrhelper import (
    to_dataset,
    meta,
    squeeze,
    expand_dims,
    coords_init,
    coords_assign,
    ds_print,
    ds_unpack,
    vars_to_dataset,
)

from data import (
    biggify,
    collapse,
    nantrapz,
    rolling_mean,
    gradient,
    ncdisp,
    ncload,
    load_concat,
    save_nc,
    pres_units,
    pres_convert,
    precip_units,
    precip_convert,
    get_coord,
    subset,
    dim_mean,
    latlon_equal,
    lon_convention,
    set_lon,
    interp_latlon,
    mask_oceans,
    mean_over_geobox,
    get_ps_clim,
    correct_for_topography,
    near_surface,
    interp_plevels,
    int_pres,
    split_timedim,
    splitdays,
    daily_from_subdaily,
    combine_daily_years,
)

from variables import (
    coriolis,
    divergence_spherical_2d,
    vorticity,
    rossby_num,
    potential_temp,
    equiv_potential_temp,
    dry_static_energy,
    moist_static_energy,
    moisture_flux_conv,
    streamfunction,
)

from plots import (
    degree_sign,
    latlon_labels,
    latlon_str,
    mapticks,
    autoticks,
    clevels,
    cinterval,
    climits,
    colorbar_symm,
    init_latlon,
    geobox,
    pcolor_latlon,
    contourf_latlon,
    contour_latlon,
    init_latpres,
    pcolor_latpres,
    contourf_latpres,
    contour_latpres,
    stipple_pts,
)

from analysis import (
    Fourier,
    fourier_from_scratch,
    fourier_smooth,
    Linreg,
    regress_field,
    corr_matrix,
    scatter_matrix,
    scatter_matrix_pairs,
    detrend,
)
