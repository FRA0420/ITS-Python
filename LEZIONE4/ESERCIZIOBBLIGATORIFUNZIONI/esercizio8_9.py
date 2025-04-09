#8-9. Messages: Make a list containing a series of short text messages. 
#Pass the list to a function called show_messages(), which prints each text message.
def show_messages(messages:list[str]) -> str:
    for n in messages:
        print(n)


myList:list[str]=["ciao","bla","adios","blua"]
show_messages(myList)
