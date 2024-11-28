import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Car Data Analysis Dashboard')


data = pd.read_csv('Car_Sales.csv') 


st.subheader('Dataset Preview')
st.write(data.head())


st.subheader('Sales by Manufacturer')
sales_by_manufacturer = data.groupby('Manufacturer')['Sales_in_thousands'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_manufacturer)


st.subheader('Price vs Horsepower')
fig, ax = plt.subplots()
sns.scatterplot(x='Price_in_thousands', y='Horsepower', data=data, ax=ax)
ax.set_title('Price vs Horsepower')
st.pyplot(fig)


st.subheader('Fuel Efficiency Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Fuel_efficiency'], kde=True, ax=ax)
ax.set_title('Fuel Efficiency Distribution')
st.pyplot(fig)


st.subheader('Engine Size vs Price')
fig, ax = plt.subplots()
sns.scatterplot(x='Engine_size', y='Price_in_thousands', data=data, ax=ax)
ax.set_title('Engine Size vs Price')
st.pyplot(fig)


st.subheader('Yearly Resale Value by Vehicle Type')
resale_by_type = data.groupby('Vehicle_type')['__year_resale_value'].mean()
st.bar_chart(resale_by_type)


st.subheader('Power Performance Factor Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Power_perf_factor'], kde=True, ax=ax)
ax.set_title('Power Performance Factor Distribution')
st.pyplot(fig)
