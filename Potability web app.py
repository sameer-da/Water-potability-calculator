# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 14:11:01 2023

@author: admin
"""

import numpy as np
import pickle
import streamlit as st


pickled_model = pickle.load(open("C:/Users/admin/Desktop/Water quality DS/modelxgb.pkl", 'rb'))


#creating a function

def potability_prediction(input_data):
    
   

    #changing input data as numpy array
    input_as_np = np.asarray(input_data,dtype=object)

    #reshaping the data
    input_reshaped = input_as_np.reshape(1,-1)

    prediction_xgb = pickled_model.predict(input_reshaped)
    print(prediction_xgb)


    if(prediction_xgb[0] == 0):
        return 'The water is not potable'
    else:
        return 'The water is potable'


def main():
    
    #title
    st.title('Water Potability indicator')
    
    #getting input data
    
    
    ph = st.text_input('ph value')
    Hardness = st.text_input('Hardness value')
    Solids = st.text_input('Solids')
    Chloramines = st.text_input('Chloramines')
    Sulfate = st.text_input('Sulfate level')
    Conductivity = st.text_input('Conductivity')
    Organic_carbon = st.text_input('Organic_carbon')
    Trihalomethanes = st.text_input('Trihalomethanes')
    Turbidity = st.text_input('Turbidity')
    
    
    # code for prediction
    result = ''
    
    #button for result
    
    if st.button('Check'):
        result = potability_prediction([ph,Hardness,Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity])
        
    st.success(result)
    
    
if __name__ == '__main__':
    main()
    
    