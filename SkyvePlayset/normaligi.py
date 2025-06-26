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

def normalize_playset(
    name: str,
    remove_banner: bool = True,
    remove_mods: tuple|dict[str, dict] = {},
    overwrite: bool = False,
) -> dict:
    with open(f"temp.{name}.json", 'r') as f:
        data = json.load(f)
    if (remove_banner
        and "GeneralData" in data
        and "BannerBytes" in data["GeneralData"]
    ):
        del data["GeneralData"]["BannerBytes"]
    if remove_mods:
        for it in remove_mods:
            d = data["SubscribedMods"]
            if it in d:
                del d[it]
    if overwrite:
        with open(f"{name}.json", 'w') as f:
            json.dump(data, f, indent=2)
    return data



if __name__ == '__main__':

    with open(f"radios.json", 'r') as f:
        mod_ids_radios = json.load(f)["SubscribedMods"]

    remove_mods = mod_ids_radios

    #{'OmniCentro', 'MapTesting', 'MapCreation'}:
    for playset_name in {'OmniCentro',}:
        playset = normalize_playset(
            playset_name, remove_mods=remove_mods, overwrite=True,
        )
    