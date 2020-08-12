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
while True:
    dic_key = input("Please enter a fruit")
    if dic_key == "quit":
        break
    if dic_key in fruit:
        description = fruit.get(dic_key)
        print(description)
    else:
        print("we Dont have a " + dic_key)
