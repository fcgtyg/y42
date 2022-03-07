# Testing a Struct Interface

## Structure
This package includes solutions for "Testing a Struct Interface" challenge. Tests written in Pytest testing framework.

* `stack.py`: A basic Stack implementation to make tests on. This stack implements every method specified at Challenge Document.

* `exceptions.py`: Exceptions of stack when a specific situation occurred. The situations and exception class names are directly from Challenge Document.

* `test_stack.py`: Actual solution part of the challenge. In this file, there are unit testss for every method of `Stack` class.

## How to run?

At the project root folder, invoke the following command:

> `$ pytest stack_test/test_stack.py`

The output should show `9 passed in x.xxs` with green font. This indicates there are 9 tests and Stack class can pass all of them.