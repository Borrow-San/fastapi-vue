FROM node:latest

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
ENV LC_ALL=C.UTF-8
ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 -g
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
    apt-get update && \
    apt-get install -y yarn

COPY package.json .
COPY package-lock.json .

CMD ["yarn", "vue-cli-service", "serve"]