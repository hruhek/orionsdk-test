# OrionSDK test example

## Setup

Clone this repo.
```shell
git clone git@github.com:hruhek/orionsdk-test.git
```

Create `.env` file with in root of this project.
```shell
cd orionsdk-test
touch .env
```

Put the following contents in `.env`.
```dotenv
ORION_SERVER=123.456.789.001
ORION_USER=username
ORION_PASSWORD=s3cr3t!
```

Set environment variables to match you host, user and password. File pattern is already in `.env` is in `.gitignore`.

## Dependencies

This code supports both PY2 and PY3. Here is PY3 example.

```shell
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

## Run query example

```shell
python solarwinds.py
```

## Run tests
```shell
pytest
```