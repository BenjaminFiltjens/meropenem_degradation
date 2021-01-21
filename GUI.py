"""
Created on Sat May 9 2020

Small GUI to predict the degradation given the time and measured concentration
Uses the OLS-PR model (standard)

@author: Benjamin Filtjens
@email: benjamin.filtjens@kuleuven.be
"""

import tkinter as tk
from sklearn.externals import joblib

# Load our model
pipeline = joblib.load('POLY.pkl')

# tkinter GUI
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 300)
canvas1.pack()

# Input box for the day
label1 = tk.Label(root, text='Day: ')
canvas1.create_window(100, 100, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 100, window=entry1)

# Input box for the measured concentration
label2 = tk.Label(root, text='Measured concentration: ')
canvas1.create_window(120, 120, window=label2)

entry2 = tk.Entry (root) # create 2nd entry box
canvas1.create_window(270, 120, window=entry2)

# Compute predicted initial concentration
def predict():
    global Day  # our 1st input variable
    Day = float(entry1.get())

    global Measurement  # our 2nd input variable
    Measurement = float(entry2.get())

    Prediction_result = ('Predicted degradation: ', pipeline.predict([[Day, Measurement]]))
    label_Prediction = tk.Label(root, text=Prediction_result, bg='orange')
    canvas1.create_window(260, 280, window=label_Prediction)


# Add a button to perform the prediction
button1 = tk.Button (root, text='Predict degradation',command=predict, bg='orange')
canvas1.create_window(270, 150, window=button1)

root.mainloop()
