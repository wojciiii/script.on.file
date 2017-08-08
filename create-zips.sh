#!/bin/bash

#rm -f kodi-rcs.zip
#zip -r kodi-rcs.zip kodi-rcs/*

#rm -f script.kodi-rcs.zip
#zip -r script.kodi-rcs.zip script.kodi-rcs/*

rm -f script.on.file.zip
zip -r script.on.file.zip script.on.file/*

rm -f context.on.file.zip
zip -r context.on.file.zip context.on.file/*

rm -f repository.kodi.wojci.home-1.0.0.zip

cd repository-install/repository.kodi.wojci.home-1.0.0
zip -r ../../repository.kodi.wojci.home-1.0.0.zip *
