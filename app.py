import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Car Data Analysis Dashboard')

# Load the data from the CSV file
data = pd.read_csv('Car_Sales.csv')  # Replace with your actual file path

# Show dataset preview (first 5 rows)
st.subheader('Dataset Preview')
st.write(data.head())

# Sales Analysis: Total Sales by Manufacturer
st.subheader('Sales by Manufacturer')
sales_by_manufacturer = data.groupby('Manufacturer')['Sales_in_thousands'].sum().sort_values(ascending=False)
st.bar_chart(sales_by_manufacturer)

# Price vs Horsepower Analysis: Scatter plot
st.subheader('Price vs Horsepower')
fig, ax = plt.subplots()
sns.scatterplot(x='Price_in_thousands', y='Horsepower', data=data, ax=ax)
ax.set_title('Price vs Horsepower')
st.pyplot(fig)

# Fuel Efficiency Distribution: Histogram
st.subheader('Fuel Efficiency Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Fuel_efficiency'], kde=True, ax=ax)
ax.set_title('Fuel Efficiency Distribution')
st.pyplot(fig)

# Engine Size vs Price: Scatter plot
st.subheader('Engine Size vs Price')
fig, ax = plt.subplots()
sns.scatterplot(x='Engine_size', y='Price_in_thousands', data=data, ax=ax)
ax.set_title('Engine Size vs Price')
st.pyplot(fig)

# Yearly Resale Value by Vehicle Type: Bar chart
st.subheader('Yearly Resale Value by Vehicle Type')
resale_by_type = data.groupby('Vehicle_type')['__year_resale_value'].mean()
st.bar_chart(resale_by_type)

# Power Performance Factor Distribution
st.subheader('Power Performance Factor Distribution')
fig, ax = plt.subplots()
sns.histplot(data['Power_perf_factor'], kde=True, ax=ax)
ax.set_title('Power Performance Factor Distribution')
st.pyplot(fig)
