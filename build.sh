#!/bin/sh
# ./ui/
cd ./ui/ || return
npm install
npm run build
# ./
cd ../ || return
# ./app/templates/
cd ./app/templates/ || return
rm -rf ./*
# ./
cd ../../ || return
# ./app/static/
cd ./app/static/ || return
rm -rf ./*
# ./
cd ../../ || return
cp -R ./ui/dist/ ./app/templates/
