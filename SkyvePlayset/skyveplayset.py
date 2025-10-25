#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Reformat Skyve exported Playset json file

Code author: HomeOnMars

-------------------------------------------------------------------------------

3-Clause BSD License

Copyright 2025 HomeOnMars

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

-------------------------------------------------------------------------------
"""

import json
import shutil
import os
from datetime import datetime


class SkyvePlayset:
    """Manipulate exported Skyve Playset files."""
    def __init__(
        self,
        name,
        skyve_dir: str,
        temp_dir : str = "./temp.",
        verbose: bool = True,
    ):
        self.name: str = name
        self.data: dict[str, dict] = {}
        self.temp_updated: bool = False

        if verbose: print(f"\n{self.name}\n")
        self.update_temp(skyve_dir, temp_dir=temp_dir, verbose=verbose)
        self.read_temp(temp_dir=temp_dir, verbose=verbose)

    def update_temp(
        self,
        skyve_dir: str,
        temp_dir : str = "./temp.",
        verbose: bool = True,
    ):
        """Update temp file."""
        name = self.name
        target = f"{temp_dir}{name}.json"
        source = ""
        try:
            mtime = int(os.path.getmtime(target))
        except FileNotFoundError:
            mtime = 0
        for f in os.listdir(skyve_dir):
            if f.startswith(name+' '):
                fp = f"{skyve_dir}{f}"    # file path
                new_mtime = int(os.path.getmtime(fp))
                if mtime == 0.0 or new_mtime > mtime:
                    source = fp
                    mtime = new_mtime
        if source:
            shutil.copy2(source, target)
            self.temp_updated = True
            if verbose:
                print(
                    f"-\tCopied '{source}' to '{target}',\n\tmodified at "
                    f"{datetime.fromtimestamp(new_mtime).isoformat()}.")
        else:
            self.temp_updated = False
            if verbose:
                print(
                    f"-\tNote: No updates for the old file '{target}'.")
        return self

    def read_temp(
        self,
        temp_dir: str = "./temp.",
        verbose: bool = True,
    ):
        """Read from temp file."""
        with open(f"{temp_dir}{self.name}.json", 'r') as f:
            self.data = json.load(f)
        return self

    def normalize(
        self,
        remove_banner: bool = True,
        remove_mods: tuple|dict[str, dict] = {},
        verbose: bool = True,
    ):
        """Remove unnecessary info."""
        data = self.data

        if 'SubscribedMods' not in data:
            data['SubscribedMods'] = {}

        if (remove_banner
            and 'GeneralData' in data
            and 'BannerBytes' in data['GeneralData']
        ):
            del data['GeneralData']['BannerBytes']
            if verbose:
                print(f"-\tRemoved banner in {self.name}")
        
        if remove_mods:
            count = 0
            for it in remove_mods:
                d = data['SubscribedMods']
                if it in d:
                    del d[it]
                    count += 1
            if verbose:
                print(
                    f"-\tRemoved {count} packages in {self.name}, "
                    f"{len(data['SubscribedMods'])} packages left.")
        return self

    def dump(self, verbose:bool=True):
        """Write to disk."""
        fp = f"{self.name}.json"
        with open(fp, 'w') as f:
            json.dump(self.data, f, indent=2)
            if verbose:
                print(f"Playset {self.name} dumped to '{fp}'.")
        return self
        


if __name__ == '__main__':

    with open(f"radios.json", 'r') as f:
        mod_ids_radios = json.load(f)['SubscribedMods']
    remove_mods = mod_ids_radios
    skyve_dir = "../CSL2_SavesDir/ModsData/Skyve/Playsets/Shared/"

    for playset_name in {'OmniCentro', 'OmniProvo', 'MapTesting', 'MapCreation'}:
        playset = SkyvePlayset(playset_name, skyve_dir)
        if playset.temp_updated:
            playset.normalize(remove_mods=remove_mods).dump()
