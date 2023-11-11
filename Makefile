run:
	uvicorn main:app --reload

build:
	docker compose -f docker-compose.local.yml build

up:
	docker compose -f docker-compose.local.yml up -d

down:
	docker compose -f docker-compose.local.yml down

shell:
	docker compose -f docker-compose.local.yml exec src python3

install:
	pip install -r requirements.txt

code:
	autopep8 --in-place --recursive ./src
	autoflake --remove-all-unused-imports --remove-duplicate-keys --remove-unused-variables --in-place --recursive ./src
	black ./src
	isort ./src
	flake8 ./src
	pylint ./src

test:
	pytest ./src -vv

test-cov:
	pytest --cov=src ./src