.PHONY: test compose-up compose-down compose-config

test:
	cd app && python3 -m pytest

compose-up:
	docker compose up --build

compose-down:
	docker compose down

compose-config:
	docker compose config

