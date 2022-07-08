<h1>OrderedDict()</h1>

```
popitem(last=True) / popitem(last=False)
```

Returns and removes a (key, value) pair. The pairs are returned in LIFO order if last is true or FIFO order if false.

```
move_to_end(key, last=True)
```

Move an existing key to either end of an ordered dictionary. The item is moved to the right end if last is true (the default) or to the beginning if last is false. Raises KeyError if the key does not exist.

