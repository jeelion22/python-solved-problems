def isPrime(a):

    if a > 1:
        for i in range(2, a):
            if a % i != 0:
                #                print(i)
                yes = f"{a} is a PRIME number"
                status = True
            else:
                no = f"{a} is not a PRIME number"
                status = False
                break
    if status is True:
        print(yes)
    else:
        print(no)


isPrime(6382880219)
