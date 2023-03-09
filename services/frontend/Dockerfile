FROM node:latest

WORKDIR /app

COPY package.json .
COPY yarn.lock ./
RUN yarn install --frozen-lockfile
RUN yarn add @vue/cli-service --dev

COPY . .

EXPOSE 8080

CMD ["yarn", "serve"]