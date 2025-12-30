#!/bin/bash
ttyd \
  --port 7681 \
  --writable \
  python3 /opt/as-calc/main.py
