# ApachePipeline
ETL pipeline using Apache Airflow

I have created a pipeline to extract exchange rate data every day and add it a csv file that tracks prices over time. It's also uploaded to a postgres database that can be queried using DBeaver. 

Pre-reqs
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
