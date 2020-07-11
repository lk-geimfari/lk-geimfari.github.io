---
layout: post
title: Note about comments and dead code
date: 2020-07-05
description: Comments are something that can both&colon; ruin your code and make it better.
web_preview_image: caspar-the-stages-of-life.jpg
---

Comments are something that can both: ruin your code and make it better. 

A good comment takes time to think and write, and therefore most often we all come across 
disgusting comments that are nothing but a piece of visual garbage.

Let's consider a small example from JavaScript:

```javascript
// Remove first five letters
const errorCode = errorText.substr(5)
```

The first thought that flashes in your head when you see this is “Thank you, cap!”. 
Why should we describe things that are already clear without comment? Why should we duplicate the information 
that the code already tells us? 

This distinguishes a good comment from a bad one - a good comment makes you feel grateful for the 
developer who wrote it when a bad comment just annoys you as hell.

Let's try to make this comment a little useful:

```javascript
// Remove "net::" from the error text
const errorCode = errorText.substr(5)
```

Better yet, resort to a more declarative approach and opt-out the comment:

```javascript
const errorCode = errorText.replace('net::', '')
```

## Dead code

Dead code, perhaps, is much more annoying than useless comments, since you also have to figure out was the code commented out 
temporarily (to debug some parts of the system or something), or did the developer just forget to delete it?

Be that as it may, dead code has no place in the modules and it should be deleted! If it suddenly turns out that 
this was something important, then you can just roll back to the correct version (unless, of course, you are 
something like an Amish programmer that does not use the version control system).
