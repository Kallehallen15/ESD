#!/usr/bin/bash

source ~/.nvm/nvm.sh

cd esp-web-tool

nvm use 18

npm start &> /dev/null
