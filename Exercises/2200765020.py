N = int(input("Enter a natural number:"))

total = 0
avg = []
for i in range(1,N+1):
    if (i % 2 != 0):
        total += i
print("Sum of odd numbers up to",N,":", total)

for j in range(1,N+1):
    if (j % 2 == 0):
        avg.append(j)
print("Average of even numbers starting from 1 up to and including", N, ":", sum(avg)/len(avg))

















