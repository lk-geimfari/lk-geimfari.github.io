---
layout: post
title: "EAFP, LBYL... WTF?"
date: 2023-08-06
preview_img: eafp-lbyl.png
description: "The purpose of this article is to discuss two opposing approaches to writing code: EAFP and LBYL."
published: true
starred: false
---

The purpose of this article is to discuss two opposing approaches to writing
code: [EAFP](https://docs.python.org/3/glossary.html#term-EAFP)
and [LBYL](https://docs.python.org/3/glossary.html#term-LBYL). 
There is no need for a long introduction, so let's dive in.

## The Problem

Suppose we have received a response from an API call, with following structure:

```python
response = {
    "data": {
        "id": 241332,
        "recipient": {
            "city": "Palo Alto",
            "country": "US",
            "address": "1 Infinite Loop",
            "postal_code": "12345",
            "state": "CA",
            "name": "Tim Cook",
            "phone": "+1234567890",
            "email": "tcook@apple.com"
        },
        "cost": 1099.00,
        "currency": "USD",
        "name": "Google Pixel 7 Pro",
        "quantity": 1,
        "color": "Obsidian",
        "capacity": "512GB"
    }
}
```

Our goal is to retrieve the `email` of the recipient. We assume that any field may be missing to add complexity.

## Look Before You Leap

The *LBLY* states that you should check for preconditions before performing any actions (like calling functions,
accessing dictionary keys, or object attributes).

Just like this:

```python
def get_user_email(response: dict) -> str | None:
    data = response.get('data')
    if data:
        recipient = data.get('recipient')
        if recipient:
            return recipient.get('email')
    return None
```

This approach is the most commonly used in programming, but it can also result in a lot of repetitive and unnecessary
code, which can be challenging to maintain.

So, why not attempt to access the key and handle the exception if it doesn't exist? This is precisely where *EAFP* comes
into play.

## Easier to Ask Forgiveness than Permission

The *EAFP* states that it's simpler to perform an action and then handle error, instead of checking all necessary
conditions beforehand.

Example:

```python
def get_user_email(response: dict) -> str | None:
    try:
        return response['data']['recipient']['email']
    except KeyError:
        return None
```

One essential thing to bear in mind is that we should always catch the most specific exception available. In this
example, we are catching a `KeyError` exception, which is raised when a dictionary key is not found. If we catch a
general `Exception` we may inadvertently catch exceptions that we weren't expecting, leading to unexpected behavior.

## Conclusion

Neither of these approaches is superior to the other. Both approaches have their pros and cons, and the
choice of which one to use and when ultimately depends on the specific requirements and context of the program.

That’s all for today. See you next time!
