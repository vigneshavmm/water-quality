import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

# Load the model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = joblib.load("my_scaler.save")

# Define the Streamlit app
def main():
    st.title("Water Quality Prediction")

    # Define the input fields
    ph = st.number_input('ph', min_value=0.0, max_value=14.0, step=0.1)
    hardness = st.number_input('Hardness', min_value=0.0, step=0.1)
    solids = st.number_input('Solids', min_value=0.0, step=0.1)
    chloramines = st.number_input('Chloramines', min_value=0.0, step=0.1)
    sulfate = st.number_input('Sulfate', min_value=0.0, step=0.1)
    conductivity = st.number_input('Conductivity', min_value=0.0, step=0.1)
    organic_carbon = st.number_input('Organic carbon', min_value=0.0, step=0.1)
    trihalomethanes = st.number_input('Trihalomethanes', min_value=0.0, step=0.1)
    turbidity = st.number_input('Turbidity', min_value=0.0, step=0.1)

    # When the user clicks the Predict button
    if st.button('Predict'):
        # Prepare the feature vector
        input_features = [ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]
        features_value = [np.array(input_features)]
        feature_names = ["ph", "Hardness", "Solids", "Chloramines", "Sulfate", "Conductivity", "Organic_carbon", "Trihalomethanes", "Turbidity"]

        # Create a DataFrame and scale the features
        df = pd.DataFrame(features_value, columns=feature_names)
        df = scaler.transform(df)

        # Make the prediction
        output = model.predict(df)
        prediction = "safe" if output[0] == 1 else "not safe"

        # Display the result
        st.success(f"Water is {prediction} for human consumption")

# Run the Streamlit app
if __name__ == "__main__":
    main()
