====================
SETUP STEP
====================

0/ go to the script folder
$ cd 01_data_injection

1/ create visual environment named 'ENV' (only 1st time)
$ python -m venv ENV

2/ activate the visual environment
$ source ENV/bin/activate

3/ install required libraries (only 1st time)
$ pip install -r requirements.txt

4/ start Postgres and Adminer services (need running docker engine)
$ docker-compose up

5/ connect postgres : http://localhost:8080/
     - System: PostgreSQL
     - Server: postgres
     - Username: postgres
     - Password: postgres
     - Database: postgres

==================================================

====================
RUNNING STEP
====================

0/ go to the script folder
$ cd 01_data_injection

1/ create tables
$ python create_tables.py

2/ insert data into table 'DelistedCompanies'
$ python etl_DelistedCompanies.py

3/ insert data into table 'DividendsHistorical'
$ python etl_DividendsHistorical.py #Param#

*** #Param# : pass the interested dividend ***
$ python etl_DividendsHistorical.py AAPL

==================================================

====================
SHUTDOWN STEP
====================
9/ stop Postgres and Adminer services
$ docker-compose down

10/ deactivate the visual environment
$ deactivate

==================================================
