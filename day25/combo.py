#!/usr/bin/python3

import sys
import re
import math
import functools
import copy

def transform(number, loop_size):
    result = 1
    for _ in range(0, loop_size):
        result = result * number
        result = result % 20201227
    return result

def get_loop_size(public_key):
    result = 1
    loop_size = 0

    while result != public_key:
        loop_size += 1
        result = result * 7
        result = result % 20201227

    return loop_size


card_public = 11562782
door_public = 18108497

# Figure out the loop size for the card

door_loop_size = get_loop_size(door_public)
print(f'door loop size: {door_loop_size}')

card_loop_size = get_loop_size(card_public)
print(f'card loop size: {card_loop_size}')

door_private_key = transform(door_public, card_loop_size)
print(f'private key (door_public): {door_private_key}')

card_private_key = transform(card_public, door_loop_size)
print(f'private key (card_public): {card_private_key}')



