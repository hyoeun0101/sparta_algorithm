class LinkedTuple:
    def __init__(self) -> None:
        self.items = list()

    def add(self, key, value):
        self.itmes.append((key,value))

    def get(self, key):
        for k,v in self.items:
            if key == k:
                return v


class LinkedDict:
    def __init__(self) -> None:
        self.items = []
        for i in range(8):
            self.items.append(LinkedTuple())
            #[LinkedTupe(), LinkedTuple(),]

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key,value)
        # [(key,value)]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)