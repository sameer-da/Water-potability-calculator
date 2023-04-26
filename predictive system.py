# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:55:59 2023

@author: admin
"""

import numpy as np
import pickle

pickled_model = pickle.load(open("C:/Users/admin/Desktop/Water quality DS/modelxgb.pkl", 'rb'))


input_data = (8.31,214.3,22018.41,8.05,356.886,363.26,18.4,100.34,4.628)

#changing input data as numpy array
input_as_np = np.asarray(input_data)

#reshaping the data
input_reshaped = input_as_np.reshape(1,-1)

prediction_xgb = pickled_model.predict(input_reshaped)
print(prediction_xgb)


if(prediction_xgb[0] == 0):
    print('The water is not potable')
else:
    print('The water is potable')