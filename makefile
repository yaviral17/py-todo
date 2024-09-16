run:
	@. venv/bin/activate && uvicorn main:app --reload

postgres:
	@sudo docker run --name some-postgres -e POSTGRES_PASSWORD=test1234 -e POSTGRES_USER=root -e POSTGRES_DB=todo -p 6789:5432 -d postgres

install:
	@pip install -r requirements.txt

docker-up:
	@sudo docker compose up --build

docker-down:
	@sudo docker compose down

.PHONY: run postgres docker-up docker-down