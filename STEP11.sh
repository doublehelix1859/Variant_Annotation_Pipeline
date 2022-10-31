#!/bin/bash

source ./STEP0.sh
cd $DIR
mkdir STEP11_out

ml python/3.8.2
#automatically export variables
set -a
. ./STEP0.sh
exec python ./STEP11.py
