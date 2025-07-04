# Customer Segmentation Analysis

This project analyzes customer purchase data from an e-commerce dataset to segment users into distinct groups using K-means clustering. It includes exploratory data analysis (EDA), data preprocessing, clustering, SQL queries for metrics, visualizations, and marketing recommendations to drive targeted campaigns. A Streamlit dashboard provides an interactive interface to view segment metrics, visualizations, and recommendations.

## Project Overview
- **Dataset**: [Online Retail Dataset](https://www.kaggle.com/datasets/vijayuv/onlineretail) from Kaggle.
- **Tasks**:
  - Cleaned and preprocessed data using Pandas to handle missing values and outliers.
  - Applied K-means clustering based on purchase frequency, average order value, and recency.
  - Visualized clusters using Seaborn and Matplotlib (scatter plots, boxplots, heatmaps).
  - Queried metrics like total revenue per segment using SQLite.
  - Provided marketing recommendations with an estimated 10-15% revenue increase.
- **Tools**: Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib), SQLite, Streamlit.

## Repository URL
- GitHub Repository: https://github.com/akhildungala/Customer-Segmentation-Analysis-for-E-Commerce

## Deployed Dashboard
- Streamlit App: https://csa-e-commerce.streamlit.app/

## Files
- `app.py`: Streamlit dashboard script to display segment metrics, visualizations, and recommendations.
- `requirements.txt`: Dependencies for running the Streamlit app.
- `cleaned_customer_data.csv`: Preprocessed customer data after cleaning and feature engineering.
- `clustered_customer_data.csv`: Customer data with cluster assignments from K-means.
- `segment_metrics.csv`: Metrics per segment (e.g., customer count, total revenue).
- `clusters.png`, `avg_order_value_by_cluster.png`, `correlation_heatmap.png`: Visualization outputs.
- `recommendations.md`: Marketing recommendations based on cluster insights.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/customer-segmentation.git
   cd customer-segmentation
   ```
2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit Dashboard**:
   ```bash
   streamlit run app.py
   ```
   - Access the dashboard at `http://localhost:8501`.

## Deployment
- The dashboard is deployed on Streamlit Cloud at https://csa-e-commerce.streamlit.app/
- To deploy your own instance:
  1. Push the repository to GitHub.
  2. Connect the repository to Streamlit Cloud, selecting `app.py` as the main file.
  3. Deploy to get a public URL.
- Ensure all files (`app.py`, `requirements.txt`, CSVs, PNGs, `recommendations.md`) are in the repository root.

## Generating Data (Optional)
If CSV or PNG files are missing, regenerate them using the following scripts in Google Colab:
1. **Preprocessing**: Run `preprocess.py` with the dataset (`OnlineRetail.csv`) to generate `cleaned_customer_data.csv`.
2. **Clustering**: Run `clustering.py` to generate `clustered_customer_data.csv` and `clusters.png`.
3. **SQL Queries**: Run `run_queries.py` to generate `segment_metrics.csv`.
4. **Visualizations**: Run `visualize.py` to generate `avg_order_value_by_cluster.png` and `correlation_heatmap.png`.
5. **Recommendations**: The `recommendations.md` file is provided directly.

## Notes
- **Dataset**: Ensure the dataset has columns `CustomerID`, `InvoiceNo`, `Quantity`, `UnitPrice`, and `InvoiceDate`.
- **Large Files**: If CSV files exceed GitHub’s 100 MB limit, use Git LFS or regenerate them using the scripts.
- **Validation**: Use silhouette scores or the elbow method to validate clustering (see Colab scripts for code).
- **Business Impact**: Recommendations target a 10-15% revenue increase through loyalty programs, bundle deals, and re-engagement campaigns.