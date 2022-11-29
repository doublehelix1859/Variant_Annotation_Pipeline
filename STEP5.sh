#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP5_out


ml python/3.8.2

set -a
. ./STEP0.sh
exec python ./STEP5.py
