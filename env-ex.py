import os
from prefect import flow


@flow(log_prints=True)
def some_work():
    not_so_secret_value = os.environ.get("yo")
    print(not_so_secret_value)


some_work.from_source(source="", entrypoint="").deploy(
    name="my-dep",
    work_pool_name="p1",
    job_variables={"VAR1": {os.environ.get("yo")}},
)