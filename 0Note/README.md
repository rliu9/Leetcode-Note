# Time Complexity Cheet Sheet

| # | Problem |
|---|---------|
| ``` sort() ``` | O(nlogn) |
| ``` remove() ``` | O(n) |
| ``` reverse() ``` | O(n) |
| ``` bisect.insort(list,num) ``` | O(n) |
| ``` heappop, heappush ``` | O(logn) |
| ``` heapify ``` | O(n) |

# functools

```
lru_cache
```

# Floating Point Arithmetic

```
format.(2, '.5f') #2.00000
```

# Tips
``` (n * (n+1)) // 2 ``` --- **Sum of [1, 2, ..., n]**

``` max(d, key=d.get) ``` --- **Dictionary d's key with highest value**

``` dict(sorted(dictionary.items(), key=lambda x:x[1])) --- ``` **Sort Dictionary by values**

``` eval('1 * 2') = 2 ``` ``` x,op,y = '2','+','3'; eval(f'{x} {op} {y}') = 5 --- ``` **Eval():Performs op passed as argument**

``` "{0:b}".format(int) == bin(int)[2:] ``` **Binary** ``` '{0:016b}'.format(int) ``` **16-digit binary string**

``` isalpha() ``` --- **only contains letters**

``` isalnum() ``` --- **contains alphanumeric characters, without symbols**

``` n & (n-1) ``` --- **remove rightmost set bit**

``` a & 0 = a ``` ``` a & a = 0 ``` --- **Bitwise AND Operator**

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
