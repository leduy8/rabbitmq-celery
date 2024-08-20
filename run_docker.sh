chmod +x run.sh
chmod +x run_tests.sh
docker network create fastapi-test
docker compose up --build