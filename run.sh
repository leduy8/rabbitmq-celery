#!/bin/bash

# Set environment or development by default
ENVIRONMENT=${1:-production}

# Export the environment variable
export ENVIRONMENT

# Run the alembic command
alembic upgrade head

# Run server
if [ "$ENVIRONMENT" == "production" ] || [ "$ENVIRONMENT" == "prod" ]; then
  fastapi run main.py --proxy-headers --port 8008
elif [ "$ENVIRONMENT" == "development" ] || [ "$ENVIRONMENT" == "dev" ]; then
  fastapi dev main.py --proxy-headers --port 8008
elif [ "$ENVIRONMENT" == "test" ]; then
  sh scripts/dev/run_tests.sh
else
  echo "Invalid operation, should be production, development or test"
fi
