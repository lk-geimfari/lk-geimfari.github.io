---
layout: post
title: "Python Libraries to Make Your Code Readable, Reliable and Maintainable"
date: 2020-08-24
description: "Experienced programmers understand perfectly well that in development they spend most of the time reading code 
             and therefore they treat the process of writing code with the deepest trepidation."
preview_img: rrm-post.png
published: true
starred: true
redirect_from: /2020/08/python-libraries-to-make-your-code-readable-and-maintainable
---

Experienced programmers understand perfectly well that in development they spend most of the time reading code 
and therefore they treat the process of writing code with the deepest trepidation (and sometimes with fanaticism). 
To write quality and maintainable code, you need to take the time to write tests and integrate QA tools. There is a 
whole technique aimed at test-driven development ([TDD]) and I will not devote this article to the topic of testing as 
such. Tests are absolutely necessary and there is nothing to discuss. In this article, we are going to talk about tools 
that help you write quality Python code.

[TDD]: https://en.wikipedia.org/wiki/Test-driven_development

Table of content:

 - [Testing Frameworks](#testing-frameworks)
 - [Test Runners](#test-runners)
 - [E2E Testing](#e2e-testing-gui--frontend)
 - [Fake Data](#fake-data)
 - [Mocking](#mocking)
 - [Code coverage](#code-coverage)
 - [Object Factories](#object-factories)
 - [Code Style](#code-style)
 - [Typing](#typing)

## Testing Frameworks

[**pytest**](https://github.com/pytest-dev/pytest/) is a framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. 

Features

- Detailed info on failing assert statements;
- Auto-discovery of test modules and functions;
- Modular fixtures for managing small or parametrized long-lived test resources;
- Can run `unittest` and nose test suites out of the box;
- `Python 3.5+` and `PyPy 3`;
- Rich plugin architecture, with over 315+ external plugins and thriving community;

<br>

[**Hypothesis**](https://github.com/HypothesisWorks/hypothesis)  is a family of testing libraries that let you write 
tests parametrized by a source of examples. A Hypothesis implementation then generates simple and comprehensible 
examples that make your tests fail. This simplifies writing your tests and makes them more powerful at the same time, 
by letting software automate the boring bits and do them to a higher standard than a human would, freeing you to focus 
on the higher-level test logic.

<br>

[**Robot Framework**](https://github.com/robotframework/robotframework) is a generic open-source automation framework 
for acceptance testing, acceptance test-driven development (ATDD), and robotic process automation (RPA). 
It has simple plain text syntax and it can be extended easily with libraries implemented using Python or Java.

<br>

[**unittest**](https://docs.python.org/3/library/unittest.html) is a unit testing framework from Python's stdlib, 
which was originally inspired by JUnit and has a similar flavor as major unit testing frameworks in other languages. 
It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, 
and independence of the tests from the reporting framework.

<br>

## Test Runners

[**tox**](https://github.com/tox-dev/tox) is aims to automate and standardize testing in Python. 
It is part of a larger vision of easing the packaging, testing and release process of Python software.

tox is a generic virtual environment management and test command line tool you can use for:

- checking your package builds and installs correctly under different environments (such as different Python
  implementations, versions or installation dependencies),
- running your tests in each of the environments with the test tool of choice,
- acting as a frontend to continuous integration servers, greatly reducing boilerplate and merging CI and shell-based
  testing.

<br>

## E2E Testing (GUI / Frontend)

[**Selenium**](https://github.com/SeleniumHQ/selenium/) is an umbrella project encapsulating a variety of tools and 
libraries enabling web browser automation. Selenium specifically provides an infrastructure for the W3C WebDriver 
specification — a platform and language-neutral coding interface compatible with all major web browsers.

<br>

[**Locust**](https://github.com/locustio/locust) is an easy to use, scriptable, and scalable performance testing tool.
 You define the behavior of your users in regular Python code, instead of using a clunky UI or domain-specific 
 language. This makes Locust infinitely expandable and very developer-friendly.

<br>

[**TestCafe**](https://github.com/DevExpress/testcafe) is a Node.js tool to automate end-to-end web testing. Write 
tests in JS or TypeScript, run them, and view results.

- **Works on all popular environments**: TestCafe runs on Windows, MacOS, and Linux. It supports desktop, mobile, remote and cloud [browsers](https://devexpress.github.io/testcafe/documentation/using-testcafe/common-concepts/browsers/browser-support.html) (UI or headless).
- **1 minute to set up**: You [do not need WebDriver](https://devexpress.github.io/testcafe/faq/#i-have-heard-that-testcafe-does-not-use-selenium-how-does-it-operate) or any other testing software. Install TestCafe with one command, and you are ready to test: `npm install -g testcafe`
- **Free and open source**: TestCafe is free to use under the [MIT license](https://github.com/DevExpress/testcafe/blob/master/LICENSE). [Plugins](#plugins) provide custom reports, integration with other tools, launching tests from IDE, etc. You can use the plugins made by the GitHub community or make your own.

<br>

[**PyAutoGUI**](https://github.com/asweigart/pyautogui) is a cross-platform GUI automation Python module for human beings. 
Used to programmatically control the mouse & keyboard.

<br>

## Fake Data

[**Mimesis**](https://github.com/lk-geimfari/mimesis) is a high-performance fake data generator for Python, which
provides data for a variety of purposes in a variety of languages. The
fake data could be used to populate a testing database, create fake API
endpoints, create JSON and XML files of arbitrary structure, anonymize
data taken from production and etc.

The key features are:

-   **Performance**: The [fastest][] data generator available for Python.
-   **Extensibility**: You can create your own data providers and use them with Mimesis.
-   **Generic data provider**: The [simplified][] access to all the providers from a single object.
-   **Multilingual**: Supports data for [a lot of languages][].
-   **Data variety**: Supports [a lot of data providers][] for a variety of purposes.
-   **Schema-based generators**: Provides an easy mechanism to generate data by the schema of any complexity.
-   **Country-specific data providers**: Provides data specific only for [some countries][].

  [fastest]: https://mimesis.name/foreword.html#performance
  [simplified]: https://mimesis.name/getting_started.html#generic-provider
  [a lot of languages]: https://mimesis.name/getting_started.html#locales
  [a lot of data providers]: https://mimesis.name/api.html
  [some countries]: https://mimesis.name/api.html#builtin-data-providers

<br>

## Mocking

[**unittest.mock**](https://docs.python.org/3/library/unittest.mock.html) is a library from Python's stdlib for mocking. 
It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

`unittest.mock` provides a core `Mock` class removing the need to create a host of stubs throughout your test suite. 
After performing an action, you can make assertions about which methods / attributes were used and arguments they
were called with. You can also specify return values and set needed attributes in the normal way.


<br>

[**FreezeGun**](https://github.com/spulec/freezegun) is a library that allows your Python tests to travel through time
 by mocking the datetime module.

Once the decorator or context manager have been invoked, all calls to `datetime.datetime.now()`, 
`datetime.datetime.utcnow()`, `datetime.date.today()`, `time.time()`, `time.localtime()`, `time.gmtime()`, and `time.strftime()`
will return the time that has been frozen.

<br>

[**HTTPretty**](https://github.com/patrys/httmock) is an HTTP client mocking tool for Python - inspired by Fakeweb for Ruby.

Common use cases:

- Test-driven development of API integrations
- Fake responses of external APIs
- Record and playback HTTP requests

<br>

## Code coverage

[**Coverage.py**](https://github.com/nedbat/coveragepy) measures code coverage, typically during test execution. It uses 
the code analysis tools and tracing hooks provided in the Python standard library to determine which lines are 
executable, and which have been executed.

<br>

## Object Factories

[**factory_boy**](https://github.com/FactoryBoy/factory_boy) is a fixtures replacement based on thoughtbot's factory_bot.

As a fixtures replacement tool, it aims to replace static, hard to maintain fixtures with easy-to-use 
factories for complex objects.

<br>

## Code Style

[**wemake-python-styleguide**](https://github.com/wemake-services/wemake-python-styleguide) is is strictest and most 
opinionated python linter ever.

Goals of WPS:

1. Enforce `Python 3.6+` usage
2. Significantly reduce complexity of your code and make it more maintainable
3. Enforce “There should be one– and preferably only one –obvious way to do it” rule
4. Create consistent coding and naming style

<br>

[**pycodestyle**](https://github.com/PyCQA/pycodestyle) is a tool to check your Python code against some of the style 
conventions in PEP8.

Features:

- Plugin architecture: Adding new checks is easy.
- Parseable output: Jump to error location in your editor.
- Small: Just one Python file, requires only `stdlib`. You can use just the `pycodestyle.py` file for this purpose.
- Comes with a comprehensive test suite.

<br>

[**Black**](https://github.com/psf/black) is the uncompromising Python code formatter. By using it, you agree to cede
control over minutiae of hand-formatting. In return, _Black_ gives you speed,
determinism, and freedom from `pycodestyle` nagging about formatting. You will save time
and mental energy for more important matters.

<br>

[**yapf**](https://github.com/google/yapf) is a formatter for Python files.

YAPF takes a different approach. It's based off of `clang-format`, developed by Daniel Jasper. In essence, 
the algorithm takes the code and reformats it to the best formatting that conforms to the style guide, even if the 
original code didn't violate the style guide. The idea is also similar to the 'gofmt' tool for the Go programming 
language: end all holy wars about formatting - if the whole codebase of a project is simply piped through YAPF 
whenever modifications are made, the style remains consistent throughout the project and there's no point 
arguing about style in every code review.

<br>

## Typing 

[**mypy**](https://github.com/python/mypy) is an optional static type checker for Python. You can add type 
hints (PEP 484) to your Python programs, and use `mypy` to type check them statically. Find bugs in your 
programs without even running them!

Here is a small example to whet your appetite (Python 3):

```python
from typing import Iterator

def fib(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b
```

<br>

[**Pyre**](https://github.com/facebook/pyre-check) is a performant type checker for Python compliant with PEP 484. 
Pyre can analyze codebases with millions of lines of code incrementally – providing instantaneous feedback to 
developers as they write code.

Pyre ships with Pysa, a security-focused static analysis tool we've built on top of Pyre that reasons about data flows 
in Python applications. Please refer to our documentation to get started with our security analysis.

<br>

[**Typeshed**](https://github.com/python/typeshed) contains external type annotations for the Python standard library 
and Python builtins, as well as third party packages as contributed by people external to those projects.

<br>

[**django-stubs**](https://github.com/typeddjango/django-stubs) contains type stubs and a custom `mypy` plugin to 
provide more precise static types and type inference for `Django` framework. Django uses some Python "magic" 
that makes having precise types for some code patterns problematic. This is why we need this project. The final goal 
is to be able to get precise types for most common patterns.

<br>

[**returns**](https://github.com/dry-python/returns) gonna make your functions return something meaningful, typed, and safe!

Features:

- Brings functional programming to Python land
- Provides a bunch of primitives to write declarative business logic
- Enforces better architecture
- Fully typed with annotations and checked with `mypy`, PEP561 compatible
- Adds emulated Higher Kinded Types support
- Has a bunch of helpers for better composition
- Pythonic and pleasant to write and to read 🐍
- Support functions and coroutines, framework agnostic
- Easy to start: has lots of docs, tests, and tutorials

<br>

That's it for now!
