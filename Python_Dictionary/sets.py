# farm_animals = {"cow", "sheep", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("=" * 40)
#
# wild_animals = set(["Lion", "Tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)
#

even = set(range(0, 40, 2))
print(even)
print(len(even))

square_tuple = (4, 6, 9, 16, 25)
squares = set(square_tuple)
print(squares)

print(even.union(squares))
print(len(even.union(squares)))

print(squares.union(even))
print("="*40)

print(squares.intersection(even))