prime = []

def is_prime(num):
    if num < 1:
        return False
    for i in range (2, num+1):
        prime.append(i)
        for j in range(2, i):
            if i % j == 0:
                prime.remove(i)
                break


  
    print(prime)

is_prime(20)