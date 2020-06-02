# Sum of even fibonacci numbers under 4000000
current_fib = 1
last_fib = 1
next_fib = 0
running_total = 0
while current_fib <= 4000000:
    next_fib = current_fib + last_fib
    current_fib, last_fib = next_fib, current_fib
    if next_fib % 2 == 0:
        running_total += current_fib

print(f"This is the sum of even fibs {running_total}")
