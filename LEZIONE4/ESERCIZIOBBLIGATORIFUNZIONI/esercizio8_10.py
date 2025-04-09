# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 
# Write a function called send_messages() that prints each text message 
# and moves each message to a new list called sent_messages as it’s printed. 
# After calling the function, print both of your lists to make sure the messages were moved correctly.

def show_messages(messages:list[str]) -> str:
    for n in messages:
        print(n)

myList:list[str]=["ciao","bla","bla"]

sent_messages:list[str]=myList[:]

def send_messages(par1:list[str]) -> None:
    for n in par1:
        print(n)
        par1.append(n)
    print(par1)

print(myList)
print(send_messages(sent_messages))

