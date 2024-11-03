#!/usr/bin/python3
"UTF-8 Validation"


from typing import List


def validUTF8(data: List[int]) -> bool:
    "check if bytes are valid as a UTF-8 string"
    i = 0
    while i < len(data):
        byte = data[i]
        mask = 1 << 7
        if byte < 128:
            i += 1
            continue
        nbytes = 0
        while byte & mask:
            nbytes += 1
            mask >>= 1
        if 4 < nbytes or nbytes < 2 or i+nbytes > len(data):
            return False
        for j in range(i+1, i+nbytes):
            if data[j] & 0xC0 == mask:
                return False
        i += nbytes
    return True
