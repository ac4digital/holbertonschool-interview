#!/usr/bin/python3

"""Method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    else:
        return False
