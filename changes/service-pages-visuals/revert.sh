#!/usr/bin/env bash
# Restore original service page content (before visual changes).
# Usage: ./revert.sh            -> revert all 10 pages
#        ./revert.sh 110 174    -> revert only the listed page IDs
# Also: WordPress keeps revisions (Page editor -> Revisions) as a second undo path.
set -e
cd "$(dirname "$0")"
KEY="$(cd ../.. && pwd)/LightsailDefaultKey-us-west-2.pem"
HOST=admin@32.185.210.182
IDS=${@:-110 117 122 128 132 174 175 176 177 178}
for id in $IDS; do
  scp -q -i "$KEY" backup-original/$id.html $HOST:/tmp/revert_$id.html
  ssh -i "$KEY" $HOST "wp post update $id /tmp/revert_$id.html" 2>&1 | grep -v 'Git Updater'
done
echo "Done. CSS block 'SERVICE PAGE VISUALS' in elevated-family-law-child/style.css is now unused; remove it too if undoing fully."
