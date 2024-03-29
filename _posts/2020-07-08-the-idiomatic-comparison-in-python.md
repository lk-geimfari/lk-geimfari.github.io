---
layout: post
title: "The Idiomatic Comparison in Python"
date: 2020-07-08
preview_img: comparison_preview.jpg
description: "Let's talk about the fundamental difference between comparison operators."
published: true
redirect_from: /2020/07/08/the-idiomatic-comparison-in-python/
---

Some newbies in Python often improperly use the operators `is` and `==` without knowing how 
exactly they work and when to use each one. In this article, I'll talk about the difference between 
them, and about the use cases of each one.

Spoiler: the main difference is that `is` compares IDs of objects to check if both the operands 
refer to the same object and cannot be overloaded, when `==` compares the values of the objects 
and can be overloaded using the magic method `__eq__`.


Have a look at this code:

```python
>>> a = []
>>> b = []
>>> a == b # a.__eq__(b)
True
>>> a is b
False
```

That's right  `a` is not `b`, and here is why:

```python
>>> a_id = id(a)
4464140992
>>> b_id = id(b)
4465176960
>>> a_id == b_id
False
```

## Use case of «is»

Using operator `is` makes sense when you want to compare variable with a singleton-object, 
like `None`, `Ellipsis` and so on:

Good:

```python
if some_object is Ellipsis:
    do_some_stuff()
```

Still, good:

```python
if some_object is not None:
    do_other_stuff()
```

Bad (even it will work correctly, because `None` always equal to `None`):

```python
if some_object == None:
    do_some_stuff()
```

It's better to write it like this:

```python
if not some_object:
    do_some_stuff()
```

or like this:

```python
if some_object is None:
    do_some_stuff()
```


## Use case of «==»

Using operator `==` makes sense when you interested in comparing the values of objects:

```python
>>> a = []
>>> b = []
>>> a == b # [].__eq__([])
True
>>> c = 'isaak'
>>> d = 'Isaak'
>>> c == d.lower()
```

Keep in mind, that by default the magic method `__eq__` inherited from `object` compares 
IDs of objects (because it knows nothing about values).

You can read more about `__eq__` [here](https://docs.python.org/3/reference/datamodel.html).

## Summary

- Use `is` when you compare variable with a singleton-object.
- Use `==` when you want to compare the values of the objects.
