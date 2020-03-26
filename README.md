# Let's StudEEE

Welcome to the repository for Let's StudEEE.
    
## Installation
### Setting up the dev environment
Create a virtual environment where you will install all modules necessary. A quick way to do this is:
```
virtualenv -p python3 venv
source venv/bin/activate
```

Afterwards, install all required modules:
```
pip install -r requirements.txt
```
### Setting up the database
The database management system used for this project is [PostgreSQL](https://www.postgresql.org/). Install the system either through the installer or through a terminal. Ensure that the postgres server is running afterwards.

Create a database named _letsstudeee_.
```
> createdb letsstudeee
```
Access the database through the _psql_ command.
```
> psql letsstudeee
```

Create a user named _coe134_ with password _coe134_ then grant all privileges on the database to this user.
```
CREATE USER coe134 WITH PASSWORD 'coe134';
GRANT ALL PRIVILEGES ON DATABASE letsstudeee TO coe134;
```

### Environment variables
There is a `.env` file for environment variables such as admin credentials. For security, I did not include it in this repository. Contact me on setting this up.

## Contribution Process
Two ways to contribute:
-   Pull Request
    1.   Fork the repository.
    2.   Create a branch for add your feature.
    3.   Commit the changes you made to that repository.
    4.   Push it to your forked repository.
    5.   Create a pull request in the original repository.
    6.   Have it approved by me.
-   Direct contributor
    -   Request access from me.

## Deployment Process
The latest release is deployed [here](http://lets-studeee.herokuapp.com). All commits and updates will go through here.
I will manually deploy the latest commit afterwards.

## Test Process
We should add several test cases to ensure code quality. However we don't have enough time to do so.