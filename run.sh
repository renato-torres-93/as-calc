#!/bin/bash
ttyd \
  --port 7681 \
  --readonly \
  --client-option disableReconnect=true \
  --client-option disableLeaveTerminal=true \
  python3 /opt/as-calc/main.py
