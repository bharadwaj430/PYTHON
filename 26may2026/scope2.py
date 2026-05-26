def outer_func():
    msg = 'this is bharadwaj!'
    result = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal result  # Allow modification of an enclosing variable
        result = 'are you a trainee at consistency.ai?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(result)  # Now result is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?

  