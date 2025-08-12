FROM nginx:1.29.0-alpine3.22

COPY ./index.html /usr/share/nginx/html/index.html
