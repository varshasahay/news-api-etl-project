from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
from airflow.providers.postgres.hooks.postgres import PostgresHook
from urllib.parse import urlparse

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 17),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='news_api_etl_dag',
    default_args=default_args,
    description='ETL pipeline using news_100_articles.csv',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    def extract_data():
        df = pd.read_csv("/mnt/c/Users/91626/Downloads/news_100_articles.csv")
        df.to_csv("/home/ubuntu_user/airflow/dags/data/raw_news_data.csv", index=False)

    def transform_data():
        df = pd.read_csv("/home/ubuntu_user/airflow/dags/data/raw_news_data.csv")

        df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
        df['published_date'] = df['publishedAt'].dt.date
        df['published_time'] = df['publishedAt'].dt.time
        df['published_hour'] = df['publishedAt'].dt.hour
        df['author'] = df['author'].str.extract(r'([A-Za-z\s]+)', expand=False)
        df.dropna(subset=['title', 'description', 'url'], inplace=True)
        df['domain'] = df['url'].apply(lambda x: urlparse(x).netloc)
        df['title_length'] = df['title'].apply(lambda x: len(str(x)))
        df['description_length'] = df['description'].apply(lambda x: len(str(x)))
        df['day_of_week'] = df['publishedAt'].dt.day_name()

        df.to_csv("/home/ubuntu_user/airflow/dags/data/cleaned_news_data.csv", index=False)

    def load_data():
        pg_hook = PostgresHook(postgres_conn_id='postgres_default')
        conn = pg_hook.get_conn()
        cursor = conn.cursor()
        df = pd.read_csv("/home/ubuntu_user/airflow/dags/data/cleaned_news_data.csv")

        for _, row in df.iterrows():
            cursor.execute(
                """
                INSERT INTO cleaned_news_data_api (
                  source, author, title, description, url, publishedAt,
                  published_date, published_time, published_hour,
                  domain, title_length, description_length, day_of_week
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    row.get("source"),
                    row.get("author"),
                    row.get("title"),
                    row.get("description"),
                    row.get("url"),
                    row.get("publishedAt"),
                    row.get("published_date"),
                    row.get("published_time"),
                    row.get("published_hour"),
                    row.get("domain"),
                    row.get("title_length"),
                    row.get("description_length"),
                    row.get("day_of_week"),
                )
            )
        conn.commit()
        cursor.close()
        conn.close()

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    # Task order
    extract_task >> transform_task >> load_task

