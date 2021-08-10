FROM node:14.15.1-alpine as build-stage
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm config set registry https://registry.npm.taobao.org
RUN npm install
COPY . .
RUN npm run build
# production stage
FROM nginx:1.19.5-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY --from=build-stage /app/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build-stage /app/static/docs /usr/share/nginx/html/docs
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
