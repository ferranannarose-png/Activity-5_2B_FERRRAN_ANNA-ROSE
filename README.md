# Stacks and Queues: Array vs. Linked List

## Description
This Python project demonstrates four data structures:
- `ArrayStack`: fixed-capacity stack using a Python list.
- `LinkedStack`: stack using linked nodes.
- `ArrayQueue`: fixed-capacity circular queue.
- `LinkedQueue`: queue using linked nodes.

The menu-driven program also checks balanced parentheses and simulates a print queue.

## Files
- `array_stack.py` — array-based stack class.
- `linked_stack.py` — linked-list stack class.
- `array_queue.py` — circular array queue class.
- `linked_queue.py` — linked-list queue class.
- `main.py` — menu and application exercises.
- `analysis.md` — written analysis answer.

## Requirements
Python 3.

## How to Run
Keep all five Python files in the same folder. Open a terminal or Python IDE in that folder and run:

```bash
python main.py
```

On some computers, use `python3 main.py`.

## Operations
Stack: push, pop, peek, is_empty, is_full.
Queue: enqueue, dequeue, peek_front, is_empty, is_full.

The program displays the structure's state after successful push, pop, enqueue, and dequeue operations. It also displays descriptive error messages for underflow and overflow.

## Test Suggestions
1. Choose Array Stack with capacity 2. Pop while empty to test underflow.
2. Push two values, then push a third to test overflow.
3. Choose Circular Array Queue with capacity 3. Enqueue A, B, C; dequeue A; then enqueue D to test wrap-around.
4. Enter `([{}])` in the balanced-parentheses exercise; it should be balanced.
5. Enter `([)]`; it should not be balanced.
6. Add print jobs such as P01 (3 pages), P02 (5 pages), and P03 (2 pages). Print jobs to observe FIFO order.

## Notes
Linked-list structures do not have a fixed capacity, so their `is_full()` method returns `False`; they may still be limited by available memory.
