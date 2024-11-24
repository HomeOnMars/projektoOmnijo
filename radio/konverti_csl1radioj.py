#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Convert owned CSL1 radios as CSL2 Extended radios.

Note: this script does not create music tracks out of the blue. You will need to buy and download those CSL1 radio stations first.

Only tested on WSL (Windows Subsystem for Linux) with game installed on Windows system.

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

import os
from os import sep
import shutil


# parameters - modify below lines to suit your own system

CSL1_PATH: str = '/mnt/d/Games/SteamLibrary/steamapps/common/Cities_Skylines/'
CSL1_RADIO_PATH: str = os.path.normpath(f'{CSL1_PATH}{sep}Files{sep}Radio{sep}')
CSL2_RADIO_PATH: str = "./"    # will need to copy the output from this folder to the below example path
# CSL2_RADIO_PATH Example:
# /mnt/c/Users/{Your-User-Name}/AppData/LocalLow/Colossal Order/Cities Skylines II/ModsData/ExtendedRadio/CustomRadios/


# helper functions

def mkdir(path: str, dry_run: bool = False, verbose: bool = True):
    if not os.path.exists(path):
        if verbose: print(f"$ makedir: {path}")
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
        if verbose: print(f"$ link: '{src}' '{dst}'")
        if not dry_run: os.link(src, dst)
    else:
        if verbose: print(f"$ copy: '{src}' '{dst}'")
        if not dry_run: shutil.copy2(src, dst)
    return

# main function

def convert_csl1_radio(
    old_radio_path : str = CSL1_RADIO_PATH,
    new_radio_path : str = CSL2_RADIO_PATH,
    old_included_types: set[str] = {'Music', 'Blurb', 'Talk'},
    radio_network_path: str = 'CSL1RadioNetwork',
    radio_network_name: str = "Classic Skylines Network",
    overwrite: None|bool = None,
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

    new_radio_network_path = os.path.normpath(f'{new_radio_path}{sep}{radio_network_path}')
    mkdir(new_radio_network_path, dry_run=dry_run, verbose=verbose)
    
    for channel in old_radio_channels:
        if verbose: print(f"For Channel '{channel}':")

        new_radio_channel_path = os.path.normpath(f'{new_radio_network_path}{sep}{channel}')
        mkdir(new_radio_channel_path, dry_run=dry_run, verbose=verbose)

        # create radio program
        new_radio_program_path = os.path.normpath(f'{new_radio_channel_path}{sep}{channel}')
        mkdir(new_radio_program_path, dry_run=dry_run, verbose=verbose)

        # segment: Playlist
        if 'Music' in old_included_types:
            old_radio_segment_path = os.path.normpath(f'{old_radio_path}{sep}Music{sep}{channel}{sep}')
            new_radio_segment_path = os.path.normpath(f'{new_radio_program_path}{sep}Playlist{sep}')
            mkdir(new_radio_segment_path, dry_run=dry_run, verbose=verbose)
            for file in [f for f in os.listdir(old_radio_segment_path)]:
                cp(
                    os.path.normpath(f'{old_radio_segment_path}{sep}{file}'),
                    os.path.normpath(f'{new_radio_segment_path}{sep}{file}'),
                    overwrite=overwrite, hardlink=hardlink, dry_run=dry_run, verbose=verbose)
                
        # segment: Talkshow
        types: set = {'Blurb', 'Talk'}.intersection(old_included_types)
        if types:
            new_radio_segment_path = os.path.normpath(f'{new_radio_program_path}{sep}Talkshow{sep}')
            mkdir(new_radio_segment_path, dry_run=dry_run, verbose=verbose)
        for type_ in types:
            old_radio_segment_path = os.path.normpath(f'{old_radio_path}{sep}{type_}{sep}{channel}{sep}')
            if os.path.exists(old_radio_segment_path):
                for file in [f for f in os.listdir(old_radio_segment_path)]:
                    cp(
                        os.path.normpath(f'{old_radio_segment_path}{sep}{file}'),
                        os.path.normpath(f'{new_radio_segment_path}{sep}{file}'),
                        overwrite=overwrite, hardlink=hardlink, dry_run=dry_run, verbose=verbose)



if __name__ == '__main__':
    print(f"Input parameters:\n\t{CSL1_PATH = }\n\t{CSL1_RADIO_PATH = }\n\t{CSL2_RADIO_PATH = }\n")
    convert_csl1_radio(
        # comment or modify below lines for English names etc.
        radio_network_path = 'CSL1RadioReto',
        radio_network_name = "Klasika Urbosilueto RadioReto",
        overwrite= False,
        hardlink = True,
        dry_run  = False,
        verbose  = True,
    )
