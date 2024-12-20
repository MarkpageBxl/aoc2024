#!/usr/bin/env python
#
# Solution for Advent of Code 2015
# Day 6, part 1
#
# Challenge URL: https://adventofcode.com/2015/day/6
#
# Author: Markus Lindström <markus@markpage.be>
#

import re
from typing import TextIO
from collections.abc import Iterable

PATTERN = re.compile(
    r"^(turn off|turn on|toggle) ([0-9]+),([0-9]+) through ([0-9]+),([0-9]+)$"
)


# command generator
def commands(fp: TextIO) -> Iterable[tuple[str, int, int, int, int]]:
    for line in fp:
        match = PATTERN.match(line)
        assert match
        command, r1, c1, r2, c2 = match.groups()
        r1, c1, r2, c2 = [int(x) for x in (r1, c1, r2, c2)]
        yield command, r1, c1, r2, c2


def turn_off(x: int) -> int:
    return 0


def turn_on(x: int) -> int:
    return 1


def toggle(x: int) -> int:
    return 1 if x == 0 else 0


def count_lights(lights: list[list[int]]):
    count = 0
    for sublist in lights:
        count += sublist.count(1)
    return count


# init matrix
lights = []
for i in range(1000):
    lights.append([0] * 1000)

with open("input") as fp:
    for command, r1, c1, r2, c2 in commands(fp):
        if command == "turn off":
            func = turn_off
        elif command == "turn on":
            func = turn_on
        elif command == "toggle":
            func = toggle
        start = (r1, c1)
        end = (r2, c2)
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                lights[row][col] = func(lights[row][col])

print(count_lights(lights))
