
class DictSorted(object):
    DICT = dict()

    def __init__(self, inputDict):
        self.DICT = inputDict

    def sortedKey(self):
        ret = sorted(self.DICT.items(), key=lambda e:e[0], reverse=False)
        return [key for key , value in ret]

    def sortedVal(self):
        ret = sorted(self.DICT.items(), key=lambda e:e[1], reverse=False)
        return [value for key , value in ret]

    def pop(self, i_value):
        for key in list(self.DICT):
            if self.DICT[key] == i_value:
                self.DICT.pop(key)
                return 200
        return 404

    def clear(self, i_value):
        length  = len(self.DICT)
        for key in list(self.DICT):
            if self.DICT[key] == i_value:
                self.DICT.pop(key)

        if length != len(self.DICT):
            return 200
        else:
            return 404

if __name__ == '__main__':
    sd = DictSorted({15: 2, 10: 2, 1: 2, 13: 2, 3: 4, 12356: 4566, 5645: 5454888, 466: 5646, 8888:5645, 10086:5645})
    ret = sd.sortedKey()
    print(ret)
    reet = sd.sortedVal()
    print(reet)

    print("sssss")
    print(sd.DICT)

    ret3 = sd.pop(2)
    print(ret3)
    print(sd.DICT)

    ret3 = sd.pop(2)
    print(ret3)
    print(sd.DICT)

    ret3 = sd.clear(5645)
    print(ret3)
    print(sd.DICT)

    print("eeeeeee")
