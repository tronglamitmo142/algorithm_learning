# Stack 
- Linear data structure that store items in **Last-in/First-Out(LIFO)**
- The insert and delete operations are often called **push and pop**
- Functions:
  - empty() - Returning where the stack is empyty - Time Complexity: O(1)
  - size() - Returns the size of the stack - O(1)
  - top()/peek() - Returnn a reference to the topmost element of the stack - O(1)
  - push() - Inserts the element at the top of the stack - O(1)
  - pop() - Delete the topmost element of the stack - O(1)

# Queue 
- Linear data structure that store items in **First-in/First-out** 
- Operations:
  - Enqueue: Adds an itmes to the queue - O(1)
  - Dequeue: Removes an item from the queue - O(1)
  - Front: Get the front item from queue - O(1)
  - Rear: Get the last item from queue - O(1)

- Implementation using queue.Queue:
  - `import queue` 
  - Add element in queue: `q.put(5)`
  - Delete element in queue: `q.get(5)`
  - Get the frist element in queue: `q.queue[0]`
  - Get the queue's size: `q.qsize()`
  - Check queue is empty: `q.isEmpty()`

