sampledict:dict={"name":"kelly", "age":25, "salary": 8000, "city": "new york"}
keys:list[str]=["name", "salary"]
print(sampledict["name"])  
newdict:dict={k: sampledict[k] for k in keys}
print(newdict)          