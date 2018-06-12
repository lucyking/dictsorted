import multidict

for i in range(0, 100, 5):
    print(i)
d = dict()
d[100] = 50
d [123] = 16

for item in d:
    print(item, ":", d[item])


bSortList = [9,8,7,6]
bSortList.sort()
print(bSortList)
#multidict sort############################

md = multidict.MultiDict()
md.add('10',100)
md.add('10', 10)
md.add('10', 50)
print(md)
#############################
list_dict = list()
list_dict.append({10:100})
print(list_dict)
print(type(list_dict[0]))
list_dict.append({10:15})
list_dict.append({10:50})


#ojbk ############################
d =  dict()
d[66666] = 100
d[66667] = 50
d[66668] = 60
d[66669] = 15
d[66670] = 102
ret = sorted(d.items(), key=lambda e:e[1], reverse=False)
print(ret)
print([value for key , value in ret])
ret = sorted(d.items(), key=lambda e:e[0], reverse=False)
print(ret)
print([key for key , value in ret])
#ojbk  class############################

class SortedDict(object):
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


sd = SortedDict({15: 2, 10: 2, 1: 2, 13: 2, 3: 4, 12356: 4566, 5645: 5454888, 466: 5646, 8888:5645, 10086:5645})
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
