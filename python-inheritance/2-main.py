#!/usr/bin/python3
is_same_class = __import__('2-is_same_class').is_same_class

print(is_same_class([], list))       # True
print(is_same_class([], object))     # False
print(is_same_class(5, int))         # True
print(is_same_class(5, float))       # False
