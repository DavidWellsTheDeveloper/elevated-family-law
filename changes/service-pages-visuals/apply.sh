#!/usr/bin/env bash
# Re-apply the visual versions (new/<id>.html) to the site.
set -e
cd "$(dirname "$0")"
KEY="$(cd ../.. && pwd)/LightsailDefaultKey-us-west-2.pem"
HOST=admin@32.185.210.182
IDS=${@:-110 117 122 128 132 174 175 176 177 178}
for id in $IDS; do
  scp -q -i "$KEY" new/$id.html $HOST:/tmp/apply_$id.html
  ssh -i "$KEY" $HOST "wp post update $id /tmp/apply_$id.html" 2>&1 | grep -v 'Git Updater'
done
