import heapq
from enum import Enum
from collections import defaultdict, deque
from datetime import datetime

'''
#Implement a Contact Manager using Array and Linked List with operations Add, Search, and Delete contacts, generate Search and Delete methods, and compare both approaches based on insertion and deletion efficiency.

# Contact Manager using Array and Linked List

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __repr__(self):
        return f"Contact({self.name}, {self.phone}, {self.email})"


# Array-based Contact Manager
class ArrayContactManager:
    def __init__(self):
        self.contacts = []
    
    def add(self, name, phone, email):
        self.contacts.append(Contact(name, phone, email))
    
    def search(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    
    def delete(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts.pop(i)
                return True
        return False
    
    def display(self):
        return self.contacts


# Node for Linked List
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.next = None


# Linked List-based Contact Manager
class LinkedListContactManager:
    def __init__(self):
        self.head = None
    
    def add(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        new_node = Node(new_contact)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def search(self, name):
        current = self.head
        while current:
            if current.contact.name == name:
                return current.contact
            current = current.next
        return None
    
    def delete(self, name):
        if not self.head:
            return False
        if self.head.contact.name == name:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.contact.name == name:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def display(self):
        contacts = []
        current = self.head
        while current:
            contacts.append(current.contact)
            current = current.next
        return contacts


# Comparison and Testing
if __name__ == "__main__":
    print("=== ARRAY-BASED CONTACT MANAGER ===")
    array_manager = ArrayContactManager()
    array_manager.add("Alice", "123-456-7890", "alice@email.com")
    array_manager.add("Bob", "098-765-4321", "bob@email.com")
    array_manager.add("Charlie", "111-222-3333", "charlie@email.com")
    
    print("All Contacts:", array_manager.display())
    print("Search 'Bob':", array_manager.search("Bob"))
    array_manager.delete("Bob")
    print("After deleting 'Bob':", array_manager.display())
    
    print("\n=== LINKED LIST-BASED CONTACT MANAGER ===")
    ll_manager = LinkedListContactManager()
    ll_manager.add("Alice", "123-456-7890", "alice@email.com")
    ll_manager.add("Bob", "098-765-4321", "bob@email.com")
    ll_manager.add("Charlie", "111-222-3333", "charlie@email.com")
    
    print("All Contacts:", ll_manager.display())
    print("Search 'Bob':", ll_manager.search("Bob"))
    ll_manager.delete("Bob")
    print("After deleting 'Bob':", ll_manager.display())
    
    print("\n=== EFFICIENCY COMPARISON ===")
    print("Array-based: Insert O(1), Search O(n), Delete O(n)")
    print("Linked List: Insert O(n), Search O(n), Delete O(n)")'''

'''#2.Implement a **Library Book Request System** using a **Queue (FIFO)** and **Priority Queue** where **faculty requests have higher priority than student requests**, generate **enqueue() and dequeue() methods using GitHub Copilot**, and **test with mixed student and faculty requests to verify correct prioritization.
class RequestType(Enum):
    STUDENT = 2
    FACULTY = 1

class BookRequest:
    def __init__(self, name, book_title, request_type):
        self.name = name
        self.book_title = book_title
        self.request_type = request_type
        self.priority = request_type.value
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __repr__(self):
        return f"BookRequest({self.name}, {self.book_title}, {self.request_type.name})"

class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, request):
        self.items.append(request)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return self.items

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, request):
        heapq.heappush(self.items, request)
    
    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.items)
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def display(self):
        return sorted(self.items)

if __name__ == "__main__":
    print("=== FIFO QUEUE ===")
    fifo_queue = Queue()
    fifo_queue.enqueue(BookRequest("Alice", "Python 101", RequestType.STUDENT))
    fifo_queue.enqueue(BookRequest("Prof. Smith", "Advanced AI", RequestType.FACULTY))
    fifo_queue.enqueue(BookRequest("Bob", "Data Science", RequestType.STUDENT))
    
    print("Queue:", fifo_queue.display())
    print("Dequeue:", fifo_queue.dequeue())
    print("Dequeue:", fifo_queue.dequeue())
    
    print("\n=== PRIORITY QUEUE ===")
    pq = PriorityQueue()
    pq.enqueue(BookRequest("Alice", "Python 101", RequestType.STUDENT))
    pq.enqueue(BookRequest("Prof. Smith", "Advanced AI", RequestType.FACULTY))
    pq.enqueue(BookRequest("Bob", "Data Science", RequestType.STUDENT))
    pq.enqueue(BookRequest("Prof. Johnson", "Machine Learning", RequestType.FACULTY))
    
    print("Priority Queue:", pq.display())
    print("\nProcessing requests:")
    while not pq.is_empty():
        print("Dequeue:", pq.dequeue())
'''
'''#3Implement an **IT Help Desk Ticket System using a Stack (LIFO)** with operations **push(ticket), pop(), and peek()**, simulate **five tickets being raised and resolved**, and use **GitHub Copilot to suggest additional operations like isEmpty() and isFull()**.
class Ticket:
    def __init__(self, ticket_id, description, priority):
        self.ticket_id = ticket_id
        self.description = description
        self.priority = priority
    
    def __repr__(self):
        return f"Ticket({self.ticket_id}, {self.description}, Priority: {self.priority})"


class Stack:
    def __init__(self, max_size=100):
        self.items = []
        self.max_size = max_size
    
    def push(self, ticket):
        if not self.is_full():
            self.items.append(ticket)
            return True
        return False
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) >= self.max_size
    
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items


if __name__ == "__main__":
    print("=== IT HELP DESK TICKET SYSTEM ===\n")
    ticket_stack = Stack(max_size=10)
    
    print("Raising tickets...")
    ticket_stack.push(Ticket("T001", "Printer not working", 3))
    ticket_stack.push(Ticket("T002", "Network connectivity issue", 1))
    ticket_stack.push(Ticket("T003", "Password reset request", 2))
    ticket_stack.push(Ticket("T004", "Software installation", 2))
    ticket_stack.push(Ticket("T005", "Email configuration", 1))
    
    print(f"Total tickets in stack: {ticket_stack.size()}")
    print(f"Top ticket (peek): {ticket_stack.peek()}\n")
    
    print("Resolving tickets (LIFO order):")
    while not ticket_stack.is_empty():
        ticket = ticket_stack.pop()
        print(f"Resolved: {ticket}")
    
    print(f"\nStack empty: {ticket_stack.is_empty()}")'''
'''#4.Implement a **Hash Table in Python** with methods **insert, search, and delete**, handle **collisions using chaining**, and generate **well-commented methods** starting from `class HashTable: pass`.
class HashTable:
    def __init__(self, size=10):
        """Initialize the hash table with a specified size."""
        self.size = size
        self.table = [[] for _ in range(size)]  # Create a list of empty lists for chaining

    def _hash(self, key):
        """Generate a hash for the given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table."""
        index = self._hash(key)
        # Check if the key already exists and update it
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Update existing key
                return
        # If key does not exist, add new key-value pair
        self.table[index].append((key, value))

    def search(self, key):
        """Search for a value by its key in the hash table."""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v  # Return the value if key is found
        return None  # Return None if key is not found

    def delete(self, key):
        """Delete a key-value pair from the hash table."""
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]  # Remove the key-value pair
                return True  # Return True if deletion was successful
        return False  # Return False if key was not found
# Example usage
if __name__ == "__main__":
    hash_table = HashTable(size=5)
    
    # Insert key-value pairs
    hash_table.insert("name", "Alice")
    hash_table.insert("age", 30)
    hash_table.insert("city", "New York")
    
    # Search for values
    print("Search for 'name':", hash_table.search("name"))  # Output: Alice
    print("Search for 'age':", hash_table.search("age"))    # Output: 30
    print("Search for 'country':", hash_table.search("country"))  # Output: None
    
    # Delete a key-value pair
    print("Delete 'age':", hash_table.delete("age"))  # Output: True
    print("Search for 'age' after deletion:", hash_table.search("age"))  # Output: None
'''
#5.Design a **Campus Resource Management System** by selecting suitable **data structures for attendance tracking, event registration, library borrowing, bus scheduling, and cafeteria order queue**, justify each choice in **2–3 sentences**, and **implement one feature in Python using AI-generated code** with a **Feature → Data Structure → Justification table**.
# Campus Resource Management System


# Feature → Data Structure → Justification Table
"""
┌─────────────────────┬──────────────────────┬─────────────────────────────────────────┐
│ Feature             │ Data Structure       │ Justification                           │
├─────────────────────┼──────────────────────┼─────────────────────────────────────────┤
│ Attendance Tracking │ Dictionary/Hash Map  │ O(1) lookup by student ID for marking  │
│                     │                      │ attendance and retrieving records.      │
├─────────────────────┼──────────────────────┼─────────────────────────────────────────┤
│ Event Registration  │ Set                  │ Stores unique student registrations,    │
│                     │                      │ prevents duplicates, O(1) insertion.    │
├─────────────────────┼──────────────────────┼─────────────────────────────────────────┤
│ Library Borrowing   │ Graph/Dictionary     │ Tracks relationships between students   │
│                     │                      │ and books with due dates efficiently.   │
├─────────────────────┼──────────────────────┼─────────────────────────────────────────┤
│ Bus Scheduling      │ Priority Queue       │ Processes buses by route priority,      │
│                     │                      │ ensuring timely departure management.   │
├─────────────────────┼──────────────────────┼─────────────────────────────────────────┤
│ Cafeteria Order     │ Queue (FIFO)         │ Maintains order fairness; customers     │
│                     │                      │ served in arrival sequence, O(1) ops.   │
└─────────────────────┴──────────────────────┴─────────────────────────────────────────┘
"""

# Implementation: Attendance Tracking using Dictionary
class AttendanceSystem:
    def __init__(self):
        self.attendance = defaultdict(list)
    
    def mark_attendance(self, student_id, date, status):
        """Mark attendance for a student (Present/Absent)."""
        self.attendance[student_id].append({"date": date, "status": status})
        return True
    
    def get_attendance(self, student_id):
        """Retrieve attendance records for a student."""
        return self.attendance.get(student_id, [])
    
    def get_attendance_percentage(self, student_id):
        """Calculate attendance percentage."""
        records = self.attendance.get(student_id, [])
        if not records:
            return 0
        present = sum(1 for r in records if r["status"] == "Present")
        return (present / len(records)) * 100

# Implementation: Cafeteria Order Queue using Queue (FIFO)
class CafeteriaOrderQueue:
    def __init__(self):
        self.queue = deque()
        self.order_count = 0
    
    def place_order(self, customer_name, items):
        """Add a new order to the queue."""
        self.order_count += 1
        order = {
            "order_id": self.order_count,
            "customer": customer_name,
            "items": items,
            "timestamp": datetime.now()
        }
        self.queue.append(order)
        return order["order_id"]
    
    def process_order(self):
        """Process the next order in queue (FIFO)."""
        if self.queue:
            return self.queue.popleft()
        return None
    
    def get_queue_size(self):
        """Get current queue size."""
        return len(self.queue)

# Testing
if __name__ == "__main__":
    print("=== ATTENDANCE TRACKING SYSTEM ===\n")
    attendance = AttendanceSystem()
    attendance.mark_attendance("S001", "2024-01-10", "Present")
    attendance.mark_attendance("S001", "2024-01-11", "Present")
    attendance.mark_attendance("S001", "2024-01-12", "Absent")
    
    print(f"Student S001 Records: {attendance.get_attendance('S001')}")
    print(f"Attendance %: {attendance.get_attendance_percentage('S001'):.1f}%\n")
    
    print("=== CAFETERIA ORDER QUEUE ===\n")
    cafeteria = CafeteriaOrderQueue()
    cafeteria.place_order("Alice", ["Burger", "Fries"])
    cafeteria.place_order("Bob", ["Pizza", "Coke"])
    cafeteria.place_order("Charlie", ["Salad", "Water"])
    
    print(f"Queue size: {cafeteria.get_queue_size()}")
    print(f"Processing: {cafeteria.process_order()}")
    print(f"Queue size: {cafeteria.get_queue_size()}")