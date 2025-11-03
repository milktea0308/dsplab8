import numpy as np
import sys

def findOptSeam(energy, seamDirection):
    """
    Following Avidan & Shamir (2007)
    Finds optimal seam by the given energy of an image
    Returns mask with 0 mean a pixel is in the seam    
    """

    if seamDirection == 0:  # vertical seam
        # Padding
        M = np.pad(energy, ((0, 0), (1, 1)),
                   mode='constant', constant_values=sys.float_info.max)
        h, w = M.shape
        ############### YOUR CODE HERE ###############
        # Forward accumulation
        
        ############### YOUR CODE ENDS ###############
        # Find minimal energy in the last row
        idx = np.argmin(M[h - 1, :])
        seamEnergy = M[h - 1, idx]

        # Initialize for backtracking (same length as image height)
        optSeamIndexArray = np.zeros(h, dtype=np.uint32)
        optSeamIndexArray[-1] = idx

        ############### YOUR CODE HERE ###############
        # Backtrack the path of minimum seam
        
        ############### YOUR CODE ENDS ###############        
        
        # Remove padding offset and clamp to valid range
        optSeamIndexArray = np.clip(optSeamIndexArray - 1, 0, w - 2)
        return optSeamIndexArray, seamEnergy
    else:  # horizontal seam
        ############### YOUR CODE HERE ###############
        
        ############### YOUR CODE ENDS ###############

        return optSeamIndexArray, seamEnergy
