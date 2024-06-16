ARG NODE_VERSION=lts-alpine
ARG CLIENT__PORT=3000

FROM node:$NODE_VERSION

ENV TZ=Asia/Kamchatka

WORKDIR /app

COPY ./entrypoint.sh .

RUN apk update && \
apk add --no-cache tzdata && \
npm i pm2 -g && \
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
echo $TZ > /etc/timezone

EXPOSE $CLIENT__PORT

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
