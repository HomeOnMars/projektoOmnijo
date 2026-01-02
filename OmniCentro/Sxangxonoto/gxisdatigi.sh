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
cp -v ../../CSL2_SavesDir/AllAboard.coc  ./
cp -v ../../CSL2_SavesDir/NoPollution.coc  ./
cp -v ../../CSL2_SavesDir/Plop\ the\ Growables.coc  ./
cp -v ../../CSL2_SavesDir/RealLife.coc ./
cp -v ../../CSL2_SavesDir/RealPop.coc  ./
cp -v ../../CSL2_SavesDir/RoadVisualTweaks.coc  ./
cp -vr ../../CSL2_SavesDir/ModsSettings/Carto      ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/RealisticWorkplacesAndHouseholds    ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/Time2Work  ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/AdjustTransitCapacity   ModsSettings/
cp -vr ../../CSL2_SavesDir/ModsSettings/OutsideTrafficAdjuster  ModsSettings/

# Reminders
echo; echo
echo "***REMEMBER TO UPDATE THE PLAYSET INFO***"
echo
