\# 🧾 Vendor Performance Analysis – Retail Inventory \& Sales



> Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, and Power BI.



\---



\## 📌 Table of Contents



\- \[Overview](#overview)

\- \[Business Problem](#business-problem)

\- \[Dataset](#dataset)

\- \[Tools \& Technologies](#tools--technologies)

\- \[Project Structure](#project-structure)

\- \[Data Cleaning \& Preparation](#data-cleaning--preparation)

\- \[Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)

\- \[Research Questions \& Key Findings](#research-questions--key-findings)

\- \[Dashboard](#dashboard)

\- \[How to Run This Project](#how-to-run-this-project)

\- \[Final Recommendations](#final-recommendations)

\- \[Author \& Contact](#author--contact)



\---



\## 📖 Overview



This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using \*\*SQL\*\* for ETL, \*\*Python\*\* for analysis and hypothesis testing, and \*\*Power BI\*\* for visualization.



\---



\## ❗ Business Problem



Effective inventory and sales management are critical in the retail sector. This project aims to:



\- Identify underperforming brands needing pricing or promotional adjustments

\- Determine vendor contributions to sales and profits

\- Analyze the cost-benefit of bulk purchasing

\- Investigate inventory turnover inefficiencies

\- Statistically validate differences in vendor profitability



\---



\## 🗂️ Dataset



\- Multiple CSV files located in `/data/` folder (sales, vendors, inventory)

\- Summary table created from ingested data and used for analysis



\---



\## 🛠️ Tools \& Technologies



| Tool | Usage |

|------|-------|

| SQL | CTEs, Joins, Filtering, ETL |

| Python | Pandas, Matplotlib, Seaborn, SciPy |

| Power BI | Interactive Visualizations \& Dashboard |

| GitHub | Version Control |



\---



\## 📁 Project Structure



```

vendor-performance-analysis/

│

├── README.md

├── .gitignore

├── requirements.txt

├── Vendor Performance Report.pdf

│

├── notebooks/                  # Jupyter notebooks

│   ├── exploratory\_data\_analysis.ipynb

│   └── vendor\_performance\_analysis.ipynb

│

├── scripts/                    # Python scripts for ingestion and processing

│   ├── ingestion\_db.py

│   └── get\_vendor\_summary.py

│

├── dashboard/                  # Power BI dashboard file

│   └── vendor\_performance\_dashboard.pbix

```



\---



\## 🧹 Data Cleaning \& Preparation



\- Removed transactions with:

&#x20; - Gross Profit ≤ 0

&#x20; - Profit Margin ≤ 0

&#x20; - Sales Quantity = 0

\- Created summary tables with vendor-level metrics

\- Converted data types, handled outliers, merged lookup tables



\---



\## 🔍 Exploratory Data Analysis (EDA)



\*\*Negative or Zero Values Detected:\*\*

\- Gross Profit: Min -52,002.78 (loss-making sales)

\- Profit Margin: Min -∞ (sales at zero or below cost)

\- Unsold Inventory: Indicating slow-moving stock



\*\*Outliers Identified:\*\*

\- High Freight Costs (up to 257K)

\- Large Purchase/Actual Prices



\*\*Correlation Analysis:\*\*

\- Weak between Purchase Price \& Profit

\- Strong between Purchase Qty \& Sales Qty (0.999)

\- Negative between Profit Margin \& Sales Price (-0.179)



\---



\## 📊 Research Questions \& Key Findings



| # | Question | Finding |

|---|----------|---------|

| 1 | Brands for Promotions | 198 brands with low sales but high profit margins |

| 2 | Top Vendors | Top 10 vendors = 65.69% of purchases → risk of over-reliance |

| 3 | Bulk Purchasing Impact | 72% cost savings per unit in large orders |

| 4 | Inventory Turnover | $2.71M worth of unsold inventory |

| 5 | Vendor Profitability | High Vendors: 31.17% margin vs Low Vendors: 41.55% margin |

| 6 | Hypothesis Testing | Statistically significant difference in profit margins → distinct vendor strategies |



\---



\## 📊 Dashboard



Power BI Dashboard shows:

\- Vendor-wise Sales and Margins

\- Inventory Turnover

\- Bulk Purchase Savings

\- Performance Heatmaps



!\[Vendor Performance Dashboard](images/dashboard.png)



\---



\## ▶️ How to Run This Project



\*\*1. Clone the repository:\*\*

```bash

git clone https://github.com/Sahajahanur/vendor-performance-analysis.git

```



\*\*2. Load the CSVs and ingest into database:\*\*

```bash

python scripts/ingestion\_db.py

```



\*\*3. Create vendor summary table:\*\*

```bash

python scripts/get\_vendor\_summary.py

```



\*\*4. Open and run notebooks:\*\*

```

notebooks/exploratory\_data\_analysis.ipynb

notebooks/vendor\_performance\_analysis.ipynb

```



\*\*5. Open Power BI Dashboard:\*\*

```

dashboard/vendor\_performance\_dashboard.pbix

```



\---



\## ✅ Final Recommendations



\- Diversify vendor base to reduce over-reliance risk

\- Optimize bulk order strategies for maximum cost savings

\- Reprice slow-moving, high-margin brands for better sales velocity

\- Clear unsold inventory strategically to free up $2.71M

\- Improve marketing support for underperforming vendors



\---



\## 👤 Author \& Contact



\*\*Sahajahanur Rahman\*\*

\*Data Analyst\*



📧 Email: \[connectingsrl@gmail.com](mailto:connectingsrl@gmail.com)

🔗 LinkedIn: https://www.linkedin.com/in/sahajahanur-laskar/

🐙 GitHub: \[github.com/Sahajahanur](https://github.com/Sahajahanur)

