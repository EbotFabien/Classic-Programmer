from time import sleep
class HashTable:
  
    def __init__(self):
        self.size = 30
        self.hashmap = [[] for _ in range(0, self.size)]
        # print(self.hashmap)

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break

        if key_exists:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hash_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                return print('No value')

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)



H = HashTable()
while 1:
    Setkey=input('Input Word to be searched \n List of them:\nimpeachment\nMarlian\nFast\nMarlian\n')
    H.set('impeachment','the action of calling into question the integrity or validity of something')
    H.set('Marlian','Free thinker')
    H.set('Astonished','Greatly surprised or impressed; amazed.')
    H.set('Hell','A situation, experience, or place of great suffering.')

    H.set('Fast','moving or capable of moving at high speed')
    H.set('Slow', 'moving or operating, or designed to do so, only at a low speed; not quick or fast.')

    H['Home'] = 'A place to be'

    print(H.get(Setkey))
    sleep(2)

    #print(H.hashmap)
