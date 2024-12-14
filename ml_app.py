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
    income = st.selectbox('Income (scale 1-9)', options=list(range(1, 10)),
                             help="Enter the user's income level on a scale of 1 to 9.")
    education = st.selectbox('Education (scale 1-8)', options=list(range(1, 9)),
                                help="Enter the user's education level on a scale of 1 to 8.")
    parent = st.radio('Parent', options=['Yes', 'No'], index=0)
    married = st.radio('Married', options=['Yes', 'No'], index=0)
    female = st.radio('Female', options=['Yes', 'No'], index=0)
    age = st.number_input('Age', min_value=0, max_value=100, value=25, step=1,
                          help="Enter the user's age.")
    submit_button = st.form_submit_button('Predict')

if submit_button:
    # Map inputs back to binary values
    parent = 1 if parent == "Yes" else 0
    married = 1 if married == "Yes" else 0
    female = 1 if female == "Yes" else 0

    prediction, probability = linkedin(income, education, parent, married, female, age)
    st.write(f"Prediction: {prediction}")
    st.write(f"Probability of being a LinkedIn user: {probability:.2f}")