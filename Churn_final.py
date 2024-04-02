# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 06:10:00 2024

@author: Ravish
"""

import streamlit as st
import pandas as pd
import joblib
import numpy as np

def main():
    
    html_temp="""
<style>
[data-testid="stAppViewContainer"]{
     background-color:#86aaf8;    # light blue:
   
}
.fa {
    font-size=500px !important;
}

</style>
"""
    Model=joblib.load('bank_churn_model_final')
    st.markdown(html_temp,unsafe_allow_html=True) 
    st.write('')
    st.write('')
    st.write('')
    st.write('')
    st.title("Customer Churn Prediction")
    # st.subheader()
    
    Gender=st.radio("**Select Your Gender..!!**",("Male","Female"))
    if Gender=="Male":
        Gender=0
    elif Gender=="Female":
        Gender=1
        
    age = st.slider('Select your age', min_value=0, max_value=120, value=25)
    
    Tenure=st.number_input("**Tenure**",0,10,step=1)
    
    CreditScore=st.number_input("**Enter credit Score**",300,1000,step=1)
    
    Balance=st.number_input("**Enter Balance**",0,40000,step=1)
    
    NumOfProduct=st.number_input("**Enter number of services**",1,5,step=1)
    
    HascrCard=st.selectbox("**Do customer have  credit card**",('YES','NO'))
    if HascrCard=='YES':
        HascrCard=1
    elif HascrCard=='NO':
        HascrCard=0
        
    Active=st.selectbox("**Customer is active or not**",('YES','NO'))
    if Active=='YES':
        Active=1
    elif Active=='NO':
        Active=0
    
    Salary=st.number_input("**Enter Salary**",100,300000,step=1)
    
    
    Geography=st.selectbox("**Do customer have  credit card**",('Germany','Spain','France'))
    if Geography=='Germany':
        Germany=1
        Spain=0
        France=0
    elif Geography=='Spain':
        Germany=0
        Spain=1
        France=0
    elif Geography=='France':
        Germany=0
        Spain=0
        France=1
    
    sample_data = {
    'CreditScore': [CreditScore],
    'Age': [age],
    'Tenure': [Tenure],
    'Balance': [Balance],
    'NumOfProducts': [NumOfProduct],
    'HasCrCard': [HascrCard],  
    'IsActiveMember': [Active],  
    'EstimatedSalary': [Salary],
    'Geography_Germany': [Germany],  
    'Geography_Spain': [Spain],  
    'Gender_Male': [Gender]  
    }
    
    new_data = pd.DataFrame(sample_data)

    

    if st.button("Predict"):
        pred=Model.predict(new_data)
        prob=Model.predict_proba(new_data)
        if pred[0]==1:
            st.warning(":black[Sorry customer will leave] :disappointed_relieved: ")
        else:
            st.balloons()
            st.success("customer will not leave with probability of {} % ".format(np.floor(prob[0][1]*100)))
      

    
    
 

if __name__=='__main__':
    main()