import pandas as pd
import os
import time
import logging
from sqlalchemy import create_engine


# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------
logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


# --------------------------------------------------
# Database Connection
# --------------------------------------------------
engine = create_engine("sqlite:///inventory.db")


# --------------------------------------------------
# Control Switch
# --------------------------------------------------
# Set to True only when you want to reload CSVs
RUN_INGESTION = False


# --------------------------------------------------
# Function: Ingest Data into Database
# --------------------------------------------------
def ingest_db(df, table_name, engine):
    """
    Load a pandas DataFrame into a database table.
    """

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False,
        chunksize=10000
    )


# --------------------------------------------------
# Function: Load CSV Files and Ingest into Database
# --------------------------------------------------
def load_raw_data():
    """
    Read all CSV files from the data folder
    and load them into the SQLite database.
    """

    start_time = time.time()

    for file in os.listdir("data"):

        if file.endswith(".csv"):

            logging.info(f"Started ingestion for file: {file}")

            df = pd.read_csv(f"data/{file}")

            table_name = file[:-4]

            ingest_db(df, table_name, engine)

            logging.info(
                f"Successfully ingested table: {table_name}"
            )

    end_time = time.time()

    total_time = round((end_time - start_time) / 60, 2)

    logging.info("Data ingestion completed successfully")
    logging.info(
        f"Total execution time: {total_time} minutes"
    )


# --------------------------------------------------
# Main Program
# --------------------------------------------------
if __name__ == "__main__":

    if RUN_INGESTION:
        load_raw_data()
    else:
        print("Data already loaded. Skipping ingestion.")