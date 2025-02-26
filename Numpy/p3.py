import numpy as np
a = np.array([1, 2, 3])
b = a.copy()  # Independent copy
b[0] = 10
print(a)  # Output: [1 2 3] (unchanged)
print(b)  # Output: [10 2 3] (changed)

# view
"""A view is a new array object that shares the same data as the original array.
Changes made to the view affect the original array.
Created using .view(). """

c = a.view()
print(c)
c[0] = 10
print(a)  # Output: [10 2 3] (affected)
print(c)  # Output: [10 2 3] (same as original)


# base
print(c.base is a)  # Output: True (c is a view of a)
print(b.base is a)

d = b.view()
d[1] = 20
print(d)
print(d.base is b)