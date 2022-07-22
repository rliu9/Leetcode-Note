# Time Complexity Cheet Sheet

| # | Problem |
|---|---------|
| ``` sort() ``` | O(nlogn) |
| ``` remove() ``` | O(n) |
| ``` reverse() ``` | O(n) |
| ``` bisect.insort(list,num) ``` | O(n) |

# functools

```
lru_cache
```


# random

```
random.sample(list, int)
```

returns multiple random elements from the list without replacement.


```
import random

l = [0, 1, 2, 3, 4]

print(random.sample(l, 3))
# [1, 3, 2]

random.sample(l, len(l)) -> shuffle a list

```

# Hashtable vs Hashmap

Hashtable is synchronized, whereas HashMap is not. This makes HashMap better for non-threaded applications.

Hashtable does not allow null keys or values. HashMap allows one null key and any number of null values.
