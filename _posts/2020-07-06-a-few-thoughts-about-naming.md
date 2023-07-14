---
layout: post
title: Thoughts on naming
date: 2020-07-06
description: Properly naming variables, functions, methods, and classes is one of the most important attributes of elegant and clean code. It reflects the programmer’s intentions clearly, without leaving room for assumptions about what was meant.
preview_img: caspar-david-friedrich-der-einsame-baum.jpg
published: true
starred: true
redirect_from: /2020/07/a-few-thoughts-about-naming
---

Properly naming variables, functions, methods, and classes is one of the most important attributes of elegant and clean code. It reflects the programmer’s intentions clearly, without leaving room for assumptions about what was meant.

In this article, we will discuss code that is the exact opposite of what we just described - code that was written carelessly or thoughtlessly. This article is a small confession, because like any other programmer, I have also written such code in the past (in fact, I still write bad code sometimes, although refactoring makes it much better). This is nothing terrible as long as we understand that we need to work on it.

This article is a translated version of my article from [harb.com](https://habr.com/ru/post/508238/) so, 
if you know Russian then you can read the original version.

Let's start.

## Variables

One of the most annoying types of variables are those that give a false impression of the nature of the data they store.

The `requests` library is extremely popular among Python developers, and if you have ever looked for anything 
related to `requests`, you must have come across something like this:

```python
import requests

req = requests.get('https://api.example.org/endpoint')
req.json()
```

Whenever I see this, I feel annoyed, not only because of the shortened name but also because the variable's 
name does not match what is stored in it.

When you make a request (`requests.Request`), you get a response (`requests.Response`), 
so reflect this in your code:

```python
response = requests.get('https://api.example.org/endpoint')
response.json()
```

Not `r`, not `res`, not `resp` and certainly not `req`, exactly `response`. `res`, `r`, `resp` – these are all 
variables whose contents can be understood only by looking at their definitions, and why jump to the definitions 
when you can initially give a suitable name?

Let's look at another example, but now from Django:

```python
users_list = User.objects.filter(age__gte=22)
```

When you see `users_list` somewhere in the code, you quite rightly expect that you can do this:

```python
users_list.append(User.objects.get(pk=3))
```

but no, you can't do this, since `.filter()` returns a `QuerySet`:

```python
Traceback (most recent call last):
# ...
# ...
AttributeError: 'QuerySet' object has no attribute 'append'
```

If it is very important for you to specify a suffix, then specify at least one that reflects the real situation:

```python
users_queryset = User.objects.all()
users_queryset.order_by('-age')
```

also okay, because such abbreviations (`_qs`) are usual for Django:

```python
users_qs = User.objects.all()
```


If you really want to write exactly `_list`, then take care that the `list` really gets into the variable:

```python
users_list = list(User.objects.all())
```

Indicating a type of data that a variable contains is often a bad idea, especially when you deal with 
dynamic languages, such as Python. In cases when it is very necessary to note that the object is a 
container data type, it is enough to simply indicate the name of the variable in the plural:

```python
users = User.objects.all()
```

Consider another example:

```python
info_dict = {'name': 'Isaak', 'age': 25}
# ...
# ... 
info_dict = list(info_dict)
# ...
# ...
```

You see a `dict` and you might want to do this:

```python
for key, value in info_dict.items():
    print(key, value)
```

Instead, you'll get an exception, because you were misled, and you will understand this only 
if you go to the definition of the variable and read the entire code from top to bottom,
right down to the section from which you started the jump — this is the price of such variables.
 
Thus, when you indicate in the variable name the type of data stored in it, you are essentially a 
guarantee that this variable must contain the specified data type at any time during the execution of the program. 
Why should you take this responsibility if it is the direct responsibility of the interpreter or compiler? 
You shouldn't! Better to spend time thinking of a good variable name than trying to figure out why the 
variables do not behave as you expect.

In the example above, the choice of the name of a variable is rather bad, and you could give a 
name that more accurately expresses the context (no need to be afraid to use the domain-specific names),
but even in this case, you could make this code better:

```python
info_dict = {'name': 'Isaak', 'age': 25}
# ...
# ... 
info_keys = list(info_dict)
# ...
# ...
```

or even like this, which is more idiomatic:

```python
info_dict = {'name': 'Isaak', 'age': 25}
# ...
# ... 
info_keys = info_dict.keys()
# ...
# ...
```

Another type of annoying variable is ones with a shortened name.

Let's go back to `requests` and consider this code:

```python
s = requests.Session()
# ...
# ... 
s.close()
```

This is an example of an unnecessary shortening for a variable name. 
This is a terrible practice, and its horror becomes even more apparent when such code 
takes up more than 10-15 lines of code.

It is much better to write as is, namely:

```python
session = requests.Session()
# ...
# ...
session.get('https://api.example.org/endpoint')
# ...
# ...
session.close()
```

or 

```python
with requests.Session() as session:
    session.get('https://api.example.org/endpoint')
```

You may argue that this is a more verbose option, but I will answer you that it pays off when 
you read the code and immediately understand that `session` is a `Session`. 

Will you understand it by variable `s` without looking at its definition?


## Methods

Smart naming of functions and methods is something that comes only with experience in designing an API,
and therefore you can often find cases where methods do not behave as you expect.

Consider an example:

```python
>>> person = Person()
>>> person.has_publications()
['Post 1', 'Post 2', 'Post 3']
```

We expressed a very clear-cut question in our code: “Does this person have publications?”, 
but what kind of answer did we get? Did we ask for a list of publications of a person?

The name of this method implies that the return value must be of Boolean type, namely `True` or `False`:

```python
>>> person = Person()
>>> person.has_publications()
True
```

We can use a more appropriate method name for getting publications:

```python
>>> person.get_publications()
['Post 1', 'Post 2', 'Post 3']
```

or

```python
>>> person.publications()
['Post 1', 'Post 2', 'Post 3']
```

We often like to call programming a creative activity, and it really is. 
However, if you write not readable code, and then justify it with “creativity”, then I have bad news for you.


## Further reading

I'm leaving this  list of outstanding relevant literature written by well-known 
professionals in the field for further study of the issue:

1. Robert Martin — [Clean Architecture](https://amzn.to/2VLWw7S)
2. Martin Fowler — [Refactoring: Improving the Design of Existing Code](https://bit.ly/2NTEaOa)
