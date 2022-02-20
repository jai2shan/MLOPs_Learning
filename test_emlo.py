import pytest
import torch
import csv
import os

# This is another change
def test_case_ModelAccuracy():
    '''Checks if tests are running'''
    with open('metrics.csv') as file:
        metrics =  csv.reader(file, delimiter = ",")
        for row in metrics:
            if row[0] == 'Accuracy':
                acc = float(row[2].split("(")[1].split(",")[0])
                assert acc > 0.75, "Accuracy did not meet the expectations"
    file.close()

def test_case_CatAccuracy():
    '''Checks if tests are running'''
    with open('metrics.csv') as file:
        metrics =  csv.reader(file, delimiter = ",")
        for row in metrics:
            if row[0] == 'Class Cats':
                acc = float(row[2].split("(")[1].split(",")[0])
    file.close()
    assert acc > 0.70, "Cat Class performance did not meet the expectations"


def test_case_DogAccuracy():
    '''Checks if tests are running'''
    with open('metrics.csv') as file:
        metrics =  csv.reader(file, delimiter = ",")
        for row in metrics:
            if row[0] == 'Class Dogs':
                acc = float(row[2].split("(")[1].split(",")[0])
    file.close()
    assert acc > 0.70, "Dog Class performance did not meet the expectations"


FileExists = ['data.zip','model.pt']

@pytest.mark.parametrize("fileName",FileExists)
def test_FileExists(fileName):
    print(fileName)
    assert fileName not in os.listdir(), "{} is present in the repo. Please remove".format(fileName)