panagram = """The quick brown
fox jumps\t
over the lazy dog"""

words = panagram.split()
print(words)
numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

data = ['9', '223', '372', '036', '854']
for index in range(len(data)):
    data[index]=int(data[index])

print(data)

integer_values=[]
for value in data:
    integer_values.append(int(value))

print(integer_values)