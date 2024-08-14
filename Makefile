# Build the Docker containers
build:
	docker-compose build

# Start the Docker containers
up:
	docker-compose up -d

# Stop the Docker containers
down:
	docker-compose down

# Run tests inside the Django container
test:
	docker-compose run backend bash -c "PYTHONPATH=/app pytest -vv"

lint:  ## Run all the linters
	docker-compose run backend poetry run ruff format /app
	docker-compose run backend poetry run mypy /app
