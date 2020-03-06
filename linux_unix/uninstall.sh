#!/usr/bin/env bash

shell_path=$(
  cd "$(dirname "$0")" || exit
  pwd
)
echo "\033[32mUninstall DD Monitor from path [${shell_path}/app]\033[0m"

rm -vrf "${shell_path}/app"

echo "\033[32mDone!\033[0m"
