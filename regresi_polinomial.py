# -*- coding: utf-8 -*-
"""Regresi Polinomial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15_gD9-6sEkctJklSsAl-A4hNR_TWoOIp
"""

import numpy as np # modul numpy untuk memudahkan pengolahan data
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model # modul untuk memproses data

# Database
# x = Data, y = Target
x = [[2],[4],[8],[10],[12],[14],[16],[18],[20],[22]]
y = [4, 16, 64, 100, 144, 196, 256, 324, 400, 484] # hasil pangkat 2 dari nilai x

# Data uji
predict = np.array([[14]]) # nilai yang diprediksi
poly = PolynomialFeatures (degree=2) # ordo yang akan digunakan
x_= poly.fit_transform(x) # fitting dengan prediksi sumbu
predict_= poly.fit_transform(predict) # fitting jenis rekresi polinomial
regr = linear_model.LinearRegression() # meregresi polinomial
regr.fit(x,y) # menentukan grafik

# Menampilkan data prediksi
print ("Citra Dwi Lestari 1207030009") # menampilkan nama dan nim
print ("Prediksi") # menampilkan kata prediksi
print ("Input = ", predict) # menampilkan kata input dari nilai prediksi
print ("Output = ", regr.predict(predict)) # menampilkan kata output dari nilai regresi prediksi