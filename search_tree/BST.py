'''
=========================================
We implement the Binary Search Tree class
with the least computational power
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
    
    def inorderTraversal(self, root): 
        result = [] 
        if root: 
            result = self.inorderTraversal(root.leftChild)
            result.append(root.data)
            result = result + self.inorderTraversal(root.rightChild)
        return result

'''
=============================================
'''

list1 = [7,4,5,3,1,8,6,10] 

myBST = BinarySearchTree()
for x in list1:
    myBST.insert(x) 

r = myBST.inorderTraversal(myBST.root)
print(r)   



#AVL tree and B+ tree ensures that the height remains O(log base 2 (n)) --> perfect height 
