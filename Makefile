default: 
	@echo "Comandos disponíveis"
	@echo "make build           - Cria containers caso não os tenha, ou caso modifique .env.dev"
	@echo "make makemigrations  - Cria migrations"
	@echo "make migrate         - Executa migrations"
	@echo "make createsuperuser - Criar um usuario"
	@echo "make start           - Inicializa container, e executa serviço Django"
	@echo "make test            - Fazer teste com o pytest"
	@echo "make shell           - Acessar o shell do container"

make:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

start:
	python manage.py runserver localhost:8000

test:
	pytest . --cov-report term --cov=. --cov-fail-under=80
shell:
	python manage.py shell