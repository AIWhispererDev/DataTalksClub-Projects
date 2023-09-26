test:
	pipenv run pytest tests/

quality_checks:
	pipenv run isort .
	pipenv run black .
	pipenv run pylint --recursive=y .

scrape: quality_checks
	python -m src.scrape_and_clean

titles:
	python -m src.generate_and_save_titles

deploy:
	python -m src.check_and_save_deployment

streamlit:
	python -m streamlit run ./app.py

all: scrape titles deploy
