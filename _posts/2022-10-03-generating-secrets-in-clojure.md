---
layout: post
title: Generating secrets in Clojure.
date: 2022-10-03
preview_img: clojure-secrets.png
description: Let's talk about how to generate cryptographically strong secrets in Clojure.
published: true
comments: false
---

Generating secrets is a very important part of any application. In this article, I'm going to tell you about secrets in Clojure.

If you're familiar with Python, you might have heard of [`secrets`](https://docs.python.org/3/library/secrets.html) module from Python's standard library.

Well, the `secrets.clj` is just like Python's secrets, but for Clojure.

It is used to produce CSPRNG i.e, cryptographically strong pseudo-random numbers that are secure and useful in security-sensitive 
applications.

Typical use cases are:

- Generating random numbers
- Creating passwords and OTP
- Generating random tokens
- Generating password recovery URLs and session keys

## Installation

Import `secrets.clj` in your project.clj file:

```clojure
[likid_geimfari/secrets "1.1.1"]
````

then run `lein deps` to install it. That's it, you're ready to go.


## Usage

#### secrets.core/randbelow(n)

This function generates a secure random integer in the range `[0, n)`, where `n` is the exclusive upper bound.

Example: 

```clojure
user=> (secrets.core/randbelow 9999)
34
```

#### secrets.core/choice(seq)

This function returns a random element from a non-empty sequence or throws an exception if the sequence is empty.

```clojure
user=> (secrets.core/choice ["bob" "alice" "eve"])
"eve"
```

#### secrets.core/choices(seq)

Just like `secrets.core/choice`, but this function returns a list of random elements picked from the sequence:

```clojure
(secrets.core/choices ["bob" "alice" "eve"] 2)
("eve" "alice")
```

#### secrets.core/token-hex(nbytes)

Generates a secure random string in hexadecimal format. The string has `nbytes` random bytes, and each byte is converted to two hex digits. 
If n-bytes are not supplied, a reasonable default gets used, which is 32.

```clojure
user=> (secrets.core/token-hex(64))
"3a3e8e6636000dd3b7d39aa4316935f27c2f013d768f0c00f309efb453f34dbc673060db2cd8af288494892848"
```

#### secrets.core/token-urlsafe(nbytes)

Generates a secure random string in URL-safe format.

```clojure
user=> (secrets.core/token-urlsafe(64))
"TItm04q8by00MRMcNBt7I3Yx-wSxyUa79isRLNyQJCd8K75RnqUahwcWA_rURBt1clknJiRGrubapGaUrEUnSw"
```

#### secrets.core/token-bytes(nbytes)

Generates a secure random string in bytes format.

```clojure
(secrets.core/token-urlsafe(16))
#object["[B" 0x3b2454e9 "[B@3b2454e9"]
```

#### How many bytes should tokens use?

To be secure against brute-force attacks, tokens need to have sufficient randomness. 
Unfortunately, what is considered sufficient will necessarily increase as computers get more powerful and able to make more guesses in a shorter period. 

I would recommend using at 64 bytes (512 bits).