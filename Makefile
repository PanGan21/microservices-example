rabbit:
	docker-compose up --build rabbitmq

admin:
	docker-compose up --build admin_db admin_queue admin

main:
	docker-compose up --build main_db main_queue main

.PHONY: admin rabbit main