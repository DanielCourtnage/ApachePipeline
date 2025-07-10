# ApachePipeline
### ETL pipeline using Apache Airflow

I have created a pipeline to extract exchange rate data every day and add it a CSV file that tracks prices over time. It's also uploaded to a Postgres database that can be queried using DBeaver. 

## Pre-reqs
To use this pipeline you need to have the following programmes installed and set up on your device:
- Python
- Astronomer
- DBeaver
- Docker Desktop
- Airflow
<br/>
Below are some command line prompts to install Airflow and Astronomer:

- $ pip install "apache-airflow[celery]==3.0.2"
- $ winget install -e –-id Astronomer.Astro

Set up instructions
1. Create a new Python project
2. Open up your Python/GitBash terminal and type the command below
3. $ astro dev init (This sets up almost all the folders you need)
4. Add or edit the .yaml and .txt files to match the ones posted in the repo
5. Create a new .py file in your dags folder and paste the Python code
6. Open Docker Desktop
7. Type into your Python terminal the prompt below
8. astro dev start
9. Set up connections using the guide above
10. Trigger the dag
11. Enjoy your data
<br/>
From here the data will be downloaded into a CSV file on your computer into the dags folder. If there is already a CSV file in place it will update it with a new line so you can compare rates over time. It also establishes a connection to a Postgres database, accessible by DBeaver or other platforms.  

To use it you simply need to open Docker Desktop and run the DAG. This will have it run every day in the background but it can also be triggered manually.

# Contribution Guidelines
This pipeline takes currency exchange rates from the current date and compares them to the pound (£), transforms only a small handful of them into a CSV file that is downloaded to your local machine and uploaded to a Postgres database. This can be edited to compare any currency by edited the currency variable at the start of the code. This could be edited to include far more currencies as well. This can also be sent to other database management systems such as AWS. It could also be edited to check against the previous line of data and update you should there be a rise or drop in an exchange. Below are different urls to call different versions of the API. These can be edited in the same way I have done for checking GDP to view different json files.  
<br/>
https://api.frankfurter.dev/v1/latest - This shows the latest exchange rates compared to Euros  
https://api.frankfurter.dev/v1/latest?base=GBP - Compared to GBP  
https://api.frankfurter.dev/v1/latest?symbols=CHF,GBP - Comparing Euros to specific currencies  
https://api.frankfurter.dev/v1/1999-01-04 - Euros from a specific date  
https://api.frankfurter.dev/v1/1999-01-04?base=USD&symbols=EUR - 2 currencies from a specific date  
https://api.frankfurter.dev/v1/2000-01-01..2000-12-31 - Comparing between 2 dates  
https://api.frankfurter.dev/v1/2024-01-01.. - From 1 date to current  
https://api.frankfurter.dev/v1/2024-01-01..?symbols=USD - Single exchange rate over time  
https://api.frankfurter.dev/v1/currencies - Names of currencies and abbreviations  
