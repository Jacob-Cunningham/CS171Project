import random 
import csv
from Searches import *
from validatorClass import *
from classifierClass import Classifier


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



def inputdata(input):
    with open(input, 'r') as file:
        lines = file.readlines()
    data = []
    for line in lines:
        if line:
            data_point = line.split()
            class_label = float(data_point[0])
            features = [float(x) for x in data_point[1:]]
            data.append((class_label, features))
    return data
