import numpy as np

def reduceImageByIndexArray(image, seamIndexArray, seamDirection):
    """
    Remove one seam from the image based on seam index.
    Handles vertical (0) and horizontal (1) seams safely.
    """

    h, w, ch = image.shape

    if seamDirection == 0:  # vertical seam
        imageReduced = np.zeros((h, w - 1, ch), dtype=image.dtype)
        ############### YOUR CODE HERE ###############
        # clamp seamIndexArray to valid column range
        
        # Remove seam
        
        ############### YOUR CODE ENDS ###############
        
    else:  # horizontal seam
        h, w, ch = image.shape
        
        # # --- This section can be used or not. --- #
        # # Ensure that the length of seamIndexArray = w
        # seamIndexArray = np.asarray(seamIndexArray, dtype=np.int32)
        # if len(seamIndexArray) != w:
        #     # If the length is incorrect, resample or clip.
        #     seamIndexArray = np.round(
        #         np.linspace(seamIndexArray[0], seamIndexArray[-1], w)
        #     ).astype(np.int32)

        # # clamp values ​​are in [0, h-1]
        # seamIndexArray = np.clip(seamIndexArray, 0, h - 1)
        # # ---------------------------------------- #
        
        imageReduced = np.zeros((h - 1, w, ch), dtype=image.dtype)
        ############### YOUR CODE HERE ###############
        
        ############### YOUR CODE ENDS ###############
        
    return imageReduced
