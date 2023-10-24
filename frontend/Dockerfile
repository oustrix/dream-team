FROM node:lts

WORKDIR /app


COPY package*.json .

RUN npm ci

COPY ./public ./public/
COPY ./src ./src/

CMD ["npm", "start"]