build-back:
	docker build -t backend ./backend

build-front:
	docker build -t frontend ./frontend

clean:
	docker system prune -a

make up:
	docker compose up