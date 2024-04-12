## Goal

Run DBT jobs that are observed with Prefect and keep credential in your environemnt (don't a Prefect Cloud Credentials Block).
Generalizes to other integrations.

Could use Docker, K8s, ECS, or whatever infrastructure type you like, just make sure your environment variable is injected.

## Steps

1. Install prefect-dbt
1. Register prefect-dbt module blocks
1. Get API key from DBT Cloud
1. Create work pool
1. Create flow code
1. Create deployment code (specify work pool)
1. Could use a SecretVolume
