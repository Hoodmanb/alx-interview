#!/usr/bin/python3
"""method that finds the keys to open other lockboxes
"""


def canUnlockAll(boxes):
    """
    Function that determines if you can open all the lockboxes
    """
    unlocked_boxes = [0]
    for box_id, box in enumerate(boxes):
        if not box:
            continue
        for key in box:
            if key < len(boxes) and key not in unlocked_boxes \
               and key != box_id:
                unlocked_boxes.append(key)

    if len(unlocked_boxes) == len(boxes):
        return True
    return False
