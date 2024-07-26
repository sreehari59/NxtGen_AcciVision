# https://nxtgenaccivision.streamlit.app/
import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from pycaret.regression import *
from flask import Flask, request

loaded_best_model = load_model('best-model')

class User_input(BaseModel):
    year: int
    month: int

app= FastAPI()

apps = Flask(__name__)

@apps.route('/foo')
def serve_foo():
    return 'This page is served via Flask!'

@apps.route("/apipredict", methods=["POST"])
def apiPredict():

    req_data = request.get_json()
    print(req_data)
    return {'prediction': 21}

apps.run(port=8888)

@app.post('/predict')
def get_forecast(input:User_input):
    if input.month not in range(1, 13):
        return {"Error": "Must be Valid input -> Month"}, 400
    else:
        print("Year:",input.year,"Month:",input.month)
        data = pd.DataFrame({
            "Category":["Alkoholunfälle"],
            "Accident_Type":["insgesamt"],
            "Year":[input.year],
            "Month":[input.month]
                })
        predicted_output = predict_model(loaded_best_model, data=data)
        predicted_val = predicted_output["prediction_label"].values[0]
        return {'prediction': predicted_val}


def main():
    # App title
    st.markdown("""
            <div style='text-align: center;'>
                <h1>Next Gen Accident Forecaster</h1>
            </div>
            <style>
            body {
                background-color: #F0F8FF;
            }
            </style>
        """, unsafe_allow_html=True)

    category = st.selectbox('Category', ("Verkehrsunfälle","Alkoholunfälle","Fluchtunfälle"))
    accident_type = st.selectbox('Accident Type', ("insgesamt" ,"Verletzte und Getötete","mit Personenschäden"))
    year = st.slider("Year", 2000, 2024)
    month = st.slider("Month", 1, 12)

    data = pd.DataFrame({
        "Category":[category],
        "Accident_Type":[accident_type],
        "Year":[year],
        "Month":[month]
            })

    if st.button('Submit'):

        predicted_output = predict_model(loaded_best_model, data=data)
        predicted_val = predicted_output["prediction_label"].values[0]
        st.write("Predicted values is: ",predicted_val)

if __name__=='__main__':
    main()

