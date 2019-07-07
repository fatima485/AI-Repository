import json
#dumb = insert or store, load=get 
alphabets = ["a","b","c"]
with open("alpha.json","w") as f:
    json.dump(alphabets,f)

student1={
    "Name" : "Fatima",
    "age" : "20",
    "roll no" :'cs-009'
}


with open("student1.json","w") as f:
    json.dump(student1,f)
with open("student1.json","r") as f:
    print(json.load(f))
