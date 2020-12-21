#!/usr/bin/python3

import sys
import re
import math
import functools

filename = 'day21/smallinput.txt'

ingredients = {}
all_allergens = set()
recipes = []

with open(filename) as f_obj:
    # Assume the matrix starts at 0,0 (z is 0)
    # Read the list and add it to the space

    for line in f_obj:
        line = line.rstrip()
        
        a = re.match(r'^(.*) \(contains (.*)\)$',line)
        print(a.group(1), a.group(2))

        d = dict()
        d["ingredients"] = a.group(1).split(' ')
        d["allergens"] = set()     

        for ingredient in a.group(1).split(' '):
            for allergen in a.group(2).split(','):
                allergen = allergen.strip()
                all_allergens.add(allergen)
                d["allergens"].add(allergen)

            if (not ingredient in ingredients) :
                ingredients[ingredient] = {}
                ingredients[ingredient]["could_have"] = set()
                ingredients[ingredient]["cant_have"] = set()

                      
            ingredients[ingredient]["could_have"].add(allergen)

        recipes.append(d)
    
print(recipes)
print(ingredients)
for ing in ingredients:
    # The could_have member has the list of all allergens this ingredient
    # could possibly have. For each of those, we go through all recipes
    # to see if there are recipes that don't have that allergen. If so,
    # it can't have that one

    for r in recipes:
        if not ing in r["ingredients"] :
            continue

        # OK, this recipe has this ingredient. 
        # Does it have at least one of the allergens that this ingredient 
        # is associated with?

        if len(ingredients[ing]["could_have"] & r["allergens"]) == 0 :
            ingredients[ing]["cant_have"] |= r["allergens"]

print (ingredients)
for ing in ingredients:
    ingredients[ing]["could_have"] -= ingredients[ing]["cant_have"]

    print(ing, ": ", ingredients[ing]["could_have"])
