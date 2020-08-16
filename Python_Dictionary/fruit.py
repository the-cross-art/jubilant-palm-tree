fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yelow citrus fruit",
         "grape": "a small,  sweet fruit growing in bunches",
         "lime": "a sour , green citrus fruit",
         }

print(fruit)

veg = {"cabbage": "every childs fav",
       "sprouts": "ummmm, lovely",
       "spinach": "can I hear some more fruit, please"}
print(veg)

# to update and add two dictionaries
# veg.update(fruit)
# print(veg)
#
# print(fruit.update(veg))
# print(fruit)
nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)