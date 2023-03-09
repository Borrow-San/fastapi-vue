FROM node:latest

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json .
COPY yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

EXPOSE 8080

CMD ["yarn", "serve"]