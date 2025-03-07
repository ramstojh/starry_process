from .temporal import *
import numpy as np

defaults = dict(
    ydeg=15,
    udeg=2,
    r=20.0,
    dr=None,
    a=0.40,
    b=0.27,
    c=0.1,
    n=10.0,
    p=1.0,
    i=60.0,
    u=np.zeros(30),
    tau=None,
    temporal_kernel=Matern32Kernel,
    normalized=True,
    normalization_order=20,
    normalization_zmax=0.023,
    marginalize_over_inclination=True,
    baseline_mean=0.0,
    baseline_var=0.0,
    driver="numpy",
    eps=1e-8,
    epsy=1e-12,
    epsy15=1e-9,
    covpts=300,
    log_alpha_max=10,
    log_beta_max=10,
    abmin=1e-12,
    sigma_max=45.0,
    mx=300,
    my=150,
)
