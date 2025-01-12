#!/usr/bin/with-contenv bashio
set -e

echo "Hello Victron"

# cd "${0%/*}"
cd /workdir
python3 -u ./app.py #"$@"