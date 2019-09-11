#!/bin/sh
# ./ui/
echo 'NPM is working...'
cd ./ui/ || return
npm install
npm run build
# ./
cd ../ || return
# ./app/templates/
cd ./app/templates/ || return
echo 'Cleaning old templates...'
rm -vrf ./*
# ./
cd ../../ || return
# ./app/static/
cd ./app/static/ || return
echo 'Cleaning old static resources...'
rm -vrf ./*
# ./
cd ../../ || return
echo 'Deploying new ui resources...'
cp -vR ./ui/dist/ ./app/templates/
mv -v ./app/templates/static/* ./app/static/
mv -v ./app/templates/img/icons/ ./app/static/img/
rm -vrf ./app/templates/img/
rm -vrf ./app/templates/static/
cp -v ./app/templates/favicon.ico ./app/static/
cp -v ./app/templates/service-worker.js ./app/static/
cp -v ./app/templates/manifest.json ./app/static/
cp -v ./app/templates/robots.txt ./app/static/
find ./app -name "precache*" -exec cp -v {} ./app/static/ \;
echo 'Done!'
