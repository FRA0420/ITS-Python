numbers_x:list[int]=[10,20,30,40,10]
numbers_y:list[int]=[75,65,35,75,30]
len_x=len(numbers_x)
len_y=len(numbers_y)

print(f"Given list: {numbers_x} \nresult is", numbers_x[0]==numbers_x[len_x-1])
print(f"Given list: {numbers_y} \nresult is", numbers_y[0]==numbers_y[len_y-1])