run:
	@uvicorn main:app --reload

postgres:
	@sudo docker run --name some-postgres -e POSTGRES_PASSWORD=test1234 -e POSTGRES_USER=root -e POSTGRES_DB=todo -p 6789:5432 -d postgres

docker-up:
	@docker-compose up --build

docker-down:
	@docker-compose down

.PHONY: run postgres docker-up docker-down