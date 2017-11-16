import numpy as np

def chi2(flux, error):
    w_mean = np.average(flux)
    chi_to_be_integrated = []
    for s in range(len(flux)):
        chi_value = (flux[s] - w_mean)**2 / (error[s])**2
        chi_to_be_integrated.append(chi_value)
    chi = sum(chi_to_be_integrated)
    return chi / (len(flux) - 1)
