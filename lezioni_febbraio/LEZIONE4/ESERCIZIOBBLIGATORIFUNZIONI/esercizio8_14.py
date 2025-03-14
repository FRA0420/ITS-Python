def make_car(manufacturer:str,model:str,**kwargs):
    output= f"{manufacturer.title()}, {model.title()}, "
    counter=0
    for k,v in kwargs.items():
        output += f"{k}={v}"
        if counter < len(kwargs)-1:
            output += ","
        counter += 1
    
    print(kwargs)
    print(output)
    return output

car = make_car("subaru","outback",color="blue",two_package=True)

