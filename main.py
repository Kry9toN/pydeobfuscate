# This code is licensed under the GNU General Public License (GPL) version 3
# Copyright (C) 2023 Dhimas Bagus Prayoga (Kry9toN)
# SPDX-License-Identifier: GPL-3.0
# For details, please refer to the LICENSE file.

import base64
import time
import re

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def use_regex(input_text):
    return re.findall(r"\(b'(.*?)'\)", input_text, re.DOTALL)

def decode(string):
    count = 0
    while 'exec' in string:
        hasil = base64.b64decode(use_regex(string)[0][::-1]).decode('utf-8')
        count += 1
        time.sleep(1)
        print(f'Layer {count} decrypted successfully')
        string = hasil
    return string

if __name__ == '__main__':
    filename = input('Input file name: ')
    file_data = read_file(filename)
    result = decode(file_data)
    with open(f'decode_{filename}', 'w') as f:
        f.write(result)
    print(f'Done! Output saved as "decode_{filename}"')
