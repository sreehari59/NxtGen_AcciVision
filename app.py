import pickle 
import streamlit as st
from fastapi import FastAPI
from pydantic import BaseModel

# model = pickle.load(open("model.pkl", "rb"))

class User_input(BaseModel):
    year: int
    month: int

app= FastAPI()

@app.post('/predict')
def get_forecast(input:User_input):
    if input.month not in range(1, 13):
        return {"Error": "Must be Valid input -> Month"}, 400
    else:
        print("Year:",input.year,"Month:",input.month)
        predicted_value = 121
        return {'prediction': predicted_value}


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
    accident_type = st.selectbox('Accident Type', ("Insgesamt" ,"Verletzte und Getötete","Mit Personenschäden"))
    year = st.slider("Year", 2000, 2024)
    month = st.slider("Month", 1, 12)
    
    if st.button('Submit'):
        print("Result is:")

if __name__=='__main__':
    main()