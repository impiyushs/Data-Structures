"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        x=self.calculate_hash_value(string)
        if self.table[x] is None:
            self.table[x]=[string]
        else:
            self.table[x].append(string)

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        x=self.calculate_hash_value(string)
        if self.table[x] is not None:
            if string in self.table[x]:
                return x
        return -1
        

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return (ord(string[0])*100+ord(string[1]))
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UTD')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UTD')

# Test store
hash_table.store('UTD')
# Should be 8568
print hash_table.lookup('UTD')

# Test store edge case
hash_table.store('UTDALLAS')
# Should be 8568
print hash_table.lookup('UTDALLAS')
