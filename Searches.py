import random 
def evaluate_solution(solution, data):
    #Evaluate the solution by counting the number of correctly classified data points.
    correct_count = 0
    for class_label, features in data:
        predicted_label = solution.get(tuple(features), None)
        if predicted_label == class_label:
            correct_count += 1
    return correct_count


def greedy_search(data): #WIP
    bestsolution = {}
    bestscore = 0
    feature_count = len(data[0][1])

    while True:
        current = dict(bestsolution)  # Make a copy of the best solution
        random_feature = random.randint(0, feature_count - 1)
        random_data_point = random.choice(data)
        random_features = random_data_point[1]
        random_class_label = random_data_point[0]
        current[tuple(random_features)] = random_class_label

        currentscore = evaluate_solution(current, data)
        if currentscore > bestscore:
            bestsolution = dict(current)
            bestscore = currentscore
        else:
            break

    return bestsolution