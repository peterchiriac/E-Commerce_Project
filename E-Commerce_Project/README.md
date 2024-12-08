## Online Retail Customer Segmentation and Insights Right

Explore customer behavior and unlock actionable insights from transactional data.

Table of Contents  
	1.	Introduction  
	2.	Dataset  
	3.	Project Objectives  
	4.	Key Features  
	5.	Technologies Used  
	6.	Project Workflow  
	7.	Key Insights and Recommendations  
	8.	Future Enhancements   
	9.	Installation  
	10.	Contact  

 ---

 1. Introduction

This project aims to analyze transactional data to understand customer behavior, segment customers into actionable categories, and derive recommendations for targeted marketing strategies. By exploring purchase patterns, we can uncover opportunities to enhance customer retention, drive revenue, and optimize resource allocation.

---

2. Dataset

This project uses the Online Retail Dataset from the UCI Machine Learning Repository. It contains transactional data for a UK-based non-store online retailer.  
	•	Data Summary:  
	•	Time Period: 01/12/2010 to 09/12/2011  
	•	Transactions: 541,909  
	•	Features: 6 (includes quantities, prices, and customer IDs)  
	•	Subject Area: Business  
	•	Associated Tasks: Classification, Clustering  
	•	Data Characteristics: Multivariate, Sequential, Time-Series  
	•	Source: UCI Online Retail Dataset  

---

3. Project Objectives
	1.	Customer Segmentation: Identify low, medium, and high-spending customers.
	2.	Customer Behavior Analysis: Investigate recency, frequency, and monetary patterns.
	3.	Feature Engineering: Create actionable features like Customer Lifetime Value (CLV).
	4.	Insights & Recommendations: Provide data-driven strategies for customer engagement.

---

 4. Key Features
	1.	Data Cleaning:
	•	Handled missing values by removing incomplete records.
	•	Eliminated duplicates to ensure accuracy.
	•	Verified and retained valid outliers representing product returns and luxury items.
	2.	Feature Engineering:
	•	Extracted time-based features like purchase hour, day, and month.
	•	Computed total sales per customer.
	•	Created segmentation based on spending behavior: Low, Medium, and High.
	3.	Customer Insights:
	•	Analyzed customer recency, frequency, and lifetime value (CLV).
	•	Correlated total sales with recency and frequency to identify trends.
	4.	Data Visualization:
	•	Visualized customer segmentation distribution.
	•	Highlighted top customers by lifetime value using bar charts.
	•	Correlation heatmaps for key variables (e.g., sales and frequency).

---

5. Technologies Used

| **Technology**  | **Purpose**                           |
|------------------|---------------------------------------|
| Python           | Core programming language            |
| Pandas           | Data manipulation and preprocessing  |
| NumPy            | Numerical computations               |
| Matplotlib       | Data visualization                   |
| Seaborn          | Advanced data visualization          |
| Excel            | Data import and inspection           |

---

6. Project Workflow
	1.	Data Collection and Integration:
	•	Loaded the dataset from the UCI repository.
	•	Inspected and summarized data to identify key issues like missing values.
	2.	Data Cleaning and Transformation:
	•	Removed missing and duplicate entries.
	•	Engineered features like TotalSales, Recency, and Frequency.
	3.	Customer Segmentation:
	•	Categorized customers into Low, Medium, and High spenders based on their total purchases.
	•	Used thresholds of £500 and £1000 for segmentation.
	4.	Statistical Analysis:
	•	Computed correlations between TotalSales, Recency, and Frequency.
	•	Highlighted insights into spending behavior and purchase patterns.
	5.	Data Visualization:
	•	Plotted customer segment distribution, CLV, and correlations for actionable insights.
	6.	Recommendations:
	•	Developed marketing strategies for customer retention and revenue growth.

---

7. Key Insights and Recommendations

Key Insights:
	•	High-Spending Customers:
	•	Contribute disproportionately to total sales.
	•	Tend to buy frequently, justifying loyalty programs.
	•	Low-Spending Customers:
	•	Represent the majority but require targeted marketing to boost spending.
	•	Correlation Insights:
	•	Frequency has a moderate positive correlation with total sales.

Recommendations:
	1.	Introduce a tiered loyalty program (e.g., Bronze, Silver, Gold) to reward high-spending customers.
	2.	Engage low-spending customers with discounts and cross-sell opportunities.
	3.	Use RFM segmentation for personalized marketing campaigns.

 ---

 8. Future Enhancements
	2.	Expand visualization capabilities for interactive dashboards.
	3.	Implement predictive analytics for churn and sales forecasting.

---

 9. Installation
     
 1. Clone this repository:  
git clone https://github.com/peterchiriac/online-retail-customer-insights.git    
cd online-retail-customer-insights  
 2.	Install required libraries:  
 pip install -r requirements.txt  
 3.	Run the analysis script to generate insights.

---

 4.	10. Contact

For inquiries or suggestions, feel free to reach out:
	•	Email: peter.chiriac@outlook.com
	•	LinkedIn: Petre Chiriac
