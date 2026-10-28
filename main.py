from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue


def show_state(structure, name):
    print(f"{name} state (top/front to bottom/rear): {structure.state()}")


def run_stack(stack, name):
    while True:
        print(f"\n--- {name} ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("0. Back to main menu")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter a value to push: ")
                stack.push(value)
                print("Value pushed.")
                show_state(stack, name)
            elif choice == "2":
                print("Popped:", stack.pop())
                show_state(stack, name)
            elif choice == "3":
                print("Top value:", stack.peek())
            elif choice == "4":
                print("Is empty:", stack.is_empty())
            elif choice == "5":
                print("Is full:", stack.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(stack, name)


def run_queue(queue, name):
    while True:
        print(f"\n--- {name} ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek front")
        print("4. Check if empty")
        print("5. Check if full")
        print("0. Back to main menu")
        choice = input("Choose an operation: ").strip()

        try:
            if choice == "1":
                value = input("Enter a value to enqueue: ")
                queue.enqueue(value)
                print("Value enqueued.")
                show_state(queue, name)
            elif choice == "2":
                print("Dequeued:", queue.dequeue())
                show_state(queue, name)
            elif choice == "3":
                print("Front value:", queue.peek_front())
            elif choice == "4":
                print("Is empty:", queue.is_empty())
            elif choice == "5":
                print("Is full:", queue.is_full())
            elif choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
        except (IndexError, OverflowError, ValueError) as error:
            print("Error:", error)
            show_state(queue, name)


def balanced_parentheses(text):
    """Return True when (), [] and {} are correctly balanced."""
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in ")]}":
            if not stack or stack.pop() != pairs[character]:
                return False
    return len(stack) == 0


def print_queue_exercise():
    """Demonstrate a print queue in FIFO order."""
    jobs = []
    while True:
        print("\n--- Print Queue Exercise ---")
        print("1. Add print job")
        print("2. Print next job")
        print("3. Show waiting jobs")
        print("0. Back to main menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            job_id = input("Enter job ID: ").strip()
            try:
                pages = int(input("Enter number of pages: "))
                if pages <= 0:
                    print("Page count must be greater than zero.")
                    continue
            except ValueError:
                print("Please enter a valid whole number for pages.")
                continue
            jobs.append({"id": job_id, "pages": pages})
            print("Job added. It will be printed after earlier jobs.")
            print("Waiting jobs:", jobs)
        elif choice == "2":
            if not jobs:
                print("Print queue is empty.")
            else:
                job = jobs.pop(0)
                print(f"Printing job {job['id']} ({job['pages']} pages).")
                print("Remaining jobs:", jobs)
        elif choice == "3":
            print("Waiting jobs (first to print first):", jobs)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")


def parentheses_exercise():
    text = input("Enter a string containing parentheses/brackets: ")
    if balanced_parentheses(text):
        print("The parentheses/brackets are balanced.")
    else:
        print("The parentheses/brackets are NOT balanced.")


def main():
    while True:
        print("\n========== STACKS AND QUEUES LAB ==========")
        print("1. Array Stack")
        print("2. Linked List Stack")
        print("3. Circular Array Queue")
        print("4. Linked List Queue")
        print("5. Check Balanced Parentheses")
        print("6. Simulate Print Queue")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            try:
                capacity = int(input("Enter stack capacity: "))
                run_stack(ArrayStack(capacity), "Array Stack")
            except ValueError:
                print("Please enter a valid positive capacity.")
        elif choice == "2":
            run_stack(LinkedStack(), "Linked List Stack")
        elif choice == "3":
            try:
                capacity = int(input("Enter queue capacity: "))
                run_queue(ArrayQueue(capacity), "Circular Array Queue")
            except ValueError:
                print("Please enter a valid positive capacity.")
        elif choice == "4":
            run_queue(LinkedQueue(), "Linked List Queue")
        elif choice == "5":
            parentheses_exercise()
        elif choice == "6":
            print_queue_exercise()
        elif choice == "0":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
