import streamlit as st
import joblib as jb
import numpy as np


#Load the model from file 
obj=jb.load('california.joblib')
model=obj['model']
cols=obj['columns']


#Header
st.header('California Housing Model')
input=[]

#Add input columns 
for i in cols:
    v = st.number_input(f'Enter the value for {i}: ')
    input.append(v)

#Calculate the median house value
if st.button('Click'):
    #Convert list in to array 
    Input = np.array([input])
    #Pass the input array to predict the value
    out = model.predict(Input)
    st.success(f'The Median House value  is {out}')


