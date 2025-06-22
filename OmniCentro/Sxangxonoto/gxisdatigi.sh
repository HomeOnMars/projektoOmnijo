#!/bin/bash

# Changelogs
pwd -P
cp -v ../Data/.markdownlint.json   ./
cp -v ../Data/Changelog.md         Sxangxonoto.md
cp -v ../Data/Changelog_tags.md    Sxangxonoto_bib.md
cp -v ../Data/Changelog_public.md  Sxangxonoto_pub.md

# ModsSettings
cd ../../SkyvePlayset/OmniCentro_ModsSettings/
pwd -P
cp -v ../../CSL2_SavesDir/RealLife.coc ./
cp -vr ../../CSL2_SavesDir/ModsSettings/Time2Work ModsSettings/

# Reminders
echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO TOO***"
echo