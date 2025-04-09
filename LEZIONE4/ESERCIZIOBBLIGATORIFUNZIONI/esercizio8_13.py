def build_profile(first_name:str,last_name:str,**kwargs)-> str:
    output:str=f"{first_name} {last_name},"
    counter=0
    for key,value in kwargs.items():
        output += f"{key} {value} "
        if counter < len(kwargs)-1:
            output+= ","
        counter += 1
    return output
    

print(build_profile("Eric","Crow",age=45,hair="Brown",weight=72))

