def hello(name = "lalit"):
    print("THE HELLO() FUNCTION HAS BEEN RUN !")

    def greet():
        return "THIS STRING IS INSIDE GREET()"
    def Welcome():
        return "THIS STRING IS INSIDE WELCOME!"
    
    print(greet())
    print(Welcome())
    print("END OF HELLO()")


    if name == "lalit":
        return greet
     
    else:
        return Welcome

    x =  HELLO()

    print(x())
