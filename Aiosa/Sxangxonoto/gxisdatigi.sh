#!/bin/bash

# Changelogs
echo; echo
pwd -P
echo; echo
cp -v ../Data/.markdownlint.json   ./
cp -v ../Data/Changelog.md         Sxangxonoto.md
cp -v ../Data/Changelog_tags.md    Sxangxonoto_bib.md
cp -v ../Data/Changelog.md         Sxangxonoto_pub.md

# Playsets
echo; echo
cd ../../SkyvePlayset/
pwd -P
echo
python3 skyveplayset.py

# Reminders
echo; echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO***"
echo
