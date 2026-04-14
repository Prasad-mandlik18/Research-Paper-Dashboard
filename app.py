import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
df = pd.read_csv("dataset.csv")

st.title("AI Impact on Digital Media Dashboard")


# DATA ANALYSIS


st.header("Statistical Analysis")


avg_engagement = df["Engagement_Rate"].mean()
max_engagement = df["Engagement_Rate"].max()
min_engagement = df["Engagement_Rate"].min()

col1, col2, col3 = st.columns(3)
col1.metric("Average Engagement", round(avg_engagement, 2))
col2.metric("Max Engagement", max_engagement)
col3.metric("Min Engagement", min_engagement)


# FILTERS (INTERACTIVE)

st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df["Year"].unique()))
platform = st.sidebar.multiselect(
    "Select Platform",
    df["Platform"].unique(),
    default=df["Platform"].unique()
)

region = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

filtered_df = df[
    (df["Year"] == year) &
    (df["Platform"].isin(platform)) &
    (df["Region"].isin(region))
]


# VISUALIZATION


st.header("Data Visualization")

# Chart 1: Platform vs Engagement
st.subheader("Platform vs Engagement")
fig1 = px.bar(filtered_df, x="Platform", y="Engagement_Rate", color="Platform")
st.plotly_chart(fig1)

# Chart 2: Sentiment
st.subheader("Sentiment Distribution")
fig2 = px.pie(filtered_df, names="Sentiment")
st.plotly_chart(fig2)

# Chart 3: AI Usage over Time
st.subheader("AI Usage Trend")
fig3 = px.histogram(df, x="Year", color="AI_Usage_Level", barmode="group")
st.plotly_chart(fig3)

# Chart 4: Region Analysis
st.subheader("Region Distribution")
fig4 = px.bar(filtered_df, x="Region", color="Region")
st.plotly_chart(fig4)


# QUALITATIVE INSIGHTS


st.header("Key Insights")

st.write("• AI usage has increased significantly over the years.")
st.write("• Platforms like Instagram, YouTube, and TikTok show higher engagement.")
st.write("• Most users show a positive sentiment toward AI-generated content.")
st.write("• AI adoption is globally distributed across regions.")
