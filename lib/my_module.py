import scipy.stats as sps


def get_sample(size):
    return sps.norm().rvs(size), sps.norm().rvs(size)
