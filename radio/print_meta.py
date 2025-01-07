"""
A short script to print meta data of all .ogg files in the same dir.

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

# built-in libs
import os
import json

# 3rd-party libs
from tinytag import TinyTag


fl = os.listdir('.')

ans = {}
ans_fix = {}
ans_types = {'_Undefined_': 0}

for f in fl:
    if os.path.splitext(f)[1] == '.ogg':

        # load tag
        tag = TinyTag.get(f).as_dict()
        # if tag['type'][0] == 'Public Service Announcements':
        #     print(f"{f}\n\t", '\n\t'.join([f"{tk}: {tag[tk]}" for tk in tag]), '\n', sep='')
        ans[f] = tag

        # process data for ans_fix
        type_ = ans[f]['type'][0] if 'type' in ans[f] else '_Undefined_'
        if type_ not in ans_fix: ans_fix[type_] = {}
        ans_fix[type_][f] = tag.copy()
        for tk, tv in ans_fix[type_][f].items():
            if isinstance(tv, (list, tuple)) and len(tv) == 1:
                ans_fix[type_][f][tk] = tv[0]

        # count types
        if 'type' in ans[f]:
            for k in ans[f]['type']:
                if k not in ans_types: ans_types[k] = 0
                ans_types[k] += 1
        else:
            ans_types[type_] += 1

with open("_meta_.json", 'w') as fp:
    json.dump(ans, fp, indent=4)

with open("_meta_fixed.json", 'w') as fp:
    json.dump(ans_fix, fp, indent=4)

with open("_meta_types.json", 'w') as fp:
    json.dump(ans_types, fp, indent=4)

print(f"\n\nTypes:\n\t", '\n\t'.join([f"{k}: {ans_types[k]}" for k in ans_types]), '\n', sep='')
