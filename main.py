import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Customizing the theme with chosen vibrant primary colors
COLOR_PRIMARY = "#FF5733"  # Orange
COLOR_SECONDARY = "#33FFC7"  # Cyan
COLOR_ACCENT = "#FFD700"  # Gold
COLOR_TEXT = "#222222"  # Black
COLOR_BG = "#F5F5DC"  # Beige

def load_data():
    # Load your CSV data
    car = pd.read_csv("Cleaned_Car_Data.csv")
    return car

def load_model():
    # Load your ML model
    model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))
    return model

def main():
    # Setting the overall theme with brighter and vibrant colors
    st.markdown(
        f"""
        <style>
            .reportview-container .main .block-container{{
                max-width: 700px;
                padding-top: 2rem;
                padding-right: 2rem;
                padding-left: 2rem;
                padding-bottom: 2rem;
                background-color: {COLOR_BG};  /* Light grey background */
            }}
            .reportview-container .main {{
                color: {COLOR_TEXT};  /* Dark grey text */
            }}
            /* Update selectbox colors */
            .css-2b097c-container {{
                background: {COLOR_SECONDARY};  /* Light green background for select boxes */
                color: {COLOR_TEXT};  /* Dark grey text for select boxes */
            }}
            .css-yk16xz-control {{
                background: {COLOR_SECONDARY};  /* Light green background for control elements */
            }}
            .css-g1d714-ValueContainer {{
                color: {COLOR_TEXT};  /* Dark grey text for selected values */
            }}
            /* Update slider colors */
            .st-e3b7q8.st-e3b7q81.st-17vr8c6.st-1bv5qo5 {{
                background: {COLOR_PRIMARY};  /* Coral red background for slider */
            }}
            .st-e3b7q8.st-e3b7q81.st-17vr8c6.st-1bv5qo5.st-15exv82.st-1bnf04w {{
                background: {COLOR_PRIMARY};  /* Coral red background for slider */
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title of the Streamlit app with brighter and vibrant colors
    st.title('Car Price Prediction')
    st.markdown('---')

    # Load data and model
    car = load_data()
    model = load_model()

    # Get unique values for dropdowns
    companies = ['Select Company'] + sorted(car['company'].unique())
    car_models = ['Select Car Model']
    years = ['Select Year'] + sorted(car['year'].unique())
    fuel_types = ['Select Fuel Type'] + sorted(car['fuel_type'].unique())

    # Dropdowns and input fields for user input with updated colors
    with st.container():
        st.markdown("**Select car details:**")
        company = st.selectbox('Company', companies, help="Select the car's company")

        # Update models based on selected company
        if company != "Select Company":
            car_models = ['Select Car Model'] + sorted(car[car['company'] == company]['name'].unique())

        car_model = st.selectbox('Car Model', car_models, help="Select the car's model")
        year = st.selectbox('Year', years, help="Select the manufacturing year of the car")
        fuel_type = st.selectbox('Fuel Type', fuel_types, help="Select the fuel type of the car")
        kms_driven_input = st.text_input('Kilometers Driven (or type)', value='')
        kms_driven_slider = st.slider('Kilometers Driven', min_value=0, max_value=int(car['kms_driven'].max()), value=int(car['kms_driven'].mean()), step=5000, format="%d km", help="Select the kilometers driven")

    # Use the slider value if input is empty, otherwise use the input value
    kms_driven = int(kms_driven_input) if kms_driven_input else kms_driven_slider


    if st.button('Predict', help="Click to get the car price prediction"):
        if company != "Select Company" and car_model != "Select Car Model" and year != "Select Year" and fuel_type != "Select Fuel Type" and kms_driven != 0:
            prediction = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
            
            # Ensuring positive values
            lower_bound = max(0, np.round(prediction[0], 2) - 10000)
            upper_bound = np.round(prediction[0], 2) + 10000
            st.write(f'<span style="font-size:24px;">The predicted price range of the car is: ₹{lower_bound} - ₹{upper_bound}</span>', unsafe_allow_html=True)
        else:
            st.warning('Please fill in all the fields.')



if __name__ == '__main__':
    main()
