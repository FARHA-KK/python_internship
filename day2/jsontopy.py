import json
student=[{ "id":1,"name":'Anu'},
{"id":2,"name":'Adhi'},
{"id":3,"name":"dhinu"},
{"id":4,"name":"Nidhu"},
{"id":5,"name":"gidhu"}]

with open("student.json",'w') as f:
    json.dump(student,f,indent=2)
with open("student.json",'r') as f:
     print(f.read())    
with open("student.json",'r') as f:
        data=json.load(f)
        for i in data:
            print(f"id:{i['id']},name:{i['name']}")
       
        