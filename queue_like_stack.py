import queue

my_stack = queue.LifoQueue(maxsize=0)
my_stack.put("2000")
my_stack.put("2001")
my_stack.put("2002")
my_stack.put("2003")
my_stack.put("2004")

print("The Size is: ", my_stack.qsize())

print(my_stack.get())
print(my_stack.get())
print(my_stack.get())
print(my_stack.get())
print(my_stack.get())

print("Empty stack: ", my_stack.empty())