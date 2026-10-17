# DICTIONARIES IN PYTHON
#dICTIONARIES ARE USED TO STORE DATA VALUIES IN KEY:VALUES PAIRS ,THEY ARE UNORDERD ,MUTABLE &DONT ALOW DUPLICATE KEYS 

dictionary = {
    "name" : "fardeen",
    "details":["ballia","baheri","pathantoli"],
    "cgpa":9.12,
    "marks":300,
    "isstudent":True,
}
dictionary["marks"]=299
print(type(dictionary))
print(dictionary["name"])
print(dictionary["details"])
print(dictionary["cgpa"])
print(dictionary["marks"])

#null dictionary

nulldic={}

nulldic["name:"]="fareen khan"
nulldic["marks:"]=299
print(nulldic)

#nested dictionary


student = {
    "name":"fardeen khan ",
    "program":'b.tech',
    "cgpa":9,
    "subject" : {
        "phy":58,
        "math":52,
        "electronic comuunicatiuon": 60,
        "electrical enginnering":60,
        "communication skills":67
    }
}
student.update({"city":"ballia"})
print(student)
print(student["subject"])
print(student["subject"]["communication skills"])


print(student.get("subject1"))# none return if anyerror 

print((student.keys()))
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())

print(student.items()) 

# store following word meaning in a python dictionary :
# table:"a piece of furniture ","list of facts &and figures"
# cat ;' "a small animal"

dictionary={
    "table":"a piece of furniture",
    "cat": "a small animal",
}
print(type(dictionary))
print(dictionary)