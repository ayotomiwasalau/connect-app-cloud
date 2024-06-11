FROM node:current-alpine3.19 as build-stage

WORKDIR .

COPY package.json ./
COPY package-lock.json ./

RUN npm install -g npm@latest

RUN npm install
RUN npm install react-scripts@3.4.3 -g

COPY . ./

EXPOSE 3000

RUN export NODE_OPTIONS=--openssl-legacy-provider

RUN npm run build


# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.15


COPY --from=build-stage ./build/ /usr/share/nginx/html






