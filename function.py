def greet():
    print("hello!")

# function calling
greet()

# function with parameter

def greet(name):
    print("hello",name)

greet("Raj")    
greet("Vinay")
greet("Vikas")


# Functions that return a value
# print() just displays something. return actually gives back a value you can store or use later.

def add(a,b):
    return a+b

print(add(10,20))
print(add(20,30))


def add_print(a, b):
    print(a + b)   # only shows it, doesn't give it back

x = add_print(3, 5)   # prints 8
print(x)  #None

# Default parameter values
def greet(name="friend"):
    print("Hello",name)

greet()   
greet("son")


def get_weather(city):
    return {"city":city,"temp":30,"condition":"sunny"}

weather=get_weather("banglore")
print(weather)

agent_memory = {
    "user_name": "Alex",
    "last_question": "What's the weather?",
    "tool_used": [],
    "turn_count": 1
}
def add_tool_use(memory,tool_name):
    memory["tool_used"].append(tool_name)
    return memory["tool_used"][-1]
    # return memory
print(add_tool_use(agent_memory,"search_web"))
# add_tool_use(agent_memory,"search_web")
# print(agent_memory)

# *args and **kwargs
# This is the last function-related piece you need before agent code starts making sense. You'll see this pattern in almost every AI framework.

# Problem it solves

# What if you don't know in advance how many inputs a function should take?


def add_two(a,b):
    return a*b

print(add_two(10,20))


# *args — accept any number of positional inputs

def add_all(*args):
    print(type(args))
    return sum(args)

print(add_all(1,2,3))
print(add_all(1,2,3,4,5,6))


# **kwargs scoops up any number of key=value inputs into a dictionary named kwargs.
def show_info(**kwargs):
    print(type(kwargs))
    print(kwargs)

show_info(name="vinay",age="22")



def run_tool(tool_name, **kwargs):
    if tool_name == "get_weather":
        return f"Weather for {kwargs['city']}: sunny"
    elif tool_name == "search":
        return f"Searching for: {kwargs['query']}"

print(run_tool("get_weather", city="Bengaluru"))
print(run_tool("search", query="latest AI news"))

# task
def log_event(**kwargs):
    for key,val in kwargs.items():
        print(key,"->",val)

log_event(event="tool_call", tool="search_web", turn=1)







