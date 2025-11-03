import numpy as np

def reduceMaskByIndexArray(mask, seamIndexArray, seamDirection):
    """
    Reduce mask (logical matrix) along seam
    """
    h, w = mask.shape

    if seamDirection == 0:
        maskReduced = np.zeros((h, w - 1), dtype=bool)
        ############### YOUR CODE HERE ###############
        
        ############### YOUR CODE ENDS ###############
        
    else:
        maskReduced = np.zeros((h - 1, w), dtype=bool)
        ############### YOUR CODE HERE ###############
        
        ############### YOUR CODE ENDS ###############
        
    return maskReduced
