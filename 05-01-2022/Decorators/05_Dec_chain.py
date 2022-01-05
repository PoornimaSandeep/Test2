print("decorator chain working like bottom-up approach the return value will pass one "
      "function to another function")

def dec(func):
    def inner():
        return "this is first function"
    return inner
def dec2(func):
      def inner():
          return "this is second function"

      return inner

@dec2
@dec
def hello():
    return "hello"

print(hello())
