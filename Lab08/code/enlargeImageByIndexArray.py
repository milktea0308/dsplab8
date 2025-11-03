import numpy as np

def enlargeImageByIndexArray(image, seamIndexArray):
    """
    Enlarge image by duplicating pixels along seam,
    using smooth interpolation (average of seam neighbors)
    to avoid visible artifacts at the seam boundary.
    """

    h, w, ch = image.shape
    imageEnlarged = np.zeros((h, w + 1, ch), dtype=image.dtype)
    ############### YOUR CODE HERE ###############
    
    ############### YOUR CODE ENDS ###############

    return imageEnlarged
