import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SLA Monitoring Test")
st.write("If you can see this, deployment worked!")

# Simple test
df = pd.DataFrame({
    'Status': ['Within SLA', 'Delayed', 'Breached'],
    'Count': [80, 15, 5]
})

fig = px.pie(df, values='Count', names='Status', title='SLA Status')
st.plotly_chart(fig)
