import random
from validatorClass import Validator
def evaluate_solution(solution, data):
    #Evaluate the solution by counting the number of correctly classified data points.
    correct_count = 0
    for class_label, features in data:
        predicted_label = solution.get(tuple(features), None)
        if predicted_label == class_label:
            correct_count += 1
    return correct_count

"""
Forward selection greedy search algorithm. Takes two arguments.
num_features is the number of features each item has
classifier is an object containing an evaluate function.
    The evaluate function takes a set of features to use.
    The stub contains only a random evaluate while the actual classifier will contain more functions for using the model.
trace is optional and controls whether the function prints out at each step
"""
def forward_selection(num_features, validator, dataset, trace = False):
    features = [(validator.evaluate(set(), dataset), set())]
    for depth in range(num_features): #find the best set with depth features
        best_choice = (0, set())
        if trace: print("Adding features to", features[-1])
        for feature in range(num_features): #try adding each feature to the set
            if feature in features[-1][1]: continue
            current_features = features[-1][1].union({feature})
            accuracy = validator.evaluate(current_features, dataset)
            if trace: print("Features", current_features, "have accuracy", accuracy)
            if accuracy > best_choice[0]:
                best_choice = (accuracy, current_features)
        if trace: print(best_choice, "is best choice\n")
        features.append(best_choice) #remember best set for the depth
    
    if trace: print("Best option for each depth:")
    if trace: 
        for feature in features:
            print(feature)

    best_choice = features[0]
    for feature in features:
        if feature[0] > best_choice[0]:
            best_choice = feature
    return best_choice[1]


"""
Backward elimination greedy search algorithm. Takes two arguments.
num_features is the number of features each item has
classifier is an object containing an evaluate function.
    The evaluate function takes a set of features to use.
    The stub contains only a random evaluate while the actual classifier will contain more functions for using the model.
trace is optional and controls whether the function prints out at each step
"""
def backward_elimination(num_features, validator, dataset, trace = False):
    features = [(validator.evaluate(set(range(num_features)), dataset), set(range(num_features)))]
    for depth in range(num_features): #find the best set with depth features
        best_choice = (0, set())
        if trace: print("Eliminating features from", features[-1])
        for feature in range(num_features): #try adding each feature to the set
            if not feature in features[-1][1]: continue
            current_features = features[-1][1].difference({feature})
            accuracy = validator.evaluate(current_features, dataset)
            if trace: print("Features", current_features, "have accuracy", str(round(accuracy * 100, 2)) + '%')
            if accuracy > best_choice[0]:
                best_choice = (accuracy, current_features)
        if trace: print(best_choice, "is best choice\n")
        features.append(best_choice) #remember best set for the depth
    
    if trace: print("Best option for each depth:")
    if trace: 
        for feature in features:
            print(feature)

    best_choice = features[0]
    for feature in features:
        if feature[0] > best_choice[0]:
            best_choice = feature
    return best_choice[1]