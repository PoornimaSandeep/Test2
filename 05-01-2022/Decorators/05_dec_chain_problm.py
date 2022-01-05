print("Write a Python program to make a chain of function decorators (bold, italic, underline etc.).")


def bold(func):
    def inner():
        return f"<b>{func()}</b>"
    return inner
def italic(func):
    def inner():
        return f"<i>{func()}</i>"
    return inner

def underline(func):
    def inner():
        return f"<u>{func()}</u>"
    return inner

@underline
@italic
@bold
def text():
    return "hello"
print(text())