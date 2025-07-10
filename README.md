# ApachePipeline
### ETL pipeline using Apache Airflow

I have created a pipeline to extract exchange rate data every day and add it a csv file that tracks prices over time. It's also uploaded to a postgres database that can be queried using DBeaver. 

## Pre-reqs
Python, Astronomer, DBeaver, Docker Desktop, Airflow
$ winget install -e –id Astronomer.Astro

Set up instructions
1. Create a new Python project
2. Open up your Python/GitBash terminal
3. $ astro dev init (This sets up almost all the folders you need)
4. Add txt files and docker files (extra files)
5. Add code and install required libraries
6. Open Docker and type into terminal
7. astro dev start
8. Set up connections
9. Trigger
10. Enjoy your data

To use it you simply need to open Docker Desktop, run the DAG. This will have it run every day in the background but it can also be triggered manually.

# Contribution Guidelines
This pipeline takes currency exchange rates from the current date and compare them to the pound (£), transforms only a small handfull of them into a csv file that is downloaded and uploaded to a postgres database. This can be edited to compare any currency by edited the currency variable at the start of the code. This could be edited to include far more currencies as well. This can also be sent to other database management systems such as AWS. It could also be edited to check against the previous line of data and update you should there be a rise or drop in an exchange. Below are different urls to call different versions of the API. These can be edited in the same way I have done for checking GDP to view different json files.  
https://api.frankfurter.dev/v1/latest - This shows the lastest exchange rates compared to Euros  
https://api.frankfurter.dev/v1/latest?base=GBP - Compared to GBP  
https://api.frankfurter.dev/v1/latest?symbols=CHF,GBP - Comparing Euros to specific currencies  
https://api.frankfurter.dev/v1/1999-01-04 - Euros from a specific date  
https://api.frankfurter.dev/v1/1999-01-04?base=USD&symbols=EUR - 2 currencies from a specific date  
https://api.frankfurter.dev/v1/2000-01-01..2000-12-31 - Comparing between 2 dates  
https://api.frankfurter.dev/v1/2024-01-01.. - From 1 date to current  
https://api.frankfurter.dev/v1/2024-01-01..?symbols=USD - Single exchange rate over time  
https://api.frankfurter.dev/v1/currencies - Names of currencies and abbreviations  
