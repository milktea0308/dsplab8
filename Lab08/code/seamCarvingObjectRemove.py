import numpy as np
import cv2
import sys
from calcEnergy import calcEnergy
from findOptSeam import findOptSeam
from reduceImageByIndexArray import reduceImageByIndexArray
from reduceMaskByIndexArray import reduceMaskByIndexArray

def seamCarvingObjectRemove(image, mask, seamDirection):
    """
    Remove object inside mask using seam carving
    """
    output = image.copy()
    while np.any(mask):
        ############### YOUR CODE HERE ###############
        # Calculate energy
                
        # modify the output of energy according the mask
        # so that "findOptSeam" always selects a seam passing
        # through the circled region
                
        # Force seam through masked region
                
        # findOptSeam
                
        # reduceImage and reduceMask
                
        ############### YOUR CODE ENDS ###############
    return output
