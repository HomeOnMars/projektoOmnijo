#!/bin/bash

# Changelogs
echo
pwd -P
echo
cp -v ../Data/.markdownlint.json   ./
cp -v ../Data/Changelog.md         Sxangxonoto.md
cp -v ../Data/Changelog_tags.md    Sxangxonoto_bib.md
cp -v ../Data/Changelog_public.md  Sxangxonoto_pub.md

# Playsets
echo
cd ../../SkyvePlayset/
pwd -P
echo
mv -vu ../CSL2_SavesDir/ModsData/Skyve/Playsets/Shared/OmniCentro*.json ./temp.OmniCentro.json

# ModsSettings
echo
cd OmniCentro_ModsSettings/
pwd -P
echo
cp -v ../../CSL2_SavesDir/RealLife.coc ./
cp -vr ../../CSL2_SavesDir/ModsSettings/Time2Work ModsSettings/

# Reminders
echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO***"
echo
