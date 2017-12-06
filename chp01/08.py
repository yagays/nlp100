#!/usr/bin/env python
# -*- coding: utf-8 -*-


letter_dict = dict(zip([chr(i) for i in range(97, 123)], range(97, 123)))


def cipher(s):
    output = ""
    for i in s:
        if i in letter_dict.keys():
            output += chr(219 - letter_dict[i])
        else:
            output += i
    return output


print(cipher("paraparaparadise"))
print(cipher(cipher("paraparaparadise")))

print(cipher("paragraph"))
print(cipher(cipher("paragraph")))
