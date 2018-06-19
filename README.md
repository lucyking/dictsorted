## DictSorted
sort object dict()'s key || value, return in list container.

## Install
```pip install dictsorted```

## Usage

```
import dictsorted as d

t = d.DictSorted({2:4, 1:3})
print(t.sortedKey())
print(t.sortedVal())
```
output:
>[1, 2]
>[3, 4]