import os
from prefect_dbt.cloud.jobs import trigger_dbt_cloud_job_run
from prefect import flow

DBT_API_KEY = os.environ.get("DBT_CLOUD_API_KEY")

@flow
def cloud_job(job_id=123456):
    trigger_dbt_cloud_job_run(, job_id=job_id
    )


if __name__ == "__main__":
    cloud_job()
