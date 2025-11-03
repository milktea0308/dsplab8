import cv2
import numpy as np

def calcEnergy(I):
    """
    Sum up the energy for each channel
    """
    I = I.astype(np.float64)
    dx = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]], dtype=np.float64)
    dy = dx.T  # vertical gradient filter

    ############### YOUR CODE HERE ###############
    R, G, B = 

    dIrx =
    # ...

    energy = 
    ############### YOUR CODE ENDS ###############
    return energy.astype(np.float64)
