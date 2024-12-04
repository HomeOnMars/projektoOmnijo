#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert owned CSL1 radios as CSL2 Extended radios.

Note: this script does not create music tracks out of the blue.
You will need to buy and download those CSL1 radio stations first.
(Check if this script actually work before you make any big decision. I do NOT promise anything.)
You will also need to subscribe to the Extended Radio mod for CSL2 on Paradox Mods.

I am not a lawyer, and I do not really know enough about copyrights.
Definitely do NOT share the ogg files online.
Probably best NOT to use those musics when streaming.

This python script has only been tested on WSL (Windows Subsystem for Linux) with game installed on Windows system.

Check and modify the "parameters" section near the beginning and the "if __name__ == '__main__':" section near the end before you proceed.

Author: HomeOnMars



-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2024 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""

# built-in libs
import os
from os import sep
import shutil
import json

# parameters - modify below lines to suit your own system

CSL1_PATH: str = '/mnt/d/Games/SteamLibrary/steamapps/common/Cities_Skylines/'
CSL1_RADIO_PATH: str = os.path.normpath(f'{CSL1_PATH}{sep}Files{sep}Radio{sep}')
# CSL1_RADIO_ICON_PATH: str = os.path.normpath(f'{CSL1_PATH}{sep}Cities Skylines - Soundtrack{sep}AlbumArtwork.png')
CSL2_RADIO_PATH: str = "./"    # will need to copy the output from this folder to the below example path
# CSL2_RADIO_PATH Example:
# /mnt/c/Users/{Your-User-Name}/AppData/LocalLow/Colossal Order/Cities Skylines II/ModsData/ExtendedRadio/CustomRadios/


# json format database
# see <https://github.com/AlphaGaming7780/ExtendedRadio/wiki/Custom-Radio>.
RADIO_JSON_NETWORK : dict = {
    "name": "",           #  <--  Update this
    "description": "",    #  <--  Update this
    "icon": "coui://extendedradio/resources/DefaultIcon.svg",
    "allowAds": True,
}

RADIO_JSON_CHANNEL : dict = {
    "name": "",           #  <--  Update this
    "description": "",    #  <--  Update this
    "icon": "coui://extendedradio/resources/DefaultIcon.svg",
}

RADIO_JSON_PROGRAM : dict = {
    "name": "",           #  <--  Update this
    "description": "",    #  <--  Update this
    "icon": "coui://extendedradio/resources/DefaultIcon.svg",
    "startTime": "00:00",
    "endTime": "00:00",
    "loopProgram": True,
    "pairIntroOutro": False,
}

RADIO_JSON_SEGMENT : dict = {
    "type": "Playlist",    #  <--  Update this
    "tags": [],
    "clipsCap": 2,
}

RADIO_JSON_AUDIOFLIE: dict = {
    "Title" : None,    #  <--  Update this
    "Album" : None,    #  <--  Update this
    "Artist": None,    #  <--  Update this
    "Type"  : None,
    "Brand" : None,
    "RadioStation"  : None,
    "RadioChannel"  : None,
    "PSAType"   : None,
    "AlertType" : None,
    "NewsType"  : None,
    "WeatherType": None,
    "loopStart" : -1,
    "loopEnd"   : -1,
    "alternativeStart": -1,
    "fadeoutTime": 1,
}

# helper functions

def mkdir(path: str, dry_run: bool = False, verbose: bool = True):
    if not os.path.exists(path):
        if verbose: print(f"\t$ makedir: {path}")
        if not dry_run: os.makedirs(path)
    return

def cp(
    src: str, dst: str,
    overwrite: None|bool = None,
    # hardlink: if set to True, will create hard link instead of copies, which saves space and are faster.
    # only works if both src and dst are in the same partition of the disk.
    # warning: Changes made to original files will automatically apply to any hard-linked file instantly.
    hardlink: bool = False,
    dry_run: bool = False,
    verbose: bool = True,
):
    if not overwrite and os.path.exists(dst):
        if overwrite is None:
            if not dry_run: raise FileExistsError(f"File '{dst}' already exists.")
            elif verbose: print(f"*** Error: File '{dst}' already exists.")
        else:
            if verbose: print(f"*   Warning: Skipping existing file '{dst}'.")
    elif hardlink:
        if verbose: print(f"\t$ link: '{src}' '{dst}'")
        if not dry_run: os.link(src, dst)
    else:
        if verbose: print(f"\t$ copy: '{src}' '{dst}'")
        if not dry_run: shutil.copy2(src, dst)
    return

def do_write_file(file_path: str, overwrite: None|bool = None, verbose: bool = True) -> bool:
    if os.path.exists(file_path):
        if overwrite is None:
            raise FileExistsError(f"File '{file_path}' already exists.")
        elif not overwrite:
            if verbose: print(f"*   Warning: Skipping existing file '{file_path}'.")
            return False
    return True

def write_json(
    data: dict,
    json_path: str,
    overwrite: None|bool = None,
    dry_run: bool = False,
    verbose: bool = True,
):
    if do_write_file(json_path, overwrite=overwrite, verbose=verbose):
        if verbose: print(f"Adding '{json_path}'...", end='')
        if not dry_run:
            with open(json_path, 'w') as fp:
                json.dump(data, fp, indent=4)
        if verbose: print(f" Done.")
    return



# main function

def convert_csl1_radio(
    old_radio_path : str = CSL1_RADIO_PATH,
    new_radio_path : str = CSL2_RADIO_PATH,
    old_included_types: set[str] = {'Music', 'Blurb', 'Talk'},
    radio_network_path: str = 'CSL1RadioNetwork',
    radio_network_name: str = "Classic Skylines Network",
    radio_network_desc: str = "Cities: Skylines 1 radio stations",
    overwrite_ogg : None|bool = None,    # if None, will raise exception if file already exists
    overwrite_json: None|bool = None,
    hardlink: bool = False,
    dry_run: bool = False,
    verbose: bool = True,
):
    """Convert CSL1 radio stations as CSL2 Extended Radio mod radio stations.
    
    old_included_types: folder type names from old radio files that will be considered.
        Only pre-selected keywords can be used. See code.
    """

    if verbose: print(f"Scanning existing CSL1 radio stations in '{old_radio_path}{sep}'...")

    old_radio_channels: list[str] = [rc for rc in os.listdir(f'{old_radio_path}{sep}Music{sep}')]
    if verbose: print(f"\n\t{'\n\t'.join(old_radio_channels)}\n")
    if verbose: print(f"{len(old_radio_channels)} channels found.\n")


    if verbose: print(f"Creating ExtendedRadio CustomRadios file structures...")

    # create radio network
    new_radio_network_path = os.path.normpath(f'{new_radio_path}{sep}{radio_network_path}')
    mkdir(new_radio_network_path, dry_run=dry_run, verbose=verbose)
    data = RADIO_JSON_NETWORK.copy()
    data["name"] = radio_network_name
    data["description"] = radio_network_desc
    write_json(
        data=data, json_path=f'{new_radio_network_path}{sep}RadioNetwork.json',
        overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
    )
    
    for channel in old_radio_channels:
        channel_name = ''.join(' ' + char if char.isupper() else char.strip() for char in channel).strip()
        if verbose: print(f"For Channel {channel_name} ('{channel}'):")

        # create radio channel
        new_radio_channel_path = os.path.normpath(f'{new_radio_network_path}{sep}{channel}')
        mkdir(new_radio_channel_path, dry_run=dry_run, verbose=verbose)
        data = RADIO_JSON_CHANNEL.copy()
        data["name"] = channel_name
        data["description"] = channel_name
        write_json(
            data=data, json_path=f'{new_radio_channel_path}{sep}RadioChannel.json',
            overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
        )
        
        # create radio program
        new_radio_program_path = os.path.normpath(f'{new_radio_channel_path}{sep}{channel}')
        mkdir(new_radio_program_path, dry_run=dry_run, verbose=verbose)
        data = RADIO_JSON_PROGRAM.copy()
        data["name"] = channel_name
        data["description"] = channel_name
        write_json(
            data=data, json_path=f'{new_radio_program_path}{sep}Program.json',
            overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
        )

        # segment: Playlist
        type_ = 'Music'
        if type_ in old_included_types:
            # write segment json file
            new_radio_seg_meta_path = os.path.normpath(f'{new_radio_program_path}{sep}Playlist{sep}')
            mkdir(new_radio_seg_meta_path, dry_run=dry_run, verbose=verbose)
            data = RADIO_JSON_SEGMENT.copy()
            data["type"] = "Playlist"
            data["clipsCap"] = 2
            write_json(
                data=data, json_path=f'{new_radio_seg_meta_path}{sep}Segment.json',
                overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
            )
            # copy audio files
            old_radio_segment_path = os.path.normpath(f'{old_radio_path}{sep}{type_}{sep}{channel}{sep}')
            new_radio_segment_path = os.path.normpath(f'{new_radio_program_path}{sep}Playlist{sep}{type_}{sep}')
            mkdir(new_radio_segment_path, dry_run=dry_run, verbose=verbose)
            for file_old in [f for f in os.listdir(old_radio_segment_path)]:
                file = file_old.replace(' – ', ' - ')
                file_noext = os.path.splitext(file)[0]
                file_split = file_noext.split(" - ")
                cp(
                    os.path.normpath(f'{old_radio_segment_path}{sep}{file_old}'),
                    os.path.normpath(f'{new_radio_segment_path}{sep}{file}'),
                    overwrite=overwrite_ogg, hardlink=hardlink, dry_run=dry_run, verbose=verbose)
                title, artist = None, None
                if len(file_split) >= 2:
                    title_split = file_split[1].strip().split(' ')
                    # remove leading numbers and extra spaces
                    if title_split and '0' <= title_split[0][0] and title_split[0][0] <= '9': title_split.pop(0)
                    title = ' '.join([t for t in title_split if t])
                    artist = file_split[0].strip()
                elif file_split:
                    title_split = file_split[0].strip().removeprefix("Radio_OfficialMars_").split(' ')
                    # remove leading numbers and extra spaces
                    if title_split and '0' <= title_split[0][0] and title_split[0][0] <= '9': title_split.pop(0)
                    title = ' '.join([t for t in title_split if t])
                    if verbose: print(f"**  Warning: Unable to parse title and album from file name '{file}'")
                else:
                    if verbose: print(f"*** Error: Empty file name '{file}'")

                data = RADIO_JSON_AUDIOFLIE.copy()
                data["Title"] = title
                data["Artist"]= artist
                write_json(
                    data=data, json_path=f'{new_radio_segment_path}{sep}{file_noext}.json',
                    overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
                )

                
        # segment: Talkshow
        types: set = {'Blurb', 'Talk'}.intersection(old_included_types)
        if types:
            # write segment json file
            new_radio_seg_meta_path = os.path.normpath(f'{new_radio_program_path}{sep}Talkshow{sep}')
            mkdir(new_radio_seg_meta_path, dry_run=dry_run, verbose=verbose)
            data = RADIO_JSON_SEGMENT.copy()
            data["type"] = "Talkshow"
            data["clipsCap"] = 1
            write_json(
                data=data, json_path=f'{new_radio_seg_meta_path}{sep}Segment.json',
                overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
            )
        # copy audio files
        for type_ in types:
            old_radio_segment_path = os.path.normpath(f'{old_radio_path}{sep}{type_}{sep}{channel}{sep}')
            new_radio_segment_path = os.path.normpath(f'{new_radio_program_path}{sep}Talkshow{sep}{type_}{sep}')
            mkdir(new_radio_segment_path, dry_run=dry_run, verbose=verbose)
            if os.path.exists(old_radio_segment_path):
                for file_old in [f for f in os.listdir(old_radio_segment_path)]:
                    file = file_old.replace(' –  ', ' - ')
                    file_noext = os.path.splitext(file)[0]
                    cp(
                        os.path.normpath(f'{old_radio_segment_path}{sep}{file_old}'),
                        os.path.normpath(f'{new_radio_segment_path}{sep}{file}'),
                        overwrite=overwrite_ogg, hardlink=hardlink, dry_run=dry_run, verbose=verbose)
                    data = RADIO_JSON_AUDIOFLIE.copy()
                    write_json(
                        data=data, json_path=f'{new_radio_segment_path}{sep}{file_noext}.json',
                        overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
                    )



if __name__ == '__main__':
    print(f"Input parameters:\n\t{CSL1_PATH = }\n\t{CSL1_RADIO_PATH = }\n\t{CSL2_RADIO_PATH = }\n")
    convert_csl1_radio(
        # comment or modify below lines for English names etc.
        radio_network_path = 'CSL1RadioReto',
        radio_network_name = "Klasika Urbosilueto RadioReto",
        radio_network_desc = "CSL1 RadioStacioj",
        overwrite_ogg = False,
        overwrite_json= False,
        hardlink = True,
        dry_run  = False,
        verbose  = True,
    )
