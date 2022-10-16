from unicodedata import name


def Hello(name="jose"):
    return "hello "+name
 
print(Hello())

mynewgreet = Hello

print(mynewgreet())

