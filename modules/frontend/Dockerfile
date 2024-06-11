FROM node:current-alpine3.19

WORKDIR .

COPY package.json ./
COPY package-lock.json ./

RUN npm install
RUN npm install react-scripts@3.4.3 -g

COPY . ./

EXPOSE 3000

RUN export NODE_OPTIONS=--openssl-legacy-provider

CMD ["npm", "start"]

