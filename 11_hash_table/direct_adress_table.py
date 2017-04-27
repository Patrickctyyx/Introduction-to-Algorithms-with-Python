class Element:

    def __init__(self, key, info=None):
        self.key = key
        self.info = info


class DirectAddressTable:

    def __init__(self, size):
        self.size = size
        self.T = [None for _ in range(self.size)]

    def direct_access_search(self, k):
        return self.T[k]

    def direct_address_insert(self, x):
        self.T[x.key] = x

    def direct_address_delete(self, x):
        self.T[x.key] = None


if __name__ == '__main__':
    dat = DirectAddressTable(10)
    dat.direct_address_insert(Element(1, 'patrick'))
    dat.direct_address_insert(Element(9))
    dat.direct_address_insert(Element(5))
    print(dat.direct_access_search(1).info)
    dat.direct_address_delete(Element(5))
    print('end')
