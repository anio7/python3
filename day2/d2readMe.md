Day 2 teaches Datatypes, Numbers,Operations, Type Conversion, f-strings

There are 4 different types of data-types in python

Strings - which area surrounded by double quotes. eg ""
We can use len to find the length of the string. eg print(len("hello"))
We can use index or subscripting to get the exact character in a string starting from the number zero(0) or we can use negative numbers from (-)1 as the last character in the string. eg. print("hello"[0])

Integers or numbers are whole numbers and to convert some strings to numbers from input we use int() conversion function

Float- short for floating point numbers since they have decimal places eg 10.1

Booleans which is basically true or false values.

To figure out which data type it is you can do type checking by input the value into type()

Number Operations
addition(+),subtraction(-),multiplication(*),exponential(**), division(/), floor division(//)

PEMDAS - parentheses, exponential, multiplication or division, addition or subtraction.

Between the calculations of M&D or A&S the one that is closest to the left will be prioritized! Calculation goes from left to right - eg 3*3+3/3-3 = 7

we can use round(var, decimal_places) for rounding numbers to decimal places.

we also have assignment operators +=,*=,/=,-=.
+= is also known as a increment operator


f-strings allows us to substitute values into a expression without the hassle of excessive scripting. The value being substituted, is always placed inside of {} which is further inside "" to give you the following example.
eg print(f"{var}")