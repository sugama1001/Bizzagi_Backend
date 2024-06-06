import celery_config
import pandas as pd
import celery

@celery.task()
def process_csv(file_content):
    df = pd.read_csv(file_content)
    print(df.head())
    return df.head().to_dict()