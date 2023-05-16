import random 
from Searches import *

def mainmenu():
    print("Welcome to Ainaz Estiri, Billy Chau, Binh Le, and Jacob Cunningham Feature Selection Algorithm.")
    #makes sure a valid input is entered or keeps looping
    while True:
        numFeatures = input("Please enter the total number of features: ")
        if numFeatures.isdigit():
            numFeatures = int(numFeatures)
            break
        else:
            print("Invalid input. Please enter a valid number.")
    

    print("Type the number of the algorithm you want to run.")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    print("3. Our group's Special Algorithm.")
    #makes sure a valid input is entered or keeps looping
    while True:
        algorithm = input()
        if algorithm =='1':
            break
        elif algorithm =='2':
            break
        elif algorithm =='3':
            break
        else:
            print("Invalid input. Please enter a valid algorithm number.")
            print("1. Forward Selection")
            print("2. Backward Elimination")
            print("3. Our group's Special Algorithm.")


    #i think this is what she wants?
    print(f"Using no features and 'random' evaluation, I get an accuracy of {random.uniform(0, 100):.1f}%") 
    print("Beginning search.")

    search() #include the text after the "Beginning search." inside the search function (as a universal function)


def inputdata(input): #Reads txt inputs from profs. example.
    with open(input, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        if line:
            data_point = line.split()
            class_label = data_point[0]
            features = [float(x) for x in data_point[1:]]
            data.append((class_label, features))
    return data

#print(inputdata('very-small-test-dataset.txt')) #Testing to see if inputdata() works




#Example data
data = [('A', [1, 2, 3]), ('B', [4, 5, 6]), ('A', [7, 8, 9]), ('B', [10, 11, 12]), ('C', [13, 14, 15])]
#solution = greedy_search(inputdata('very-small-test-dataset.txt'))
solution = greedy_search(data)

print("Solution:")
for features, class_label in solution.items():
    print(f"Features: {features}, Class: {class_label}")