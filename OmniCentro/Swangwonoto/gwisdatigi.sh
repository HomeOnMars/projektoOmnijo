#!/bin/bash

# Changelogs
echo; echo
pwd -P
echo; echo
cp -v ../Data/.markdownlint.json   ./
cp -v ../Data/Changelog.md         Swangwonoto.md
cp -v ../Data/Changelog_tags.md    Swangwonoto_bib.md
cp -v ../Data/Changelog_public.md  Swangwonoto_pub.md

# Playsets
echo; echo
cd ../../SkyvePlayset/
pwd -P
echo
python3 skyveplayset.py

# ModsSettings
echo; echo
cd OmniCentro_ModsSettings/
pwd -P
echo; echo
cp -v ../../CSL2_SavesDir/Plop\ the\ Growables.coc  ./
cp -v ../../CSL2_SavesDir/RealLife.coc ./
cp -v ../../CSL2_SavesDir/RealPop.coc  ./
cp -vr ../../CSL2_SavesDir/ModsSettings/Carto      ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/RealisticWorkplacesAndHouseholds    ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/Time2Work  ModsSettings/

# Reminders
echo; echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO***"
echo
