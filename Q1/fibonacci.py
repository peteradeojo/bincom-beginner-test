# Question 1: Implement a Fibonacci Series generator
# implemented a generator function


def fibonacci():
  # Initialize with first fibonacci numbers which are 1 and 1
  a = 1
  b = 1
  value = a
  bridge = 0
  while True:
    yield value

    # Logic for updating the next number in the series
    bridge = a + b
    a = b
    b = bridge
    value = a



fib = fibonacci()

# use the generator to print 10 numbers in the series
for i in range(10):
  print(next(fib))
