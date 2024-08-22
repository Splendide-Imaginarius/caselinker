#!/usr/bin/env bash

set -euo pipefail
shopt -s nullglob globstar

FOLDER="$1"

for RUBY_FILE in "${FOLDER}"/**/*.rb
do
	ruby ruby_strings.rb "${RUBY_FILE}"
done
