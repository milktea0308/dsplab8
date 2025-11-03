import numpy as np
from calcEnergy import calcEnergy
from findOptSeam import findOptSeam
from reduceImageByIndexArray import reduceImageByIndexArray
from enlargeImageByIndexArray import enlargeImageByIndexArray

def seamCarvingInsert(image, insertsize):
    # Duplicate image
    image_duplicate = image.copy()
    h, w, ch = image.shape
    # Create a container to record the seam index
    seamIndex = np.zeros((h, insertsize), dtype=np.uint32)

    # Find seams to remove
    ############### YOUR CODE HERE ###############
    # Use a for loop to delete each seam with your
    # "calcEnergy", "findOptSeam", "reduceImageByIndexArray"
    for i in range(insertsize):
        
    ############### YOUR CODE ENDS ###############
    
    # Update seam indices
    ############### YOUR CODE HERE ###############
        
    ############### YOUR CODE ENDS ###############

    # Insert the seam back into the original image.
    # Copy the original image to insert it into the seam.
    output = image.copy()
    ############### YOUR CODE HERE ###############
        
    ############### YOUR CODE ENDS ###############
    return output
