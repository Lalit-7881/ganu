import two
print("Top Level two.py")
two.func()


if __name__ == "__main__":
   print("two.py vbeing run directly")
else:
    print("two is being imported")