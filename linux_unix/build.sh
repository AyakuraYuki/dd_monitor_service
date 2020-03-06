#!/usr/bin/env bash

shell_path=$(
  cd "$(dirname "$0")" || exit
  pwd
)
echo -e "\033[32mDD Monitor will be installed in path [${shell_path}/app]\033[0m"

start=$(date +%s)

echo -e "\033[32mStep 1. Download core and prepare for core running environment.\033[0m"
cd "${shell_path}" || exit
git clone https://github.com/AyakuraYuki/dd_monitor.git 'backend'
backend_folder="${shell_path}/backend"
cd "${backend_folder}" || exit
git checkout backend
pip install -r requirements.txt
end1=$(date +%s)
echo -e "\033[34m([$((end1 - start))s] Step 1. Done)\033[0m"

echo -e "\033[32mStep 2. Download ui and build the pages.\033[0m"
cd "${shell_path}" || exit
git clone https://github.com/AyakuraYuki/dd_monitor.git 'ui'
frontend_folder="${shell_path}/ui"
cd "${frontend_folder}" || exit
git checkout ui
npm install
cd "${frontend_folder}" || exit
npm run build
cd "${shell_path}" || exit
end2=$(date +%s)
echo -e "\033[34m([$((end2 - end1))s] Step 2. Done)\033[0m"

echo -e "\033[32mStep 3. Assemble core and pages together.\033[0m"
cp -vrf "${frontend_folder}/dist" "${backend_folder}/"
rm -rf "${frontend_folder}"
rm -rf "${backend_folder}/.git"
mv "${backend_folder}" "${shell_path}/app"
end3=$(date +%s)
echo -e "\033[34m([$((end3 - end2))s] Step 3. Done)\033[0m"

echo -e "\033[32m[$((end3 - start))s] Done!\033[0m"
