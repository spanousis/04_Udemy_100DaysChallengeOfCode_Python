"""
This is a difficult challenge.
Your are goint to write a program that will mark a spot on a map with an X.
In the starting code, you will find a variable called map.
This map contains a nested list. When map is printed this is what it 
looks like, notice the nesting:
[['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
This is a bit hard to wrk with. So on lines 6 and 23, we've used this line
of code print(f"{row1}\n{row2}\n{row3}") to format
the 3 lists to printed as a 3 by 3 grid, each on a new line.
['_', '_', '_']
['_', '_', '_']
['_', '_', '_']

  A  B  C
1 _  _  _
2 _  X  _
3 _  _  _

Input in this case is B2

"""

line1 = ["_", "_", "_"]
line2 = ["_", "_", "_"]
line3 = ["_", "_", "_"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# Don't change the code above
# Write your code below this row

columnChar = position[0].lower()
columnList = ["a", "b", "c"]
columnNum = columnList.index(columnChar)

rowNum = int(position[1]) - 1
map[rowNum][columnNum] = "X"


# Write your code above this row
# Don't change the code below
print(f"{line1}\n{line2}\n{line3}")