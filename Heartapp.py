# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import numpy as np
import streamlit as st 
from sklearn.tree import DecisionTreeClassifier
from pickle import dump
from pickle import load
import pickle


 
import pickle
import streamlit as st


 
# loading the trained model
classifier = pickle.load(open("DecisionTree_model.pkl", "rb"))

 
#@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
  
# this is the main function in which we define our webpage  

def main():       
    # front end elements of the web page 
    
    html_temp = """ 
    <div style ="background-color:Blue;padding:8px"> 
    <h1 style ="color:white;text-align:centre heading;"> Heart Disease Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    #st.title("Streamlit Heart Disease Prediction ML App")
    st.subheader("**Heart Disease Detection Application with the help of Machine Learning Classification Model**")
    # following lines create boxes in which user can enter data required to make prediction
    
    st.sidebar.subheader("Enter your health condition")


    Sex = st.sidebar.radio("Gender",["Male","Female"])
    AgeCategory = st.sidebar.radio("choose your age?",['18-24','25-29','30-34','35-39','40-44','50-54','55-59','60-64','65-69',
                                                      '70-74','75-79','80-older'])
    SleepTime= st.sidebar.slider(label = 'Average Sleep Time ', min_value = 0,max_value = 24 ,step = 1)
    Race = st.sidebar.radio("Race?",['White','Black','Asian','american Indian/Alaskan Native','Others','Hispanic'])
    BMI= st.sidebar.slider(label = 'Enter BMI ', min_value = 0.0,max_value = 100.0 ,step = 0.1)
    Stroke = st.sidebar.radio("Have you experienced heart Stroke before?",["Yes","No"])
    PhysicalHealth = st.sidebar.radio("Do you take care of your Physical health?",["Yes","No"])
    PhysicalActivity = st.sidebar.radio("Do you workout regularly?",["Yes","No"])
    Diabetic = st.sidebar.radio("Are you Diabetic?",["Yes","No"])
    Smoking = st.sidebar.radio("Smoking habits",["Yes","No"])
    AlcoholDrinking = st.sidebar.radio("Consume Alcohol?",["Yes","No"])
    MentalHealth = st.sidebar.radio("Mentally Healthy",["Yes","No"])
    DiffWalking = st.sidebar.radio("Experiencing any difficulty while walking",["Yes","No"])
    GenHealth = st.sidebar.radio("General health condition (any recurring health sickness)?",["Yes","No"])
    Asthma = st.sidebar.radio("Are you suffering from Asthama?",["Yes","No"])
    KidneyDisease = st.sidebar.radio("Diagonised by Kidney Disease?",["Yes","No"])
    SkinCancer = st.sidebar.radio(" Treated for Skin Cancer before?",["Yes","No"])



    test = [["BMI","Smoking","AlcoholDrinking","Stroke","PhysicalHealth","MentalHealth","DiffWalking","Sex","AgeCategory","Race",
         "Diabetic","PhysicalActivity","GenHealth","SleepTime","Asthma","KidneyDisease","SkinCancer"]]

    test = pd.DataFrame([{"BMI" : BMI,"Smoking" : Smoking,"AlcoholDrinking" : AlcoholDrinking ,"Stroke" : Stroke ,"PhysicalHealth" : PhysicalHealth,"MentalHealth" : MentalHealth,"DiffWalking" : DiffWalking,"Sex" : Sex,"AgeCategory" : AgeCategory ,
                      "Race" : Race,"Diabetic" : Diabetic,"PhysicalActivity" : PhysicalActivity,"GenHealth" : GenHealth ,"SleepTime" : SleepTime ,"Asthma" : Asthma,"KidneyDisease" : KidneyDisease,"SkinCancer" : SkinCancer}])


    st.table(test)


    clse = ["BMI","Smoking","AlcoholDrinking","Stroke","PhysicalHealth","MentalHealth","DiffWalking","Sex","AgeCategory","Race",
         "Diabetic","PhysicalActivity","GenHealth","SleepTime","Asthma","KidneyDisease","SkinCancer"]

    for x in clse:
        for i in test[x]:
            if i == "Yes":
                    test[x] = 1
            else:
                    test[x] = 0
                
    for i in test["Sex"]:
        if i == "Male":
                    test["Sex"] = 1
        else:
                    test["Sex"] = 0 
                
    for i in test["AgeCategory"]:
        if i == "18-24":
                test["AgeCategory"] = 0
        elif i == "25-29":
                test["AgeCategory"] = 1
        elif i == "30-34":
                test["AgeCategory"] = 2
        elif i == "35-39":
                test["AgeCategory"] = 3
        elif i == "40-44":
                test["AgeCategory"] = 4
        elif i == "45-49":
                test["AgeCategory"] = 5
        elif i == "50-54":
                test["AgeCategory"] = 6
        elif i == "55-59":
                test["AgeCategory"] = 7
        elif i == "60-64":
                test["AgeCategory"] = 8
        elif i == "65-69":
                test["AgeCategory"] = 9
        elif i == "70-74":
                test["AgeCategory"] = 10
        elif i == "75-80":
                test["AgeCategory"] = 11
        else:
                test["AgeCategory"] = 12
        
    race = ['White','Black','Asian','american Indian/Alaskan Native','Others','Hispanic']
    for i in test["Race"]:
        if i ==race[0]:
                test["Race"] = 5
        elif i ==race[1]:
                test["Race"] = 2
        elif i ==race[2]:
                test["Race"] = 1
        elif i ==race[3]:
                test["Race"] = 0
        elif i ==race[4]:
                test["Race"] = 4
        else:
                test["Race"] = 3
    
    result = ""
        
    DecisionTree_model = pickle.load(open('DecisionTree_model.pkl', 'rb'))
            
    if st.button("Predict Heart Condition"): 
                st.write('Results can be understood as below')
                st.write('*If Prediction = 0 indicates "Heart is in healthy state"*')
                st.write('*If Prediction = 1 indicates "Heart is not in healthy condition, need to visit doctor immediately"*')
                result = DecisionTree_model.predict(test)
                st.success('The output is {}'.format(result))

 

if __name__=='__main__': 
    main()

    

        
    















