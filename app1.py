"Developed by -> Tariq"
import numpy as np
import pickle
import pandas as pd
import streamlit as st

from PIL import Image
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)
def welcome():
    return "Welcome All"


def predict_card_default(LB, edu, mar, Age, pa, B1, B2, B3, B4, B5, B6, P1, P2, P3, P4, P5, P6):
   

    prediction = classifier.predict([[LB, edu, mar, Age, pa, B1, B2, B3, B4, B5, B6, P1, P2, P3, P4, P5, P6]])
    print(prediction)
    return prediction


def main():
    st.title("Developed by : Mohammad Tariq")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card default </h2>
    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)
    LB = st.text_input("Limited Balance")
    Edu = st.selectbox("Education", ('Graduate School', 'University', 'High School', 'Others'))
    edu = 1
    if Edu == 'Graduate School':
        ed = 1
    elif Edu == 'University':
        ed = 2
    elif Edu == 'High School':
        ed = 3
    elif Edu == 'Others':
        ed = 4

    Mar = st.selectbox("Status", ("Married", 'Single', 'Other'))
    mar = 1
    if Mar == 'Married':
        mar = 1
    elif Mar == 'Single':
        mar = 2
    elif Mar == 'Other':
        mar = 3
    Age = st.text_input("Age")
    pay1 = st.selectbox('', ('Account started that month with a zero balance, and never used any credit'
                                  , 'Account had a balance that was paid in full'
                                  , 'At least the minimum payment was made, but the entire balance wasnt paid'
                                  , 'Payment delay for 1 month'
                                  , 'Payment delay for 2 month'
                                  , 'Payment delay for 3 month'
                                  , 'Payment delay for 4 month'
                                  , 'Payment delay for 5 month'
                                  , 'Payment delay for 6 month'
                                  , 'Payment delay for 7 month'
                                  , 'Payment delay for 8 month'))
    pa = -2
    if pay1 == 'Account started that month with a zero balance, and never used any credit':
        pa = -2
    elif pay1 == 'Account had a balance that was paid in full':
        pa = -1
    elif pay1 == 'At least the minimum payment was made, but the entire balance wasnt paid':
        pa = 0
    elif pay1 == 'Payment delay for 1 month':
        pa = 1
    elif pay1 == 'Payment delay for 2 month':
        pa = 2
    elif pay1 == 'Payment delay for 3 month':
        pa = 3
    elif pay1 == 'Payment delay for 4 month':
        pa = 4
    elif pay1 == 'Payment delay for 5 month':
        pa = 5
    elif pay1 == 'Payment delay for 6 month':
        pa = 6
    elif pay1 == 'Payment delay for 7 month':
        pa = 7
    elif pay1 == 'Payment delay for 8 month':
        pa = 8
    B1 = st.text_input("Last month Bill Amount (in New Taiwanese (NT) dollar)")
    B2 = st.text_input("Last 2nd month Bill Amount (in New Taiwanese (NT) dollar)")
    B3 = st.text_input("Last 3rd month Bill Amount (in New Taiwanese (NT) dollar)")
    B4 = st.text_input("Last 4th month Bill Amount (in New Taiwanese (NT) dollar)")
    B5 = st.text_input("Last 5th month Bill Amount (in New Taiwanese (NT) dollar)")
    B6 = st.text_input("Last 6th month Bill Amount (in New Taiwanese (NT) dollar)")
    P1 = st.text_input("Amount paid in Last Month (in New Taiwanese (NT) dollar)")
    P2 = st.text_input("Amount paid in Last 2nd Month (in New Taiwanese (NT) dollar)")
    P3 = st.text_input("Amount paid in Last 3rd Month (in New Taiwanese (NT) dollar)")
    P4 = st.text_input("Amount paid in Last 4th Month (in New Taiwanese (NT) dollar)")
    P5 = st.text_input("Amount paid in Last 5th Month (in New Taiwanese (NT) dollar)")
    P6 = st.text_input("Amount paid in Last 6th Month (in New Taiwanese (NT) dollar)")
    result=[]
    if st.button("Predict"):
        result = predict_card_default(LB, edu, mar, Age, pa, B1, B2, B3, B4, B5, B6, P1, P2, P3, P4, P5, P6)
        if result[0]==1:
            st.success('This account will be defaulted')
        else:
            st.success('This account will NOT be defaulted')
        
        
    
    #st.text("Developed by : Mohammad Tariq")


if __name__ == '__main__':
    main()