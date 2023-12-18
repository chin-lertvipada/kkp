### SETUP STEP


#### 1/ go to the script folder
```sh
$ cd 01_data_injection
```

#### 2/ create visual environment named 'ENV' (only 1st time)
```sh
$ python -m venv ENV
```

#### 3/ activate the visual environment
```sh
$ source ENV/bin/activate
```

#### 4/ install required libraries (only 1st time)
```sh
$ pip install -r requirements.txt
```

#### 5/ start Postgres and Adminer services (need running docker engine)
```sh
$ docker-compose up
```

#### 6/ connect postgres : http://localhost:8080/
```sh
     - System: PostgreSQL
     - Server: postgres
     - Username: postgres
     - Password: postgres
     - Database: postgres
```

==================================================

### RUNNING STEP

#### 1/ go to the script folder
```sh
$ cd 01_data_injection
```

#### 2/ create tables
```sh
$ python create_tables.py
```

#### 3/ insert data into table 'DelistedCompanies'
```sh
$ python etl_DelistedCompanies.py
```

#### 4/ insert data into table 'DividendsHistorical'
```sh
$ python etl_DividendsHistorical.py #Param#
```

*** #Param# : pass the interested dividend ***
```sh
$ python etl_DividendsHistorical.py AAPL
```

==================================================

### SHUTDOWN STEP

#### 1/ stop Postgres and Adminer services
```sh
$ docker-compose down
```

#### 2/ deactivate the visual environment
```sh
$ deactivate
```

==================================================
