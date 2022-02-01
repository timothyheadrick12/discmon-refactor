#!/bin/bash
cd "${0%/*}"
cd "bot"
yarn start &
cd "../emulator"
pipenv run python ../emulator && fg
