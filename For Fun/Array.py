"""" An array has to be one type of thing. Eg only integars or only strings.
This is why the code belows puts a list into the array cos their is a mix of types """

from array import array

scores = array('d')
print(scores)
scores.append(98)
scores.append(97)
print(scores)

# scores.insert(0, 'helloo')
# print(scores)
""" Insert does not work with arrays"""
