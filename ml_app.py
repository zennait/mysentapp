import pickle
import streamlit as st
import pandas as pd


with open('log_regression.pkl', 'rb') as file:
    lr = pickle.load(file)


def linkedin(income,education, parent, married,female, age) :
    input_data = pd.DataFrame({
        'income': [income],     
        'education': [education],
        'parent': [parent],
        'married': [married],
        'female': [female],
        'age': [age],

    })

    prediction = lr.predict(input_data)
    probability = lr.predict_proba(input_data)[0][1]
    if prediction [0]==1:
        return 'This is a LinkedIn user', probability
    else:
        return 'Not a LinkedIn user', probability
    

st.title('LinkedIn User Predictor')
st.markdown("This app predicts whether a person is a LinkedIn user based on their attributes.")
with st.form('user_input'):
    income = st.selectbox(
        'Income (Household)',
        options=[
            '1 - Less than $10,000',
            '2 - $10,000 to under $20,000',
            '3 - $20,000 to under $30,000',
            '4 - $30,000 to under $40,000',
            '5 - $40,000 to under $50,000',
            '6 - $50,000 to under $75,000',
            '7 - $75,000 to under $100,000',
            '8 - $100,000 to under $150,000',
            '9 - $150,000 or more'
        ],
        help="Select the user's household income level."
    )

    education = st.selectbox(
        'Education (Highest Level Completed)',
        options=[
            '1 - Less than high school',
            '2 - High school incomplete',
            '3 - High school graduate',
            '4 - Some college, no degree',
            '5 - Two-year associate degree',
            '6 - Four-year college degree',
            '7 - Some postgraduate or professional schooling',
            '8 - Postgraduate or professional degree'
        ],
        help="Select the user's highest level of education completed."
    )

    parent = st.radio('Parent', options=['Yes', 'No'], index=0)
    married = st.radio('Married', options=['Yes', 'No'], index=0)
    female = st.radio('Female', options=['Yes', 'No'], index=0)
    age = st.number_input('Age', min_value=0, max_value=100, value=25, step=1,
                          help="Enter the user's age.")
    
    # Submit button inside the form
    submit_button = st.form_submit_button('Predict')

if submit_button:
    # Map inputs to numerical values
    income = int(income.split(' - ')[0])
    education = int(education.split(' - ')[0])
    parent = 1 if parent == "Yes" else 0
    married = 1 if married == "Yes" else 0
    female = 1 if female == "Yes" else 0

    prediction, probability = linkedin(income, education, parent, married, female, age)
    st.write(f"Prediction: {prediction}")
    st.write(f"Probability of being a LinkedIn user: {probability:.2f}")