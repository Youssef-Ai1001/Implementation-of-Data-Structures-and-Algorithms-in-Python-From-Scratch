import queue

# queue_like_stack
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

# queue
orders_queue = queue.SimpleQueue()
orders_queue.put("10")
orders_queue.put("20")
orders_queue.put("30")
orders_queue.put("40")
orders_queue.put("50")

print("The Size is: ", orders_queue.qsize())

orders_queue.get()
orders_queue.get()
orders_queue.get()
orders_queue.get()
orders_queue.get()

print("Empty queue: ", orders_queue.empty())