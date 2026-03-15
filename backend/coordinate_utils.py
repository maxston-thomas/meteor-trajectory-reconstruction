import numpy as np

def radec_to_vector(ra_deg, dec_deg):
    """Convert Right Ascension and Declination (degrees)
    into a 3D unit direction vector. """

    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)

    x = np.cos(dec) * np.cos(ra)
    y = np.cos(dec) * np.sin(ra)
    z = np.sin(dec)

    return np.array([x, y, z])