import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv("vehicles_us.csv")
st.header("Vehicle best features choices")
st.write("***What do you first look for when getting a car?***")

hist_button = st.button("Show Histogram")
if hist_button:
    st.write("Histogram of Vehicle Model vs Condition")
    fig = px.histogram(vehicles, x="model", color="condition", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button("Show Scatter Plot")
if scatter_button:
    st.write("Dispersion graphic of Vehicle odometer vs price")
    fig = px.histogram(vehicles, x="odometer", y ="price", color="transmission", marginal="box")
    st.plotly_chart(fig, use_container_width=True)