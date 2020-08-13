fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yelow citrus fruit",
         "grape": "a small,  sweet fruit growing in bunches",
         "lime": "a sour , green citrus fruit",
         "apple": "round and crunchy"}

print(fruit)
print(fruit["lemon"])

# # to add new value to dictionary
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
#
# # dictionary values get changed by assigning same value
# fruit["pear"] = "a great white apple"
# print(fruit)
# del fruit["lemon"]
# print(fruit)
# fruit.clear()
# cant use del fruit as ir creates an error
print(fruit)
# while True:
#     dic_key = input("Please enter a fruit")
#     if dic_key == "quit":
#         break
#     description = fruit.get(dic_key, "we dont have a " + dic_key)
#     print(description)
    # if dic_key in fruit:
    #     description = fruit.get(dic_key)
    #     print(description)
    # else:
    #     print("we Dont have a " + dic_key)


# for snack in fruit:
#     print(fruit[snack])

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-'*40)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " = " + fruit[f])

for f in sorted(fruit.keys()):
    print(f + " = " + fruit[f])

# not an very efficent way to
# for val in fruit.values():
#     print(val)
#
# for key in fruit:
#     print(fruit[key])

fruit_keys = fruit.keys()
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)