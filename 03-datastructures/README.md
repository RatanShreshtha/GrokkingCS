# What Are Linear Structures?

Stacks, queues, deques, and lists are examples of data collections whose items are ordered depending on how they are added or removed. Once an item is added, it stays in that position relative to the other elements that came before and came after it. Collections such as these are often referred to as linear data structures.


# What is a Stack?

A stack (sometimes called a “push-down stack”) is an ordered collection of items where the addition of new items and the removal of existing items always takes place at the same end. This end is commonly referred to as the “top.” The end opposite the top is known as the “base.”

The base of the stack is significant since items stored in the stack that are closer to the base represent those that have been in the stack the longest. The most recently added item is the one that is in position to be removed first. This ordering principle is sometimes called LIFO, last-in first-out. It provides an ordering based on length of time in the collection. Newer items are near the top, while older items are near the base.

Many examples of stacks occur in everyday situations. 
1. Almost any cafeteria has a stack of trays or plates where you take the one at the top, uncovering a new tray or plate for the next customer in line.
2. Every web browser has a Back button. As you navigate from web page to web page, those pages are placed on a stack (actually it is the URLs that are going on the stack). The current page that you are viewing is on the top and the first page you looked at is at the base. If you click on the Back button, you begin to move in reverse order through the pages.

## Stack Abstract Data Type

The stack abstract data type is defined by the following structure and operations. A stack is structured, as described above, as an ordered collection of items where items are added to and removed from the end called the **top**. Stacks are ordered **LIFO**. 

### Stack Operations

- `Stack()` creates a new stack that is empty. It needs no parameters and returns an empty stack.

- `push(item)` adds a new item to the top of the stack. It needs the item and returns nothing.

- `pop()` removes the top item from the stack. It needs no parameters and returns the item. The stack is modified.

- `peek()` returns the top item from the stack but does not remove it. It needs no parameters. The stack is not modified.

- `is_empty()` tests to see whether the stack is empty. It needs no parameters and returns a boolean value.

- `size()` returns the number of items on the stack. It needs no parameters and returns an integer.

**Example**

`s = Stack()` creates a stack that starts out empty, table below shows the results of a sequence of stack operations.

| Stack Operation |    Stack Contents    | Return Value |
| :-------------: | :------------------: | :----------: |
| `s.is_empty()`  |         `[]`         |    `True`    |
|   `s.push(4)`   |        `[4]`         |              |
| `s.push('dog')` |     `[4,'dog']`      |              |
|   `s.peek()`    |     `[4,'dog']`      |   `'dog'`    |
| `s.push(True)`  |   `[4,'dog',True]`   |              |
|   `s.size()`    |   `[4,'dog',True]`   |     `3`      |
| `s.is_empty()`  |   `[4,'dog',True]`   |   `False`    |
|  `s.push(8.4)`  | `[4,'dog',True,8.4]` |              |
|    `s.pop()`    |   `[4,'dog',True]`   |    `8.4`     |
|    `s.pop()`    |     `[4,'dog']`      |    `True`    |
|   `s.size()`    |     `[4,'dog']`      |     `2`      |


|   Queue Operation   |    Queue Contents    | Return Value |
| :-----------------: | :------------------: | :----------: |
|   `q.is_empty()`    |         `[]`         |    `True`    |
|   `q.enqueue(4)`    |        `[4]`         |              |
| `q.enqueue('dog')`  |     `['dog',4]`      |              |
| `q.enqueue('True')` |   `[True,'dog',4]`   |              |
|     `q.size()`      |   `[True,'dog',4]`   |     `3`      |
|   `q.is_empty()`    |   `[True,'dog',4]`   |   `False`    |
|  `q.enqueue(8.4)`   | `[8.4,True,'dog',4]` |              |
|    `q.dequeue()`    | `[8.4,True],'dog']`  |     `4`      |
|    `q.dequeue()`    |     `[8.4,True]`     |   `'dog'`    |
|     `q.size()`      |     `[8.4,True]`     |     `2`      |


|   Deque Operation    |       Deque Contents       | Return Value |
| :------------------: | :------------------------: | :----------: |
|    `d.is_empty()`    |            `[]`            |     True     |
|   `d.add_rear(4)`    |           `[4]`            |              |
| `d.add_rear('dog')`  |        `['dog',4,]`        |              |
| `d.add_front('cat')` |     `['dog',4,'cat']`      |              |
| `d.add_front(True)`  |   `['dog',4,'cat',True]`   |              |
|      `d.size()`      |   `['dog',4,'cat',True]`   |      4       |
|    `d.is_empty()`    |   `['dog',4,'cat',True]`   |    False     |
|  `d.add_rear(8.4)`   | `[8.4,'dog',4,'cat',True]` |              |
|  `d.remove_rear()`   |   `['dog',4,'cat',True]`   |     8.4      |
|  `d.remove_front()`  |     `['dog',4,'cat']`      |     True     |





## Deque Abstract Data Type

The deque abstract data type is defined by the following structure and operations. A deque is structured, as described above, as an ordered collection of items where items are added and removed from either end, either **front** or **rear**. 

### The deque operations are given below.

- `Deque()` creates a new deque that is empty. It needs no parameters and returns an empty deque.

- `add_front(item)` adds a new item to the front of the deque. It needs the item and returns nothing.

- `add_rear(item)` adds a new item to the rear of the deque. It needs the item and returns nothing.

- `remove_front()` removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.

- `remove_rear()` removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.

- `is_empty()` tests to see whether the deque is empty. It needs no parameters and returns a boolean value.

- `size()` returns the number of items in the deque. It needs no parameters and returns an integer.


`d = Deque()` creates a deque that starts out empty, table below shows the results of a sequence of deque operations.


|   Deque Operation    |       Deque Contents       | Return Value |
| :------------------: | :------------------------: | :----------: |
|    `d.is_empty()`    |            `[]`            |     True     |
|   `d.add_rear(4)`    |           `[4]`            |              |
| `d.add_rear('dog')`  |        `['dog',4,]`        |              |
| `d.add_front('cat')` |     `['dog',4,'cat']`      |              |
| `d.add_front(True)`  |   `['dog',4,'cat',True]`   |              |
|      `d.size()`      |   `['dog',4,'cat',True]`   |      4       |
|    `d.is_empty()`    |   `['dog',4,'cat',True]`   |    False     |
|  `d.add_rear(8.4)`   | `[8.4,'dog',4,'cat',True]` |              |
|  `d.remove_rear()`   |   `['dog',4,'cat',True]`   |     8.4      |
|  `d.remove_front()`  |     `['dog',4,'cat']`      |     True     |