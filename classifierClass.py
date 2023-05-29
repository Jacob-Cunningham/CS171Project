import math

class Classifier:
    def __init__(self):
        self.trainSamples = []  # List to store the training samples

    def train(self, samples):
        self.trainSamples = samples  # Store the training samples for future classification

    def test(self, state):
        minDistance = math.inf  # Initialize minimum distance as infinity
        nearestPoint = None  # Initialize nearest point as None

        # Iterate over each training sample to find the nearest point
        for trainSample in self.trainSamples:
            distance = self.euclideanDistance(state['feat1'], trainSample['feat1'])
            if distance < minDistance:
                minDistance = distance
                nearestPoint = trainSample['label']
            print(trainSample + " is class " + nearestPoint)
        # Return the predicted class label of the nearest training point
        return nearestPoint

    def euclideanDistance(self, feat1, feat2):
        # Compute the Euclidean distance between two points in an n-dimensional space
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(feat1, feat2)]))
        return distance
