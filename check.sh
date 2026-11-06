#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"

test -f README.md

fail=0

echo "== tests (unittest)"
python3 -m unittest discover -s . -t . > /tmp/cilab-out.txt 2>&1 || fail=1
tail -4 /tmp/cilab-out.txt >&2
rm -f /tmp/cilab-out.txt

if [ "$fail" -eq 0 ]; then
  echo "checks passed"
fi
exit "$fail"
