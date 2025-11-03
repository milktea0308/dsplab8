import cv2
from calcEnergy import calcEnergy
from findOptSeam import findOptSeam
from reduceImageByIndexArray import reduceImageByIndexArray

def seamCarvingContentAmplification(image):
    """
    Enlarge image with scaling, then reduce by seam carving
    """
    # input size
    h_input, w_input, ch = image.shape
    # Enlarge image with standard scaling
    enlarged_image = cv2.resize(image, None, fx=1.4, fy=1.4, interpolation=cv2.INTER_LINEAR)
    h_enlarge, w_enlarge, ch = enlarged_image.shape

    ############### YOUR CODE HERE ###############
        
    ############### YOUR CODE ENDS ###############

    return output
