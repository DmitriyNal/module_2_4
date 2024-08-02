numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
pr_flag = False
for i in numbers:
    if i==1:
        continue
    pr_flag = False
    for j in range(2, i):
        if i % j == 0:
            pr_flag = True
            break
    if pr_flag:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)





















        #print(primes)
#print(not_primes)













