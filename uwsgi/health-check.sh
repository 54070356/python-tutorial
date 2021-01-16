#!/bin/bash

curl -f http://127.0.0.1:${PORT}/actuator/health || exit 1