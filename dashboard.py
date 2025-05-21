import pandas as pd
import plotly.express as px
import streamlit as st

# Streamlit page layout config
st.set_page_config(layout="wide")

# Dataframe (df) creation
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")

# Conversion to datetime format and filtering data by "Date"
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Views by YYYY-MM
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Month", df["Month"].unique())
df_filtered = df[df["Month"] == month]

#Plot placement
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

## 1 - Profit per Day 
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Profit per Day")
col1.plotly_chart(fig_date, use_container_width=True)

## 2 - Profit per Product Type 
fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", title="Profit per Product Type", orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

## 3 - Profit per City
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", color="City", title="Profit per City")
col3.plotly_chart(fig_city, use_container_width=True)

## 4 - Profit per Payment Type
fig_pay = px.pie(df_filtered, values="Total", names="Payment", color="Payment", title="Profit per Payment Type")
col4.plotly_chart(fig_pay, use_container_width=True)

## 5 - Profit per City
city_total = df_filtered.groupby("City")[["Rating"]].sum().reset_index()
fig_rating = px.bar(city_total, x="City", y="Rating", color="City", title="Rating")
col5.plotly_chart(fig_rating, use_container_width=True)
