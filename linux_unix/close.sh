#!/usr/bin/env bash

shell_path=$(
  cd "$(dirname "$0")" || exit
  pwd
)
cd "${shell_path}" || exit

app_folder="${shell_path}/app"
core_cmd="sh ${app_folder}/run.sh"
core_pid=$(ps -ef | grep "${core_cmd}" | grep -v grep | awk '{print $2}')
kill -9 ${core_pid}

pages_cmd="python -m http.server --directory ${app_folder}/dist"
pages_pid=$(ps -ef | grep "${pages_cmd}" | grep -v grep | awk '{print $2}')
kill -9 ${pages_pid}
