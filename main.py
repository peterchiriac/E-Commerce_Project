
# Step 1: Data Collection and Integration
# The dataset was downloaded from UCI Machine Learning Repository


# 1.1 Import Libraries
import pandas as pd
import numpy as np

# 1.2 Load the dataset
file_path = '/content/Users/peter/Desktop/pete_writes_code/E-Commerce_Project/Data/Online Retail.xlsx'
data = pd.read_excel(file_path)

# 1.3 Inspect the data
# Display the first 5 rows of the data
print('First 5 rows of the data')
print(data.head())

# 1.4 Summary of the data structure
print("\nSummary of data:")
print(data.info())

# 1.5 Summary statistics for numerical columns:
print("\nStatistics of numerical columns:")
print(data.describe())

# 1.6 Outlier Detection
# Checking for outliers in Quantity, UnitPrice, and TotalSales columns
data['TotalSales'] = data['Quantity'] * data['UnitPrice']
summary_stats = data[['Quantity', 'UnitPrice', 'TotalSales']].describe()
print("\Summary statistics for Quantity, UnitPrice, 'TotalSales (Outlier detection):")
print(summary_stats)
# After checking for outliers:
# - Negative quantities were identified, representing product returns, and were retained.
# - High unit prices were reviewed and correspond to luxury items, so they were also retained.

# Step 2: Data Inspection and Cleaning

# Check for missing values
missing_values = data.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Drop rows with missing values
# for the Description column
data_cleaned = data.dropna(subset=['Description', 'CustomerID'])

# Check for duplicate rows
duplicate_rows = data_cleaned.duplicated().sum()
print(f"Duplicate rows found:{duplicate_rows}")
# Drop duplicate rows
data_cleaned = data_cleaned.drop_duplicates()

#transform CustomerID into string
data_cleaned['CustomerID'] = data_cleaned['CustomerID'].astype(str)

# Verify the change
print(data_cleaned['CustomerID'].dtypes)


print("Data after cleaning:")
print(data_cleaned.info())


# Step 3: Data Transformation

# 3.1 Feature Creation: Extracting Date and Time Information
#Ensure InvoiceDate is in datetime format:
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Extract date and time components (hour, day, month)
data['Hour'] = data['InvoiceDate'].dt.hour
data['Day'] = data['InvoiceDate'].dt.day
data['Month'] = data['InvoiceDate'].dt.month

# Display the first few rows to verify the transformations
print("Date and time components extracted:")
print(data[['InvoiceDate', 'Day', 'Hour', 'Month']].head())

# 3.2 Aggregating Data: Total Sales Per Customer
# Grouping by CustomerID to calculate total sales per customer
customer_sales = data.groupby('CustomerID')['TotalSales'].sum().reset_index()

# Sort customers by total sales
customer_sales = customer_sales.sort_values(by='TotalSales', ascending=False)

# Display the top 10 customers by total sales
print("Top 10 customers by total sales:")
print(customer_sales.head())

# 3.3 Customer Segmentation: Creating Customer Categories (High-Spending, Medium-Spending, Low-Spending)
def categorize_customer(sales):
  if sales >= 1000:
    return 'High-Spending'
  elif 500 <= sales < 1000:
    return 'Medium-Spending'
  else:
    return 'Low-Spending'

# Apply the function to create a new column 'CustomerSegment'
customer_sales['CustomerSegment'] = customer_sales['TotalSales'].apply(categorize_customer)

# Display the first few rows to verify the segmentation
print("Customer segmentation created:")
print(customer_sales.head())

# 3.4 Creating New Features Based on Customer Behaviour:

      # Recency
# Calculate the last purchase for each customer
latest_purchase = data.groupby('CustomerID')['InvoiceDate'].max().reset_index()
# Calculate recency (difference between current date and last purchase date)
latest_purchase['Recency'] = (pd.Timestamp.now() - latest_purchase['InvoiceDate']).dt.days
# Merge recency back into the main customer_sales DataFrame
customer_sales = customer_sales.merge(latest_purchase[['CustomerID', 'Recency']], on='CustomerID')

print("Recency feature created:")
print(customer_sales.head())

      # Frequency
# Calculate the frequency of purchases for each customer
frequency = data.groupby('CustomerID')['InvoiceNo'].nunique().reset_index()
frequency.columns = ['CustomerID', 'Frequency']
# Merge frequency back into the main customer_sales DataFrame
customer_sales = customer_sales.merge(frequency, on='CustomerID')

print("Frequency feature created:")
print(customer_sales.head())

# 3.5 Customer Lifteime Value (CLV) Prediction

customer_sales['CLV'] = customer_sales['TotalSales'] * customer_sales['Frequency']
print("Customer Lifetime Value (CLV) calculated:")
print(customer_sales[['CustomerID', 'CLV']].head())

# 3.6 Creating Categorical Features Based on Purchase Amount

# Define spending categories based on TotalSales
bins = [0, 100, 500, 1000, data['TotalSales'].max() + 1]
labels = ['Low-Spending', 'Medium-Spending', 'High-Spending', 'Very-High-Spending']
# Create a new column for spending categories
data['SpendingCategory'] = pd.cut(data['TotalSales'], bins=bins, labels=labels)
# Display the first few rows
print(data[['CustomerID', 'TotalSales', 'SpendingCategory']].head())

# Step 4 - Statistical Analysis

# In this section, we analyze relationships between key variables (`TotalSales`, `Frequency`, `Recency`)
# and assess the distribution of customer segments.
# The goal is to extract insights from customer behavior and spending patterns.

# 4.1 Correlation Analysis - Check relationships between TotalSales, Frequency, and Recency
correlation_matrix = customer_sales[['TotalSales', 'Frequency', 'Recency']].corr()
print("Correlation matrix:")
print(correlation_matrix)

### Insights
# Customers who buy more frequently tend to spend more (moderate correlation: 0.566).
# Recency is not a strong predictor of total spending, but there is a slight negative relationship (-0.132).
# Frequent buyers tend to have purchased more recently, but the relationship is weak (-0.259).


# 4.2 Analyze the distribution of customer segments
segment_distribution = customer_sales['CustomerSegment'].value_counts(normalize=True) * 100

print("Customer Segment Distribution (%):")
print(segment_distribution)


# Step 5 - Data Visualisation

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# 5.1 Plot Customer Segment Distribution
plt.figure(figsize=(8,6))
sns.countplot(x='CustomerSegment', data=customer_sales, order=['Low-Spending', 'Medium-Spending', 'High-Spending'])
plt.title('Customer Segment Distribution', fontsize=16)
plt.xlabel('Customer Segment', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.show()

# 5.2 Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap', fontsize=16)
plt.show()

# 5.3 Bar Plot of Customer Lifetime Value (CLV)

top_customers = customer_sales.nlargest(10, 'CLV')
# Ensure CustomerID is treated as an integer
top_customers['CustomerID'] = top_customers['CustomerID'].astype(int)

plt.figure(figsize=(8,6))
# Added .astype(str) to convert CustomerID to string for plotting
sns.barplot(x=top_customers['CustomerID'].astype(str), y=top_customers['CLV'] / 1e6, data=top_customers)  # CLV in millions
plt.title('Top 10 Customers by CLV', fontsize=16)
plt.xlabel('Customer ID', fontsize=12)
plt.ylabel('Customer Lifetime Value (CLV) in Millions [Currency]', fontsize=12)
plt.xticks(rotation=45)
plt.show()

