#!/bin/sh
if ! [ -d ./node_modules ]
then
npm i
fi

if ! [ -d ./.output ]
then
npm run build
fi

pm2-runtime start ecosystem.config.cjs
