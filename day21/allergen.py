#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day21/input.txt'


# ingredients with the set of all recipes that they are in
ingredients = {}


# Allergens with the set of all recipes they are in.
allergens = {}

recipeNum = 0
with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    for line in f_obj:
        line = line.rstrip()
        
        a = re.match(r'^(.*) \(contains (.*)\)$',line)

        for ingredient in a.group(1).split(' '):

            if not ingredient in ingredients:
                ingredients[ingredient] = {}
                ingredients[ingredient]["recipes"] = set()
                ingredients[ingredient]["count"] = 0


            ingredients[ingredient]["recipes"].add(recipeNum)
            ingredients[ingredient]["count"] += 1

        for allergen in a.group(2).split(','):
            allergen = allergen.strip()
            if not allergen in allergens:
                allergens[allergen] = set()
            
            allergens[allergen].add(recipeNum)

        recipeNum += 1

# Now for each ingredient see if its set of recipes is a subset of
# any of the allergen sets

totalIngredients = 0

inertIngredients = []

for ing in ingredients :
    could_be_allergen = False
    for a in allergens:
        if (allergens[a] <= ingredients[ing]["recipes"]) :
            # Could be this allergen, so we continue
            could_be_allergen = True
            break

    if not could_be_allergen:
        totalIngredients += ingredients[ing]["count"]
        # Get rid of the ingredient that is inert
        inertIngredients.append(ing)
        
print("Total Ingredients:", totalIngredients)

for ing in inertIngredients:
    del ingredients[ing]

dangerous = {}
while len(allergens) :
    foundAl = ''
    matchedIng = ''
    for al in allergens:
        onlyOne = True
        matchedIng = ''
        for ing in ingredients:
            if (allergens[al] <= ingredients[ing]["recipes"]) :
                if (matchedIng == ''):
                    matchedIng = ing
                else:
                    onlyOne = False
                    break
        if (onlyOne) :
            print(al,":",matchedIng)
            del ingredients[matchedIng]
            foundAl = al
            break
    del allergens[foundAl]
    dangerous[foundAl] = matchedIng

print(sorted(dangerous))
part2 = ",".join([dangerous[i] for i in sorted(dangerous)])

print(part2)

