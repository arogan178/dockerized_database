# Rest API for DummyAPI.io

- This repository contains scripts to access and manipulate user data from the DummyAPI.io.
- The API data is retrieved and stored in a MySQL database using Python scripts.
- The repository includes a Docker Compose file for containerization and easy deployment.

## Pre-requisites

- Docker
- Python 3.X or higher
- pip

## Requirements

- mysql-connector-python-library
- requests library

---

## Installation

- Clone the repository

```bash
git clone https://github.com/<username>/<repository>.git
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Build the Docker container:

```bash
docker-compose up -d
```

- Log into the MySQL database

```bash
mysql -h 127.0.0.1 -P 3306 -u root -p
```

- Password: pwd

- Execute the `000_CreateDB.sql` script in MySQL Shell to create the database and tables

```mysql-shell
\sql
source (repository_location)/sql_scripts/000_CreateDB.sql
```

---

## Usage

### database.py

- Open `database.py`
- Update the `config` dictionary with the correct values for your MySQL server.

### api_connection.py

- Open `api_connection.py` in text editor
- Update the `app_id` variable with your own app ID. (You can get one from dummyapi.io)
- Run the script using the following command:

```bash
python api_connection.py
```

---

## Note

- The `api_connection.py` and `database.py` scripts assume that the Docker container is running.

- The `api_connection.py` script will fetch data from the dummyapi.io API and insert it into the MySQL database.

- The `database.py` script will retrieve the data from the MySQL database and print it to the console.

- The `config` dictionary in the `database.py` script should be updated with the correct values for your MySQL server.

---

## Support

- Please open an issue for support.

## Contributors

- Pull requests are welcome. Please make sure that your changes are tested before submitting a pull request.

## License

- MIT
