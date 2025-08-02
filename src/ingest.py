import pandas as pd
from sqlalchemy import create_engine
import os

def download_wdi_data():
    url = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"
    os.makedirs("data", exist_ok=True)
    df = pd.read_csv(url)
    df.to_csv("data/wdi_sample.csv", index=False)

def load_to_postgres():
    engine = create_engine(os.getenv("DATABASE_URL"))
    df = pd.read_csv("data/wdi_sample.csv")
    df.to_sql("wdi_data", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    download_wdi_data()
    load_to_postgres()