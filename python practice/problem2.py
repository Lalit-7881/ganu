# Write program to detect double space
from tokenize import Double


st = "This is a string with double    space"

Doublespace= st.find("  ")
print("Double spaces")