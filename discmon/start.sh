#!/bin/bash
cd "${0%/*}"
cd "bot"
yarn start &
cd "../emulator"
python ./emulator && fg
