import pyttsx3
book= open(r"book.txt")
book_text=book.readlies()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runandwait()
    