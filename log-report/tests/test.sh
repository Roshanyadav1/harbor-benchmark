#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier

# pytest is baked into the environment image (environment/Dockerfile).
set +e
pytest /tests/test_outputs.py -rA
status=$?
set -e

if [ "$status" -eq 0 ]; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
