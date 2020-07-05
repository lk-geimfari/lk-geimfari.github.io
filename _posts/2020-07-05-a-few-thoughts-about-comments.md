---
layout: post
title: About useful and not so comments
date: 2020-07-05
description: A teeny-tiny post about comments in code.
---

Comments are something that can both: ruin our code and make it better. 
A good comment takes time to think and write, and therefore most often we all come across 
disgusting comments that are nothing but a visual piece of garbage.

Let's consider a small example from JavaScript:

```javascript
// Remove first five letters
const errorCode = errorText.substr(5)
```

The first thought that flashes in your head when you see this is “Thank you, cap!”. 
Why describe what is already clear without comment? Why should we duplicate the information 
that the code already tells us? 

This distinguishes a good comment from a bad one - a good comment makes you feel grateful to 
the developer who wrote it, and a bad comment only annoys you.

Let's try to make this comment useful:

```javascript
// Remove "net::" from error text
const errorCode = errorText.substr(5)
```

Better yet, resort to a more declarative approach and opt-out the comment:

```javascript
const errorCode = errorText.replace('net::', '')
```

Speaking of comments, one can't help but mention the dead code. Dead code, perhaps, is much more annoying 
than useless comments, since you also have to understand if the code was commented out 
temporarily (to debug some parts of the system or something), or did the developer just forget to delete it?

Be that as it may, dead code has no place in the modules and it must be deleted! If it suddenly turns out that 
this was something important, then you can just roll back to the correct version (unless, of course, you are 
something like an Amish programmer that does not use the version control system).
