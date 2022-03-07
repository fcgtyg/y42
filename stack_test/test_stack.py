import pytest
from stack import Stack
from exceptions import EmptyStackException, NullElementException


@pytest.fixture
def stack():
    return Stack()


@pytest.fixture
def stack_with_data(*initial_data):
    def __make_stack(*initial_data):
        return Stack(*initial_data)
    return __make_stack


def test_size(stack_with_data):
    initial_data = ["First Element", "Second Element"]
    stack = stack_with_data(*initial_data)
    
    expected_val = len(initial_data)
    actual_val = stack.size()
    
    assert expected_val == actual_val


def test_push_normal(stack):
    case_ = "Normal Element"
    stack.push(case_)
    assert stack.peek() == case_
    assert stack.size() == 1


def test_push_none(stack):
    case_ = None # Null Element
    with pytest.raises(NullElementException) as expected_exception:
        stack.push(case_)


def test_pop_empty(stack):
    with pytest.raises(EmptyStackException) as expected_exception:
        stack.pop()


def test_pop_non_empty(stack_with_data):
    case_ = ["First Element", "Last Element"]
    stack = stack_with_data(*case_)

    expected = case_[-1]
    actual = stack.pop()

    assert expected == actual
    assert stack.size() == len(case_)-1


def test_peek_empty(stack):
    with pytest.raises(EmptyStackException) as expected_exception:
        stack.peek()


def test_peek_non_empty(stack_with_data):
    peek_ = "peek element"
    stack = stack_with_data("first element", "second element", peek_)

    size_before_peek = stack.size()
    expected = peek_
    actual = stack.peek()
    size_after_peek = stack.size()

    assert expected == actual
    assert size_before_peek == size_after_peek


def test_empty_empty(stack):
    assert stack.empty()


def test_empty_non_empty(stack_with_data):
    stack = stack_with_data(object())
    assert not stack.empty()