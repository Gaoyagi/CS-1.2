#!python

from linkedlist import LinkedList


class HashTable(object):
    #initializer function (constructor) for new hashtable (a new list of linked lists)
    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    #prints a hash table bucket
    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    #prints out hash table in string format
    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    #hashing function
    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    #creates an list that holds all the keys in the hashtable
    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []   #creates key's list
        #loops through all the hashtables buckets
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Collect all values in each bucket
        values = []
        for bucket in self.buckets:
            for _, value in bucket.items():
                values.append(value)
        return value

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        entries = 0
        for bucket in self.buckets:
            entries+=len(bucket.items())
        return entries

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        keys = self.keys()
        if key in keys:
            return True
        else:
            return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = _bucket_index(key)      
        #check if the key exists in the hashtable
        if self.buckets[index] == None:
            raise KeyError('Key not found: {}'.format(key))
        #loop through the hashtable's bucket by key and value
        for k, value in self.buckets[index].items():
            #check if the key matches the desired one
            if key == k:
                return value    #return the current value if the keys match
        raise KeyError('Key not found: {}'.format(key))     #if nothing is found

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = _bucket_index(key)
        entry =  {key: value}
        if self.buckets[index] == None:
            self.buckets[index].head.data = Node(entry)
            self.buckets[index].tail = self.buckets[index].head.data
        else:
            self.buckets[index].tail.next = Node(entry)
            self.buckets[index].tail = self.buckets[index].tail.next

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = _bucket_index(key)
        if self.buckets[index] == None:
            raise KeyError('Key not found: {}'.format(key))
        iterate = self.buckets[index].head
        while iterate.next != None:
            if iterate.data
        raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()