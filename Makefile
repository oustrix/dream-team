build-back:
	docker build -t backend ./backend

build-front:
	cd ./frontend && \
	npm run build && \
	docker build -t frontend .

clean:
	docker system prune -a

make up:
	docker compose up