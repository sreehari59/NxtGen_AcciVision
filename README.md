# NxtGen_AcciVision

NxtGen_AcciVision or Next Generation Accident Forecaster helps in forecasting the future accidents. This is project is part of a Digital Product School Challenge. The challenge consist of 3 parts:
1. Mission 1: Create a AI Model
2. Mission 2: Publish your source code & Deploy
3. Mission 3: Post the URL to the endpoint

## Demo
The application can be viewed in this link [link](https://nxtgenaccivision.streamlit.app/) or the API endpoint `sree1996.pythonanywhere.com` can be used to get the predictions.
Note: The endpoint only accepts a POST request with a JSON body
```
{
"year":2020,
"month":10
}
```
And it return the applications prediction in the following format:
```
{
"prediction":value
}
```

## Data Description
The dataset used is "Monatszahlen Verkehrsunfälle" which is the Dataset from the [München Open Data Portal](https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7). The features used for the forecast are:
1. Category
2. Accident-type
3. Year
4. Month
5. Value

## Mission 1: Create a AI Model
As the first step the exploratory data analysis was done. I made use of [pycaret](https://pycaret.org/) package to train the model. The main advantage is that it runs all the possible model and provides a comparitive analysis of the different machine learning models. The data set had data from year 2000 to 2024. To build the prediction model, data up until 2020 was used. Due to the limited features and limited data available Meta model Prophet or other time series model like ARIMA, SARIMA were not used. 

## Mission 2: Deploy AI model
To deploy the AI model [Streamlit Community Cloud](https://docs.streamlit.io/deploy/streamlit-community-cloud) was used. The endpoint was setup using [PythonAnywhere](https://www.pythonanywhere.com/) as streamlit cloud does not support endpoint creation. The successfulness of the endpoint was verified with the help of [Thunder Client](https://www.thunderclient.com/).

## Mission 3: Post the URL to the endpoint
The final step was to post a request to the challenge endpoint with the a given body format.

## Tec Stack Used
1. Flask
2. streamlit
3. pycaret
4. pandas

## EDA and Result










