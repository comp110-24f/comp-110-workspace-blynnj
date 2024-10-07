"""Import and call functions from other files"""

__author__: str = "730749523"


from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))

# calling get_coords using global variables
print(get_coords(x, y))
