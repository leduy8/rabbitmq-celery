FROM python:3.9-alpine

WORKDIR /www/fastapi-test

COPY requirements/ ./requirements

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY . .

ENTRYPOINT ["/bin/sh", "-c", "sh /www/fastapi-test/run.sh"]
