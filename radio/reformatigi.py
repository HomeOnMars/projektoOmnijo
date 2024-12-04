#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sort music files in the local folder, and convert m4a files to ogg files.

WORK IN PROGESS.

Require ffmpeg and libvorbis (install with apt - as I only tested this on Ubuntu)

Only tested on WSL (Windows Subsystem for Linux).
Most likely will NOT work in Windows directly.

Warning: if the song file name ended with a number, the script may not treat it correctly.
Rename it like: from '42.ogg' to '01_42.ogg' as a fix.


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
import subprocess
import json

# 3rd party libs
from tinytag import TinyTag


# json format database
# see <https://github.com/AlphaGaming7780/ExtendedRadio/wiki/Custom-Radio>.
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

def mv(
    src: str, dst: str,
    # if None: will raise exceptions if dst already exists
    overwrite: None|bool = None,
    dry_run: bool = False,
    verbose: bool = True,
):
    if not overwrite and os.path.exists(dst):
        if overwrite is None:
            if not dry_run: raise FileExistsError(f"File '{dst}' already exists.")
            elif verbose: print(f"*** Error: File '{dst}' already exists.")
        else:
            if verbose: print(f"*   Warning: Skipping moving '{src}' to existing file '{dst}'.")
    else:
        if verbose: print(f"\t$ move: '{src}' '{dst}'")
        if not dry_run: shutil.move(src, dst)
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

def name_func_default(no: int, old_filename: str) -> str:
    """Default function for generating new names from old ones"""

    # new_fn = f"{no:03}_{'_'.join(old_filename.split('_')[1:])}".translate(None, ' \'\\/:*?"<>|')
    new_fn = old_filename
    fns: list = new_fn.split('_')
    if fns[0] and fns[0][-1] in set('0123456789'):    # first word: my no of the file
        fns = fns[1:]
    new_fn = '_'.join(fns)

    fns: list = new_fn.split(' ')
    if fns[0] and fns[0][-1] in set('0123456789'):    # first word: album no of the file
        fns = fns[1:]
    # titlize and remove labels
    fns = [
        fn.title() for fn in fns
        if fn.title() not in {
            '(Acoustic)',
            '[Acoustic]',
        }
    ]
    # remove '(feat. xxx)' info
    new_fns = []
    par_lvl : int = 0    # par means parenthesis
    for fn in fns:
        if fn.startswith('(Feat'):
            par_lvl += 1
        if not par_lvl:
            new_fns.append(fn)
        if par_lvl and fn.endswith(')'):
            par_lvl -= 1
    new_fn = ''.join(new_fns)    # throw away spaces
    
    # normalize - throw away any char unsupported by windows file explorer
    new_fn = f"{no:03}_{new_fn}".translate({c: None for c in ' \'\\/:*?"<>|'})
    return new_fn



# main function

def normalize_csl2_music_files(
    name_func = lambda no, old_filename: f"{old_filename}", #f"",
    tbc_ext_set: set[str] = {'.m4a'},    # tbc = to be converted; ext = file name extension
    overwrite_move: None|bool = None,    # if None, will raise exception if file already exists
    overwrite_ogg : None|bool = None,    # if None, will raise exception if file already exists
    overwrite_json: None|bool = None,
    do_sort_fname : bool = True,
    do_convert_ogg: bool = True,
    do_add_json   : bool = True,    # only works if do_convert_ogg is also True - for now
    dry_run: bool = False,
    verbose: bool = True,
):
    """Convert CSL1 radio stations as CSL2 Extended Radio mod radio stations.
    
    name_func: function taking the number and old filename (no extension), and return the filename (without extension)
        e.g.,
            lambda no, old_filename: f"{old_filename}"
                will keep the old filename;
            lambda no, old_filename: f"{no:03}_{'_'.join(old_filename.split('_')[1:])}"
                will re-order filenames such as 042_1234asdf to sth like 001_1234asdf.
    """

    # init
    all_ext_set = tbc_ext_set.copy(); all_ext_set.add('.ogg')
    filenames_raw_list: list[str] = os.listdir('.')
    filenames_dict: dict[str: set[str]] = {}
    for filename in filenames_raw_list:
        fn, ext = os.path.splitext(filename)
        if fn not in filenames_dict:
            filenames_dict[fn] = {ext}
        else:
            filenames_dict[fn].add(ext)


    # sort file names
    if do_sort_fname:
        filenames_old_list : list = [
            fn for fn, exts in filenames_dict.items()
            if all_ext_set.intersection(exts)    # select music files only
        ]
        filenames_old_list.sort(key = lambda txt: txt.split('_')[0])
        for i, fn in enumerate(filenames_old_list):
            new_fn = name_func(i, fn)
            filenames_dict[new_fn] = filenames_dict.pop(fn)
            for ext in filenames_dict[new_fn]:
                mv(
                    f'{fn}{ext}', f'{new_fn}{ext}',
                    overwrite=overwrite_move, dry_run=dry_run, verbose=verbose)

    

    # convert to ogg and add json files
    if do_convert_ogg:
        for fn, exts in filenames_dict.items():
            tbc_ext_list = list(tbc_ext_set.intersection(exts))
            if tbc_ext_list and (overwrite_ogg or '.ogg' not in exts):
                tbc_ext = tbc_ext_list[0]
                # convert to ogg
                cmds: list[str] = [
                    'ffmpeg',
                    '-i',
                    f'{fn}{tbc_ext}',
                    '-acodec', 'libvorbis',
                    '-ar', '48000',
                    '-vn',
                    f'{fn}.ogg',
                ]
                if verbose: print(f"\t$ {' '.join(cmds)}")
                if not dry_run:
                    subprocess.run(cmds)
                    exts.add('.ogg')

                # add json
                if do_add_json:
                    if overwrite_json or '.json' not in exts:
                        tag: TinyTag = TinyTag.get(f'{fn}{tbc_ext}')
                        data = RADIO_JSON_AUDIOFLIE.copy()
                        data["Title"] = tag.title
                        data["Album"] = tag.album
                        data["Artist"]= tag.artist
                        write_json(
                            data=data, json_path=f'{fn}.json',
                            overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
                        )
                    exts.add('.json')

    return filenames_dict

if __name__ == '__main__':
    normalize_csl2_music_files(
        name_func = lambda no, old_filename: f"M{name_func_default(no, old_filename)}",
        overwrite_ogg = False,
        overwrite_json= False,
        dry_run  = False,
        verbose  = True,
    )
"".translate()