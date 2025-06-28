#!/bin/bash

# Changelogs
echo; echo
pwd -P
echo; echo
cp -v ../Data/.markdownlint.json   ./
cp -v ../Data/Changelog.md         Sxangxonoto.md
cp -v ../Data/Changelog_tags.md    Sxangxonoto_bib.md
cp -v ../Data/Changelog_public.md  Sxangxonoto_pub.md

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
cp -v ../../CSL2_SavesDir/RealLife.coc ./
cp -vr ../../CSL2_SavesDir/ModsSettings/Time2Work ModsSettings/

# Reminders
echo; echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO***"
echo
