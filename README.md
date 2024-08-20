# Fastapi project template

## Requirements

- Python 3.8+
- PostgreSQL, MySQL or SQLite

## Installation

### Set up virtual environment

```shell
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```shell
pip install -r requirements/common.txt
```

### Install `pre-commit` hooks

- Install `pre-commit`: https://pre-commit.com/
- Install `pre-commit` hooks:

```shell
pre-commit install
```

## Running

Inside the virtual environment

To run in production mode:

```shell
sh run.sh
```

To run in development mode:

```shell
sh run.sh dev
```

To run test:

```shell
sh run.sh test
```
