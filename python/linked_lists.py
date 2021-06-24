data structures: Python

Linked Lists: 

	# Node class
	class Node:
	  
		# Function to initialize the node object
		def __init__(self, data):
			self.data = data  # Assign data
			self.next = None  # Initialize
							  # next as null
	  
	# Linked List class
	class LinkedList:
		
		# Function to initialize the Linked
		# List object
		def __init__(self):
			self.head = None
					
					
		# This function is in LinkedList class
		# Function to insert a new node at the beginning
		def push(self, new_data):
		 
			# 1 & 2: Allocate the Node &
			#        Put in the data
			new_node = Node(new_data)
				 
			# 3. Make next of new Node as head
			new_node.next = self.head
				 
			# 4. Move the head to point to new Node
			self.head = new_node
			
		
		# Inserts a new node after the given prev_node. This method is
		# defined inside LinkedList class shown above */
		def insertAfter(self, prev_node, new_data):
		 
			# 1. check if the given prev_node exists
			if prev_node is None:
				print "The given previous node must inLinkedList."
				return
		 
			# 2. Create new node &
			# 3. Put in the data
			new_node = Node(new_data)
		 
			# 4. Make next of new Node as next of prev_node
			new_node.next = prev_node.next
		 
			# 5. make next of prev_node as new_node
			prev_node.next = new_node
		
		
		# Appends a new node at the end.  This method is
		#  defined inside LinkedList class shown above */
		def append(self, new_data):
		 
		   # 1. Create a new node
		   # 2. Put in the data
		   # 3. Set next as None
		   new_node = Node(new_data)
		 
		   # 4. If the Linked List is empty, then make the
		   #    new node as head
		   if self.head is None:
				self.head = new_node
				return
		 
		   # 5. Else traverse till the last node
		   last = self.head
		   while (last.next):
			   last = last.next
		 
		   # 6. Change the next of last node
		   last.next =  new_node
			   
			   
		# Utility function to print the linked list
		def printList(self):
			temp = self.head
			while (temp):
				print temp.data,
				temp = temp.next
				
				
		# Given a reference to the head of a list and a key,
		# delete the first occurrence of key in linked list
		def deleteNode(self, key):
			 
			# Store head node
			temp = self.head
	 
			# If head node itself holds the key to be deleted
			if (temp is not None):
				if (temp.data == key):
					self.head = temp.next
					temp = None
					return
	 
			# Search for the key to be deleted, keep track of the
			# previous node as we need to change 'prev.next'
			while(temp is not None):
				if temp.data == key:
					break
				prev = temp
				temp = temp.next
	 
			# if key was not present in linked list
			if(temp == None):
				return
	 
			# Unlink the node from linked list
			prev.next = temp.next
	 
			temp = None
			
			
		# Given a reference to the head of a list
		# and a position, delete the node at a given position
		def deleteAtNode(self, position):
	 
			# If linked list is empty
			if self.head == None:
				return
	 
			# Store head node
			temp = self.head
	 
			# If head needs to be removed
			if position == 0:
				self.head = temp.next
				temp = None
				return
	 
			# Find previous node of the node to be deleted
			for i in range(position -1 ):
				temp = temp.next
				if temp is None:
					break
	 
			# If position is more than number of nodes
			if temp is None:
				return
			if temp.next is None:
				return
	 
			# Node temp.next is the node to be deleted
			# store pointer to the next of node to be deleted
			next = temp.next.next
	 
			# Unlink the node from linked list
			temp.next = None
	 
			temp.next = next
			
			
		# This function counts number of nodes in Linked List
		# iteratively, given 'node' as starting node.
		def getCount(self):
			temp = self.head # Initialise temp
			count = 0 # Initialise count
	 
			# Loop while end of linked list is not reached
			while (temp):
				count += 1
				temp = temp.next
			return count
			
			
		# This function counts number of nodes in Linked List
		# recursively, given 'node' as starting node.
		def getCountRec(self, node):
			if (not node): # Base case
				return 0
			else:
				return 1 + self.getCountRec(node.next)
 
 
	    # This Function checks whether the value
		# x present in the linked list
		def search(self, x):
	 
			# Initialize current to head
			current = self.head
	 
			# loop till current not equal to None
			while current != None:
				if current.data == x:
					return True # data found
				 
				current = current.next
			 
			return False # Data Not found
            
            
        # Returns data at given index in linked list
        def getNth(self, index):
            current = self.head  # Initialise temp
            count = 0  # Index of current node
     
            # Loop while end of linked list is not reached
            while (current):
                if (count == index):
                    return current.data
                count += 1
                current = current.next
     
            # if we get to this line, the caller was asking
            # for a non-existent element so we assert fail
            assert(false)
            return 0
            
        # recursive method to find Nth Node
        def getNthNodeRec(self, head, position, llist):
            count = 0  # initialize count
            if(head):
                if count == position:  # if count is equal to position,
                                      # it means we have found the position
                    print(head.data)
                else:
                    llist.getNthNode(head.next, position - 1, llist)
            else:  # if head doesn't exist we have
                  # traversed the LinkedList
                print('Index Doesn\'t exist')
 