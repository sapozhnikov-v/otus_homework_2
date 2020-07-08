#!/bin/bash
set -e
if [ "$ENV" = 'DEV' ]; then
  exec python "lotto.py"

elif [ "$ENV" = 'TEST' ]; then
  exec pytest -v
fi