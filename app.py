import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Customer Segmentation Dashboard")

# Load data
data = pd.read_csv('clustered_customer_data.csv')
metrics = pd.read_csv('segment_metrics.csv')

# Display metrics
st.header("Segment Metrics")
st.dataframe(metrics)

# Visualizations
st.header("Visualizations")
st.image('clusters.png', caption='Customer Segments', use_column_width=True)
st.image('avg_order_value_by_cluster.png', caption='Average Order Value by Cluster', use_column_width=True)
st.image('correlation_heatmap.png', caption='Feature Correlations', use_column_width=True)

# Display recommendations
st.header("Recommendations")
with open('recommendations.md', 'r') as f:
    st.markdown(f.read())