import os
from prefect import flow


@flow(log_prints=True)
def some_work():
    not_so_secret_value = "x"  # os.environ.get("wow")
    print(not_so_secret_value)


if __name__ == "__main__":

    flow.from_source(
        source="https://github.com/discdiver/creds-examples.git",
        entrypoint="env-ex.py:some_work",
    ).deploy(
        name="my-dep",
        work_pool_name="dock1",
    )


# if i don't have "yo" as an environmment variable on the work pool, does this fail?
