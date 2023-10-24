FROM node:lts

WORKDIR /app

COPY ./build .

RUN npm install -g serve

CMD serve -s . -l tcp://0.0.0.0:3000