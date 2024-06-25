#!/bin/bash
set -e

BUILD_DIR=~/build
mkdir -p $1/usr/lib/python3/dist-packages/
cp bin/q.py $1/usr/lib/python3/dist-packages/
cp bin/qif.py $1/usr/lib/python3/dist-packages/
