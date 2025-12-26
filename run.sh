#!/bin/bash
ttyd \
  --port 7681 \
  --writable \
  --once \
  python3 /opt/as-calc/main.py
