# What is a dictionary?

# A dictionary stores data as key → value pairs. Think of it like a real dictionary: you look up a word (key) to get its meaning (value).

person={
    "name":"hariom",
    "age":22,
    "city":"bng"
}
print(person)

# {} curly braces make a dictionary
# "name" is a key
# "Alex" is its value
# Each pair is separated by a comma

# You get a value by putting its key in square brackets:
print(person["name"])
print(person["age"])
print(person["city"])
# print(person["state"])

# If the key doesn't exist, this crashes your program. Safer way — use

print("name",person.get("name"))
print("state",person.get("state","N/A"))# N/A (your own default)

person["state"]="KA"
person["CT"]="IND"

print(person)

del person["CT"]
print(person)

  #or
if "CT" in person:
    person.pop("CT")
else:
     print("No, name is not there")

for key,value in person.items():
     print(key,"->",value)


tool_result = {
    "status": "success",
    "data": {"temperature": 30, "city": "Bengaluru"}
}

print(tool_result)

print("---------------")

print(tool_result["data"])
print(tool_result["data"]["temperature"])

if "data" in tool_result.items():
     del tool_result["data"]

print(tool_result)

# task

agent_memory={
     
}


print(agent_memory)
agent_memory["user_name"]="?"
agent_memory["last_question"]="?"
agent_memory["tool_used"]={}
del agent_memory["tool_used"]

agent_memory["tool_used"]=[]
agent_memory["tool_used"].append("?")
agent_memory["tool_used"].append("?")

agent_memory["turn_count"]=0;
agent_memory["turn_count"]=agent_memory.get("turn_count")+1

for key,val in agent_memory.items():
     print(key,"->",val)

print(agent_memory)

print(agent_memory["tool_used"][1])







