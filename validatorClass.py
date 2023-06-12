from classifierClass import Classifier
class Validator:
    def __init__(self):
        self.classifier = Classifier()
    
    def evaluate(self, featureSubset, dataset, trace=False):

        # Train the classifier on the filtered dataset
        accuracy = 0

        for instance in range(len(dataset)):
            self.classifier = Classifier()
            self.classifier.train(dataset[:instance])
            self.classifier.train(dataset[instance + 1:])
            accuracy += self.calculateAccuracy(dataset[instance], featureSubset, trace)

        return accuracy / len(dataset)

    def calculateAccuracy(self, toTest, featureSubset, trace):
        predictedLabel = self.classifier.test(toTest, featureSubset)
        if trace: print("predicting label", predictedLabel, "for instance", toTest.label)
        if predictedLabel == toTest.label:
            return 1
        return 0

    #def calculateAccuracy(self, dataset, featureSubset):
    #    # Calculate the accuracy of the classifier on the given dataset
    #    correctPredictions = 0
    #    totalInstances = len(dataset)
#
    #    for instance in dataset: #TODO leave one out
    #        predictedLabel = self.classifier.test(instance, featureSubset)
    #        if predictedLabel == instance.label:
    #            correctPredictions += 1
#
    #    accuracy = correctPredictions / totalInstances
#
    #    return accuracy