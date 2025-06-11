# 📰 News API ETL Project

This is a beginner-friendly data engineering project that extracts news articles from the News API, transforms the data using Python, loads it into PostgreSQL, and automates the pipeline using Apache Airflow. The final data is visualized using Jupyter Notebook.

---

## 🔧 Tech Stack Used

- **Python**
- **Apache Airflow**
- **PostgreSQL**
- **Jupyter Notebook**
- **News API**
- **Pandas**

---

## 📁 Project Folder Structure

news_api_etl_project/
├── README.md
├── dags/ # Airflow DAGs for ETL workflow
│ └── news_api_etl.py # Main DAG file
├── data/ # Raw and cleaned data files
│ ├── raw_news_data.csv
│ └── cleaned_news_data.csv
├── images/ # Screenshots or graphs
│ └── airflow_dag_graph.png
├── notebooks/ # Jupyter notebooks for visualization
│ └── news-api-graphs.ipynb
├── requirements.txt # Python dependencies
└── scripts/ # Python scripts used in ETL
└── news_api_extract.py

