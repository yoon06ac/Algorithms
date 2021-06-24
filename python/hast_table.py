# m = Length of Hash Table
# n = Total keys to be inserted in the hash table
 
# Load factor lf = n/m 
# Expected time to search = O(1 +lf )
# Expected time to insert/delete = O(1 + lf)

# The time complexity of search insert and delete is 
# O(1) if  lf is O(1)

# Function to display hashtable
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
# Creating Hashtable as 
# a nested list.
HashTable = [[] for _ in range(10)]
  
# Hashing Function to return 
# key for every value.
def Hashing(keyvalue):
    return keyvalue % len(HashTable)
  
  
# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
      
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)