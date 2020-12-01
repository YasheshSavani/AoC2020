#! /usr/bin/env python3
import time
start = time.perf_counter()
with open("example_input.txt", "r") as f:
	example_input = [int(x.strip()) for x in f]


with open("puzzle_input.txt", "r") as f:
	puzzle_input = [int(x.strip()) for x in f]


target_prod=2020
debug = 1


def part1(target, inp):
	for x in inp:
		if (target-x in inp):
			return (x, target-x)

def part2(target, inp):
	for x in inp:
		for y in inp:
			if (target-x-y in inp):
				return (x, y, target-x-y)
if debug:
	example_entrys1 = part1(target_prod, example_input)
	assert (example_entrys1[0] * example_entrys1[1] == 514579)

puzzle_entrys = part1(target_prod, puzzle_input)
print("Part I:",puzzle_entrys[0] * puzzle_entrys[1])

if debug:
	example_entrys2 = part2(target_prod, example_input)
	assert (example_entrys2[0] * example_entrys2[1] * example_entrys2[2] == 241861950)

puzzle_entrys = part2(target_prod, puzzle_input)
print("Part II:",puzzle_entrys[0] * puzzle_entrys[1] * puzzle_entrys[2])

ende = time.perf_counter()
print('{:5.3f}s'.format(ende-start))
