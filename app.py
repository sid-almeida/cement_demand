import streamlit as st
import pandas as pd
import pickle as pkl
import os

# load the data
data = pd.read_csv('https://raw.githubusercontent.com/sid-almeida/cement_demand/main/model_data.csv')
data = data.drop(['Unnamed: 0'], axis=1)

# train model
X_train = data.drop(['demand'], axis=1)
y_train = data['demand']
from sklearn.ensemble import GradientBoostingRegressor
gbregressor = GradientBoostingRegressor(n_estimators = 100, random_state = 0)
model = gbregressor.fit(X_train, y_train)

with st.sidebar:
    st.image("https://github.com/sid-almeida/cement_demand/blob/main/Brainize%20Tech.png?raw=true", width=250)
    st.title("Cement Demand Prediction")
    choice = st.radio("**Navigation:**", ("About", "Prediction"))
    st.info('**Note:** Please be aware that this application is intended solely for educational purposes. It is strongly advised against utilizing this tool for making any financial decisions.')

if choice == "About":
    st.write("""
        # Cement Demand Prediction
        This app predicts the demand of cement of a company for a certain period in time!
        """)
    st.write('---')
    st.write('**About the App:**')
    st.write(
        'Utilizing a Gradient Boosting Regressor, the aforementioned approach employs a meticulously trained model encompassing 8 distinct features. Its primary objective is to predict the demand for a cement company in India.')
    st.info(
        '**Note:** Please be aware that this application is intended solely for educational purposes. It is strongly advised against utilizing this tool for making any financial decisions.')
    st.write('---')
    st.write('**About the Data:**')
    st.write(
        'The dataset is related to Cement Sales and Demand in India, it also contains some external factors that which affecting the sales and demand of cement.\n'
        'It has features like Production, Sales, Demand, Population, GDP, Loan Disbursement, and Interest Rates.\n'
        'This is a simulated dataset, Data was collected in a yearly format and then simulated on the basis of research papers\n'
        'For more information, please visit the [**DataSet**](https://www.kaggle.com/datasets/kishorkhengare/cement-sales-demand)')
    st.write('---')

if choice == "Prediction":
    production = st.number_input('Production', min_value=0, max_value=100000000, value=0)
    sales = st.number_input('Sales', min_value=0, max_value=100000000, value=0)
    population = st.number_input('Population', min_value=0, max_value=100000000, value=0)
    gdp = st.number_input('GDP', min_value=0, max_value=100000000, value=0)
    disbursement = st.number_input('Loan Disbursement', min_value=0, max_value=100000000, value=0)
    interest_rate = st.number_input('Interest Rate', min_value=0, max_value=100000000, value=0)
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox('Select Month', ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                                               'November', 'December'))
        if option == 'January':
            month = 1
        elif option == 'February':
            month = 2
        elif option == 'March':
            month = 3
        elif option == 'April':
            month = 4
        elif option == 'May':
            month = 5
        elif option == 'June':
            month = 6
        elif option == 'July':
            month = 7
        elif option == 'August':
            month = 8
        elif option == 'September':
            month = 9
        elif option == 'October':
            month = 10
        elif option == 'November':
            month = 11
        elif option == 'December':
            month = 12
    with col2:
        year = st.number_input('Select Year', min_value=2010, max_value=2024, value=2010)

    if st.button('Predict'):
        prediction = model.predict([[production, sales, population, gdp, disbursement, interest_rate, month, year]])
        st.success('The demand for the cement company in the given period is {}'.format(prediction[0]))

st.write('Made with ❤️ by [Sidnei Almeida](https://www.linkedin.com/in/saaelmeida93/)')
