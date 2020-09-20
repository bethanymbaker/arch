#!/bin/python

import sys

import json

# create a dictionary with all the champion data
champion_powers = json.load(sys.stdin)


def game_power(champion_name):
    return champion_powers[champion_name]['game_power']


def lore_power(champion_name):
    return champion_powers[champion_name]['lore_power']


# The battle score for a champion is defined by the remainder of champion's lore power divided by the enemy's game power (AKA 'mod')
# For example, if Jax has lore power of 5, and game power of 12. TwistedFate has lore power of 20 and game power of 12.
# Damage for Jax against TF is 5 mod 12 = 5. Damage for TF against Jax is 20 mod 12 = 8.
# Since 8 > 5, TF wins. If a tie happens, return None as the winner.
#
# The function is expected to return an STRING which is the name of the winner.
# The function accepts 2 STRINGs champion_a, champion_b as parameters.

def lore_battle(champion_a, champion_b):
    damage_a = lore_power(champion_a) % game_power(champion_b)
    damage_b = lore_power(champion_b) % game_power(champion_a)
    if damage_a > damage_b:
        return champion_a
    if damage_a < damage_b:
        return champion_b
    return None


# champions_list contains the names for all champions

champions_list = champion_powers.keys()


# Complete the 'lore_war_winner' function below.
# It compures when all champions battle against each other, who won the most lore battles.
# Return results should be the name of the champion who won the lore war, and the number of battles they won.
#
# The function is expected to return an STRING and INTEGER.

def lore_war_winner():
    l = list(champions_list)
    d = {}
    for idx, champ_1 in enumerate(l[:-1]):
        for champ_2 in l[idx + 1:]:
            winner = lore_battle(champ_1, champ_2)
            if winner is not None:
                if winner in d:
                    d[winner] += 1
                else:
                    d[winner] = 1
    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    return sorted_d[0]


winner, wons = lore_war_winner()
print("The winner of the lore war is:", winner)
print("Num won:", wons)
