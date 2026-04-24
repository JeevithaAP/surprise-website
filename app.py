import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

st.title("📊 Data Analytics Dashboard")

# Load data
df = pd.read_csv("Nassau.csv")

# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]

# KPIs
st.subheader("Key Metrics")

col1, col2 = st.columns(2)
col1.metric("Total Sales", int(filtered_df["Sales"].sum()))
col2.metric("Total Profit", int(filtered_df["Profit"].sum()))

# Charts
st.subheader("Visualizations")

fig1 = px.bar(filtered_df, x="Region", y="Sales", color="Region")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.pie(filtered_df, names="Category", values="Profit")
st.plotly_chart(fig2, use_container_width=True)

# Insights
st.subheader("Insights")

st.write("• Sales vary across regions.")
st.write("• Some categories generate more profit.")
st.write("• Filters help analyze data interactively.")

# Power BI placeholder
st.subheader("Power BI Dashboard")

st.write("Power BI dashboard will be embedded here.")
