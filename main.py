import csv
import pandas as pd
import numpy as np
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split # Import train_test_split function
import random
import os
from lib.rsvm.trainer import Trainer
from lib.rsvm.predictor import Predictor
import pickle
from statistics import mean
import sys
import joblib

# fungsi untuk mengambil dataset (lokasi file sejajar dengan file main.py)
def open_dataset():
    with open('diabetest.csv', 'r') as file:
        data = []
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

# fungsi untuk menghilangkan data kosong
def clean_data(dataset):
    data = []
    for row in dataset:
        if row[1] != '0' and row[2] != '0' and row[3] != '0' and row[4] != '0' and row[5] != '0' and row[6] != '0' and row[7] != '0':       # cek data clean
            data.append(row)
    return data

# fungsi untuk menampilkan jumlah data, class 0, dan class 1 pada dataset
def check_dataset(dataset):
    total_data = 0
    class_0 = 0
    class_1 = 0

    for row in dataset:
        total_data = total_data + 1         # hitung jumlah data
        if row[8] == '1' :
            class_1 = class_1 + 1           # hitung jumlah data class 1
        else :
            class_0 = class_0 + 1           # hitung jumlah data class 0
    
    print("===========================")
    print("total data = ", total_data)
    print("total class 1 = ", class_1)
    print("total class 0 = ", class_0)
    print("===========================")
    print("")

def min_max_norm(arr):
    # min-max norm
    data = minmax_scale(arr)
    for row in data:
        row[0] = round(row[0], 3)
        row[1] = round(row[1], 3)
        row[2] = round(row[2], 3)
        row[3] = round(row[3], 3)
        row[4] = round(row[4], 3)
        row[5] = round(row[5], 3)
        row[6] = round(row[6], 3)
        row[7] = round(row[7], 3)
    return data


 

if __name__ == "__main__":
    dataset = open_dataset()                # mendapatkan database
    dataset.pop(0)                          # delete header dataset (index ke-0)
    print("dataset murni")
    check_dataset(dataset)

    clean_dataset = clean_data(dataset)     # clean data
    print("dataset clean")
    check_dataset(clean_dataset)

    normalisasi = min_max_norm(clean_dataset)# normalisasi min max
    print("dataset normalisasi")
    check_dataset(normalisasi)

    normalisasi_pd = pd.DataFrame(normalisasi)# convert ke pandas

    # Split dataset into training set and test set
    # Separating the target variable 
    X = normalisasi_pd.values[:, 0:7] 
    Y = normalisasi_pd.values[:, 8]

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2,random_state=100) # 80% training and 30% test
    trainer = Trainer(X_train, y_train)
    trainer.make(r = 0.1, v = 5)
    trainer.tune(c = 100, g = 0.0001, k = 1, s = 0)
    trainer.train()
    accuracy = sum(trainer.get_accuracy()[0])/5
    print(accuracy)
    model = trainer.set_model()
    joblib.dump(model,'rsvm_model.sav')



        
