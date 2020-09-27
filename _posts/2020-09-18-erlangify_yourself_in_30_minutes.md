---
layout: post
title: Erlangify Yourself: Part I. Primitives.
published: false
comments: false
---

![carbon](https://user-images.githubusercontent.com/15812620/91530751-556c4c80-e914-11ea-8b2d-17a2d11a22bb.png)

### About Erlang

Erlang is a programming language used to build massively scalable soft real-time systems with requirements on high 
availability. Some of its uses are in telecoms, banking, e-commerce, computer telephony and instant messaging. 
Erlang's runtime system has built-in support for concurrency, distribution and fault tolerance.

You can read more about Erlang on [https://erlang.org/]()

### Installation

macOS

```
~ brew install erlang
```

Ubuntu:

```
~ apt install erlang
```

then just run shell:

```bash
~ ⟩ erl
Erlang/OTP 23 [erts-11.0.3] [source] [64-bit] [smp:4:4] [ds:4:4:10] [async-threads:1] [hipe] [dtrace]

Eshell V11.0.3  (abort with ^G)
```

### Comments

Percent sign in Erlang starts a one-line comment:

```erlang
1> % One-line comment
```

There are no multi-line comments in Erlang, so use usual comments on each line of a multiline comment block, like this:

```erlang
%% Author: Isaak
%% Copyright 2020-2030
%% Something else

http_ok () -> {ok, 200}.
```

### Punctuation

The most confusing thing for newbies in Erlang is its punctuation: commas (`,`), periods (`.`) and semicolons (`;`).

So let's figure out when to use each one:

* Commas (`,`) separate arguments in function calls, data constructors, and patterns.
* Periods (`.`) separate entire functions and expressions.
* Semicolons (`;`) separate clauses in several contexts: function definitions, `case`, `if`, `try/catch`, and `receive` expressions.

You will see examples next.

### Variables, Pattern-matching and Data Structures

First thing you need to know about variables is that in Erlang **variable names must always start with a capital letter**:

```erlang
1> Pi = 3.14.
3.14
```

Always keep in mind that **expressions ends with a period**, otherwise you're continuing expression:

```erlang
1> Pi = 3.14
1> Pi - 1
1> .
* 2: syntax error before: Pi
1>
```

Erlang **does not have variable assignment** in the usual sense, instead variables are bound to values through the 
pattern matching mechanism. In a pattern matching, a left-hand side (`Lhs`) pattern is matched against a right-hand
 side (`Rhs`) term (value). If the matching succeeds, any unbound variables in the pattern become bound.

```erlang
1> Year.
* 1: variable 'Year' is unbound
2> Year = 2020.
2020
```

If the matching fails, a run-time error occurs:

```erlang
3> Year = 2021.
** exception error: no match of right hand side value 2021
```

Atoms are literals, the constants with a name that represents its value. Atoms start with lowercase letters, 
followed by a sequence of alphanumeric characters or the underscore (`_`) or at (`@`) sign:

```erlang
1> Hello = world.
world
2> Node = example@node.
example@node
```

An atom is to be enclosed in single quotes (') if it does not begin with a lower-case letter or if it contains other 
characters than alphanumeric characters, underscore (_), or @:

```erlang
1> Atom = 'my atom'.
'my atom'
```

A tuple is a compound data type with a fixed number of elements and they are similar to structs in `C`:

```erlang
1> Point = {point, 15, 35}.
{point,15,35}
```

You can extract elements of tuples using pattern-matching mechanism (an operator `=`):

```erlang
2> {point, X, Y} = Point.
{point,15,35}
3> X.
15
4> Y.
35
```

We can use `_` as a placeholder for anonymous variables. Unlike regular variables, several occurrences of `_` in the 
same pattern don’t have to bind to the same value:

```erlang
1> Person = {person, {name, john}}.
{person,{name,john}}
2> {_, {_, Name}} = Person.
{person,{name,john}}
3> Name.
john
```

You can create a list by enclosing the list elements in square brackets and separating them with commas:

```erlang
1> Numers = [1, 2, 3].
[1,2,3]
```

The individual elements of a list can be of any type:

```erlang
1> MixedList = [atom, 1, 3.14, {atom, []}].
[atom,1,3.14,{atom,[]}]
```

We call the first element of the list a `head` and the rest elements of the list as a `tail`. We use the vertical 
bar (`|`) to separate the head of a list from its tail:

```erlang
1> Countries = [switzerland, russia, germany, canada, austria].
[switzerland,russia,germany,canada,austria]
2> [Head|Tail] = Countries.
[switzerland,russia,germany,canada,austria]
3> Head.
switzerland
4> Tail.
[russia,germany,canada,austria]
```

This is shocking, but there is no separated data type for strings in Erlang. In Erlang, strings are just lists 
of integers:

```erlang
1> Name = "Hello".
"Hello"
[72, 101, 108, 108, 111] = "Hello".
```

The console shows some lists as strings (as above), and others as numbers:

```erlang
2> List = [1,2,3,4,5].
[1,2,3,4,5]
```

If Erlang sees that the list consists only of character codes, it displays it as a string. And if the list contains 
numbers that differ from the character codes, then it will be displayed as a list of numbers:

```erlang
3> [72, 101, 108, 108, 111].
"hello"
4> [72, 101, 108, 108, 1111].
[72,101,108,108,1111]
```

As most of functional programming languages, Erlang supports list comprehensions. List comprehensions are expressions 
that create lists without having to use funs, maps, or filters.

List comprehensions have notation `[F(X) || X <- L]`, which means "the list of `F(X)` where `X` is taken from the list `L`.

Let's look at example:

```erlang
1> L = [1, 2, 3].
2> [X * -1 || X <- L].
```
