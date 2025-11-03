from calcEnergy import calcEnergy
from findOptSeam import findOptSeam
from reduceImageByIndexArray import reduceImageByIndexArray

def seamCarvingReduce(image, reduceSize, seamDirection):
    """
    Reduce image by removing 'reduceSize' seams
    """
    output = image.copy()
    for k in range(reduceSize):
        energy = calcEnergy(output)
        optSeamIndexArray, seamE = findOptSeam(energy, seamDirection)
        output = reduceImageByIndexArray(output, optSeamIndexArray, seamDirection)
        print(f"Reducing seam {k + 1}/{reduceSize}", end='\r')
    print()
    return output
