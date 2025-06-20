#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sort music files in the local folder, and convert m4a files to ogg files.

Require ffmpeg and libvorbis (install with apt - as I only tested this on Ubuntu)

Only tested on WSL (Windows Subsystem for Linux).
Most likely will NOT work in Windows directly.

Warning: if the song file name ended with a number, the script may not treat it correctly.
Rename it like: from '42.ogg' to '01__42.ogg' as a fix.
(2 '_' are needed as the code by default throw away the first 2 numbers)
You can customize the naming format by altering the name_func in the "if __name__ == '__main__':" section.


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

# 3rd-party libs
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


# tinytag image type to file extension
TINYTAG_TYPE_2_EXT: dict[str] = {
    'image/jpeg': '.jpg',
    'image/png' : '.png',
}



# helper functions

def upper_first_only(txt: str) -> str:
    for i, c in enumerate(txt):
        if c.isalpha():
            return txt[:i+1].upper() + txt[i+1:]
    return txt

def mv(
    src: str, dst: str,
    # if None: will raise exceptions if dst already exists
    overwrite: None|bool = None,
    dry_run: bool = False,
    verbose: bool = True,
):
    if os.path.normpath(src) == os.path.normpath(dst):
        return
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

def cp(
    src: str, dst: str,
    # if None: will raise exceptions if dst already exists
    overwrite: None|bool = None,
    dry_run: bool = False,
    verbose: bool = True,
):
    if os.path.normpath(src) == os.path.normpath(dst):
        return
    if not overwrite and os.path.exists(dst):
        if overwrite is None:
            if not dry_run: raise FileExistsError(f"File '{dst}' already exists.")
            elif verbose: print(f"*** Error: File '{dst}' already exists.")
        else:
            if verbose: print(f"*   Warning: Skipping moving '{src}' to existing file '{dst}'.")
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

def name_func_default(no: int, old_filename: str) -> str:
    """Default function for generating new names from old ones"""

    # new_fn = f"{no:03}_{'_'.join(old_filename.split('_')[1:])}".translate(None, ' \'\\/:*?"<>|')
    new_fn = old_filename
    fns: list = new_fn.split(' ')
    fn0s: list = fns[0].split('_')
    if fn0s[0] and set('0123456789').intersection(set(fn0s[0])):    # throw away first word?: my no of the file
        fn0s = fn0s[1:]
    if fn0s: fns[0] = '_'.join(fn0s)
    else: fns.pop(0)
    
    fn0s: list = fns[0].split('_')
    if fn0s[0] and fn0s[0].isnumeric():    # throw away first word?: album no of the file
        fn0s = fn0s[1:]
    if fn0s: fns[0] = '_'.join(fn0s)
    else: fns.pop(0)
    # titlize and remove labels
    fns = [
        # throw away \' too
        upper_first_only(fn.translate({ord(c): None for c in '\''}))
        for fn in fns
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
    new_fn = f"{no:03}_{new_fn}".translate({ord(c): None for c in '\\/:*?"<>|'})
    # remove '+' in filename that is causing problems ('InvalidOperationException: HTTP/1.1 404 Not Found') with the game
    new_fn = new_fn.translate({ord('+'): '-'})
    return new_fn



# main function

def normalize_csl2_music_files(
    name_func = lambda no, old_filename: f"{old_filename}", #f"",
    # tbc = to be converted; ext = file name extension
    # Note: '._ogg' and '.oga' is a special case, where the file will be simply renamed as '.ogg'
    tbc_ext_set: set[str] = {'._ogg', '.oga', '.m4a', '.mp3', '.mp4', '.flac'},
    overwrite_move: None|bool = None,    # if None, will raise exception if file already exists
    overwrite_ogg : None|bool = None,    # if None, will raise exception if file already exists
    overwrite_json: None|bool = None,
    overwrite_image: bool = True,
    do_sort_fname : bool = True,
    do_convert_ogg: bool = True,
    do_add_json   : bool = True,    # only works if do_convert_ogg is also True - for now
    do_save_cover : bool = False,   # save cover art image
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

    

    # convert to ogg, add json files, and save cover art.
    for fn, exts in filenames_dict.items():
        # make sure convertible file actually exist
        try: tbc_ext = list(tbc_ext_set.intersection(exts))[0]
        except IndexError:
            if '.ogg' not in exts:
                continue
            else:
                cp(
                    f'{fn}.ogg', f'{fn}.oga',
                    overwrite=overwrite_ogg, dry_run=dry_run, verbose=verbose)
                tbc_ext = '.oga'

        if do_convert_ogg and (overwrite_ogg or '.ogg' not in exts):
            if tbc_ext == '._ogg':
                # Force re-format as ogg
                #     to overwrite anything funny in the metadata
                cmds: list[str] = [
                    'ffmpeg',
                    '-y',                      # overwrite
                    '-i', f'{fn}{tbc_ext}',    # input
                    # '-acodec', 'copy',
                    '-acodec', 'libvorbis',    # format: ogg (audio only)
                    '-ar', '48000',            # audio sampling frequency
                    '-fflags', '+igndts',      # regen DTS to fix the warnings
                        # (see <https://stackoverflow.com/questions/55914754/how-to-fix-non-monotonous-dts-in-output-stream-01-when-using-ffmpeg>)
                        # doesn't seem to work actually
                    '-loglevel', 'error',       # tell ffmpeg to stop bothering with the warnings about above
                    '-vn',
                    f'{fn}.ogg',
                ]
                if verbose: print(f"\t$ {' '.join(cmds)}")
                if not dry_run:
                    subprocess.run(cmds)
                    exts.add('.ogg')
            elif tbc_ext == '.oga':
                # copy paste
                cp(
                    f'{fn}{tbc_ext}', f'{fn}.ogg',
                    overwrite=overwrite_ogg, dry_run=dry_run, verbose=verbose)
                if not dry_run:
                    exts.add('.ogg')
            elif tbc_ext != '.ogg':
                # convert to ogg
                cmds: list[str] = [
                    'ffmpeg',
                    '-y',                      # overwrite
                    '-i', f'{fn}{tbc_ext}',    # input
                    '-acodec', 'libvorbis',    # format: ogg (audio only)
                    '-ar', '48000',            # audio sampling frequency
                    '-vn',
                    f'{fn}.ogg',
                ]
                if verbose: print(f"\t$ {' '.join(cmds)}")
                if not dry_run:
                    subprocess.run(cmds)
                    exts.add('.ogg')

        if do_add_json or do_save_cover:
            tag: None|TinyTag = None
            try:
                tag = TinyTag.get(f'{fn}{tbc_ext}', image=do_save_cover)
            except Exception:
                try:
                    tag = TinyTag.get(f'{fn}{tbc_ext}', image=False)
                except Exception as e:
                    if verbose: print(f"*** Error: {fn}:\n\t{e}")

            if do_add_json and tag is not None:
                if overwrite_json or '.json' not in exts:
                    data = RADIO_JSON_AUDIOFLIE.copy()
                    data["Title"] = tag.title
                    data["Album"] = tag.album
                    data["Artist"]= tag.artist
                    write_json(
                        data=data, json_path=f'{fn}.json',
                        overwrite=overwrite_json, dry_run=dry_run, verbose=verbose,
                    )
                exts.add('.json')

            if do_save_cover and tag is not None:
                image = tag.images.any
                if image is not None:
                    try:
                        image_ext = TINYTAG_TYPE_2_EXT[image.mime_type]
                    except KeyError:
                        if verbose: print(f"**  Warning: Unknown image type in file '{fn}{tbc_ext}'.")
                    else:
                        try:
                            if verbose: print(f"\t$ save '{fn}{image_ext}'")
                            if not dry_run:
                                with open(f'{fn}{image_ext}', 'wb' if overwrite_image else 'xb') as f:
                                    f.write(image.data)
                        except FileExistsError:
                            if verbose: print(f"*   Note: file '{fn}{image_ext}' already exists. Skipping this.")


    return filenames_dict

if __name__ == '__main__':
    normalize_csl2_music_files(
        name_func = lambda no, old_filename: f"M{name_func_default(no, old_filename)}",
        overwrite_move  = None,
        overwrite_ogg   = False,
        overwrite_json  = False,
        overwrite_image = False,
        do_sort_fname  = True,
        do_convert_ogg = True,
        do_add_json    = True,
        do_save_cover  = True,
        dry_run  = False,
        verbose  = True,
    )
