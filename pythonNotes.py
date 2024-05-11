## Python Counter
'''
In Python, `Counter` is a subclass of `dict` provided by the `collections` module. It is used to count the occurrences of 
elements in an iterable (e.g., list, tuple, string) and store them as key-value pairs, where the key is the element being counted, 
and the value is its count.

Here's how you can use `Counter`:

'''
from collections import Counter

# Create a Counter object from a list
my_list = [1, 2, 3, 1, 2, 1, 3, 4, 5]
my_counter = Counter(my_list)

print(my_counter)


'''
This will output:

```
Counter({1: 3, 2: 2, 3: 2, 4: 1, 5: 1})
```

In this example:

- We import `Counter` from the `collections` module.
- We create a list `my_list` with some elements.
- We create a `Counter` object `my_counter` by passing `my_list` to the `Counter()` constructor.
- The `Counter` object `my_counter` contains the counts of each unique element in `my_list`.

You can also use `Counter` with other iterable types, such as strings or tuples:
'''

my_string = 'hello'
my_counter = Counter(my_string)
print(my_counter)
# Output: Counter({'h': 1, 'e': 1, 'l': 2, 'o': 1})

'''
`Counter` objects have several useful methods for working with counts, such as `most_common()` 
to get the most common elements, arithmetic operations like addition and subtraction, and more.
'''




### Deafualt Dict python
'''


In Python, collections.defaultdict is a subclass of the built-in dict class that provides a default value for 
keys that haven't been explicitly set. It is particularly useful when working with dictionaries and dealing with missing keys, 
as it eliminates the need for explicit checks for key existence.

Here's how you can use collections.defaultdict:
'''

from collections import defaultdict

# Create a defaultdict with default value 0
my_dict = defaultdict(int)

# Increment the count for key 'a'
my_dict['a'] += 1

# Accessing a missing key returns the default value (0 in this case)
print(my_dict['b'])  # Output: 0

# Print the defaultdict
print(my_dict)  # Output: defaultdict(<class 'int'>, {'a': 1, 'b': 0})


'''
In this example:

We import defaultdict from the collections module.
We create a defaultdict named my_dict with a default value of int, which is 0. This means that accessing a 
missing key will return 0 without raising a KeyError.
We increment the count for key 'a'.
When we access the missing key 'b', it returns the default value 0.
Finally, we print the defaultdict, showing that the key 'b' has been added with the default value 0.
You can use any valid Python object as the default value, such as list, set, str, etc. This makes collections.defaultdict 
very versatile and useful in various situations where you need a default value for missing keys.
'''