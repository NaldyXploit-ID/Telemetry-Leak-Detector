#!/usr/bin/env bash
# simple scanner stub: perform HEAD requests for a list of hosts
set -eu
hosts=("https://example.com" "https://example.org")
for h in "${hosts[@]}"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "$h" || echo "000")
  printf "%s -> %s\n" "$h" "$code"
done
exit 0
