class QueueNode: 
    def __init__(self, data):
        self.data = data
        self.next = None

'''
================================================
We implement the queue similar to the linked list 
The front is the first node of the linked list 
The rear is the last node of the linked list 
================================================
'''        
class Queue: 
    def __init__(self):
        self.front = None
        self.rear = None 
        self.size = 0 

    def enqueue(self,data):
        newNode = QueueNode(data)
        # enqueue when the queue is empty
        if self.front == None:  
            self.front=newNode 
            self.rear=newNode
        # enqueue when the queue is not empty 
        else:
            self.rear.next=newNode 
            self.rear = newNode 
        self.size += 1
 
    def dequeue(self):
        # if que is empty, cannot dequeue, return None 
        if self.front == None:  
            return None 
        else: 
            data = self.front.data 
            self.front = self.front.next
            if self.front == None:
                self.rear = None 
            self.size -= 1 
            return data 
 
    def printNode(self):
        curr = self.front
        while curr:
            print(curr.data)
            curr = curr.next 

myqueue = Queue() 
myqueue.enqueue(3)
myqueue.enqueue(5)
myqueue.enqueue(9)
myqueue.dequeue()
myqueue.enqueue(10)
myqueue.dequeue()
myqueue.printNode()

