# 7.2 dictionary
dict={}
#1.syntax
#dictionary_name = {key1: value1, key2: value2, key3: value3}
stud = {
"name": "varun",
"age": 24,
"course": "ECE"
}
print(stud)

#2. Dictionary Operations
#2.1 Accessing Values
print(stud["name"])
print(stud.get("age"))

#dict.get(key, default_value) will return None or the specified default_value if the key is not found.
print(stud.get("id", "Not Available")) 

# 2.2 Adding and Updating Items
stud["age"]=25 # updating
stud["id"]=1234567809  #new
print(stud)

# 2.3 Removing Items from a Dictionary
#pop()
a=stud.pop("age")
print(a)

#del()
del stud["id"]
print(stud)

#popitem()
stud.popitem()
print(stud)

#clear()
stud.clear()
print(stud)
