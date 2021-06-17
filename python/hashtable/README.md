# Hashtables
Hashtable is a type of data structure that implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found.

## Challenge

Create a HAshmap class to and implement the methods add, get , contain to it and test them.

## Approach & Efficiency
- Fetch the index corresponding to the input key using the helper function
- The traversal of the linked list similar to in get() but what is special here is that one needs to remove the key along with finding it and two cases arise
- If the key to be removed is present at the head of the linked list
- If the key to be removed is not present at the head but somewhere else

Efficiency for hashmapping is : Time O(1) 

## API
- Create a new HashTable

ht = HashTable()

- Create some data to be stored

phone_numbers = ["555-555-5555", "444-444-4444"]

- Insert our data under the key "phoneDirectory"

ht.insert("phoneDirectory", phone_numbers)

- Do whatever we need with the phone_numbers variable

phone_numbers = None
... - Later on...

- Retrieve the data we stored in the HashTable

phone_numbers = ht.find("phoneDirectory")

- find() retrieved our list object

- phone_numbers is now equal to ["555-555-5555", "444-444-4444"]