import streamlit as st
import pandas as pd
from processor import prepare_and_train

st.set_page_config(page_title="Swift Sales Forecast")

st.title("Sales Performance & Forecasting Platform")
st.write("Real-time insights and revenue prediction engine")
#Run on backend
model,df=prepare_and_train()
#Sidebar for user input
st.sidebar.header("Run On-Demand Forecast")
region = st.sidebar.selectbox("Select Region",df['Region'].unique())
last_sales = st.sidebar.number_input("Last Month's Revenue($)",value=40000)
trend = st.sidebar.number_input("3-Month Average Trend($)",value=42000)
#prediction logic
if st.sidebar.button("Predict Next Month"):
    prediction=model.predict([[last_sales,trend]])
    st.sidebar.success(f"Predicted Revenue: ${prediction[0]:,.2f}")

#Main Dashboard Visuals
col1,col2 = st.columns(2)
with col1:
    st.subheader(f"Revenue Trend:{region}")
    region_data=df[df['Region']==region]
    st.line_chart(region_data.set_index('Date')['Revenue'])
with col2:
    st.subheader("Data Preview")
    st.dataframe(df.tail(10))

st.info("Note: This model uses Random Forest Regression with Lag features to capture seasonality")