'''
Lab 3 Task 3
'''


'''
=========================================
We first implement the queue clsss
=========================================
'''

class QueueNode: 
    def __init__(self, data):
        self.data = data
        self.next = None

'''
We implement the queue similar to the linked list 
The front is the first node of the linked list 
The rear is the last node of the linked list 
'''        
class Queue: 
    def __init__(self):
        self.front = None
        self.rear = None 
        self.size = 0 

    def enqueue(self,data):
        newNode = QueueNode(data)  
        if self.front == None:
            self.front=newNode 
            self.rear=newNode 
        else:
            self.rear.next=newNode 
            self.rear = newNode 
        self.size += 1
 
    def dequeue(self):  
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


'''
=========================================
Then we implement the Binary Search Tree clsss
=========================================
'''

class BSTNode: 
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 
        
class BinarySearchTree:  
    def __init__(self): 
        self.root = None  
        self.size = 0

    def insert(self,data): 
        # create a new node 
        newNode = BSTNode(data)
        
        # inser the new node into the binary search tree
        
        # if the tree is empty, the new node is set as root.
        if self.root == None:   
            self.root=newNode 
            self.size+=1
            return
        # if the tree is not empty, we try to find the 
        # value of of the input data in the BST 
        # if the input data is already in the BST, do nothing
        # if we can not find the input data in the BST, 
        # insert the new node at the empty node we reached.   
        curr=self.root
        while curr:
            # if data exists in the tree already, do nothing, return 
            if newNode.data == curr.data:
                return
            # if data is larger than the current node data,
            # go to right child, if right child is empty, insert node. 
            elif newNode.data > curr.data: 
                if curr.rightChild != None: 
                    curr = curr.rightChild
                else:
                    curr.rightChild = newNode
            # if data is smaller than the current node data,
            # go to left child, if left child is empty, insert node. 
            else:  
                if curr.leftChild != None: 
                    curr = curr.leftChild
                else:
                    curr.leftChild = newNode  
        self.size+=1
        return 
    
    def levelorderTraversal(self): 
        result = [] 
        myqueue = Queue() 
        curr = self.root
        if curr != None: 
            myqueue.enqueue(curr) 
        while myqueue.front: 
            curr = myqueue.dequeue() 
            result.append(curr.data) 
            if curr.leftChild != None:
                myqueue.enqueue(curr.leftChild)
            if curr.rightChild != None:
                myqueue.enqueue(curr.rightChild)  
        return result

'''
=============================================
'''
                
list1 = [7,4,5,3,1,8,6,10] 

myBST = BinarySearchTree()
for x in list1:
    myBST.insert(x) 

r = myBST.levelorderTraversal()
print(r)  

