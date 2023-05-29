class Validator:
    def __init__(self, classifier):
        self.classifier = classifier

    def evaluate(self, featureSubset, dataset):
        # Filter the dataset to include only the selected features
        filteredDataset = self.filterDataset(featureSubset, dataset)

        # Train the classifier on the filtered dataset
        self.classifier.train(filteredDataset)

        # Evaluate the accuracy of the classifier on the filtered dataset
        accuracy = self.calculateAccuracy(filteredDataset)

        return accuracy

    def filterDataset(self, featureSubset, dataset):
        # Filter the dataset to include only the selected features
        filteredDataset = []
        for instance in dataset:
            filteredInstance = {}
            for feature in featureSubset:
                filteredInstance[feature] = instance[feature]
            filteredInstance['label'] = instance['label']
            filteredDataset.append(filteredInstance)
        return filteredDataset

    def calculateAccuracy(self, dataset):
        # Calculate the accuracy of the classifier on the given dataset
        correctPredictions = 0
        totalInstances = len(dataset)

        for instance in dataset:
            predictedLabel = self.classifier.test(instance)
            if predictedLabel == instance['label']:
                correctPredictions += 1

        accuracy = correctPredictions / totalInstances

        return accuracy