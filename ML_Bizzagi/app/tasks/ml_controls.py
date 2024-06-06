import celery_config

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

@celery.task()
def process_csv(file_content):
    df = pd.read_csv(file_content)
    print(df.head())
    return df.head().to_dict()