FROM node:14

WORKDIR /app

COPY package.json .
COPY yarn.lock ./
RUN yarn add @vue/cli-service --dev
RUN yarn install --frozen-lockfile

COPY . .
EXPOSE 8080

CMD ["yarn", "serve"]