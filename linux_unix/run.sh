#!/usr/bin/env bash

shell_path=$(
  cd "$(dirname "$0")" || exit
  pwd
)
cd "${shell_path}" || exit

app_folder="${shell_path}/app"
cd "${app_folder}" || exit
# Start core
(sh "${app_folder}/run.sh" &)
# Start pages server
(python -m http.server --directory "${app_folder}/dist" &)
