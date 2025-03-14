# 8-11. Archived Messages: Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

def send_messages(par1:list[str]) -> None:
    new_list= par1.copy()
    for n in new_list:
        print(n)
        
    print(new_list)
myList:list[str]=["ciao","bla","bla"]
print(myList)
send_messages(myList)
