# important to add the .py extension in the name 
# Example 1 
import streamlit as st 
import plotly.express as px 
import pandas as pd 
pip install --upgrade pip

# Title of the app 
st.title("Streamlit Dashboard with Plotly")

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
}
df = pd.DataFrame(data)

# Create a bar chart 
fig = px.bar(df, x="Category", y="Values", title="Sample Bar Chart")

# Display the chart in Streamlit
st.plotly_chart(fig)
