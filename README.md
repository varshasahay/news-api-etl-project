# 📰 News API ETL Project (Docker + Airflow)

This is a beginner-friendly **Data Engineering Project** that builds a complete ETL pipeline using **News API**, **Apache Airflow**, and **PostgreSQL**, all inside **Docker**.  
The pipeline extracts latest news articles, transforms and cleans the data, loads it into a PostgreSQL database, and visualizes it using Jupyter Notebook.

---

## 🚀 Tech Stack Used

- 🐍 Python  
- 🛠️ Apache Airflow  
- 🐘 PostgreSQL  
- 🐳 Docker & Docker Compose  
- 📊 Jupyter Notebook  
- 🌐 News API  
- 📦 Pandas, Requests, SQLAlchemy

---

## 📁 Folder Structure

news_api_etl_project/
│
├── dags/ # Airflow DAGs
│ └── news_api_etl.py
│
├── scripts/ # ETL Python scripts
│ └── news_api_extract.py
│
├── data/ # Raw and cleaned data files
│ ├── raw_news_data.csv
│ └── cleaned_news_data.csv
│
├── notebooks/ # Jupyter notebooks for visualization
│ └── news-api-graphs.ipynb
│
├── images/ # Graphs or DAG screenshots
│ └── airflow_dag_graph.png
│
├── requirements.txt # Python dependencies
├── docker-compose.yml # Docker services
└── dockerfile # Dockerfile for Airflow image


---


---

## 🚀 How to Run the Project (Using Docker)

> 📦 **Prerequisites:**
> - Docker & Docker Compose installed

### 🔹 Step 1: Clone the Repository
```bash
git clone https://github.com/varshasahay/news_api_etl_project.git
cd news_api_etl_project
docker-compose up --build

