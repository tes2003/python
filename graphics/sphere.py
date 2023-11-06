def areas(r):
    a=4*3.14*r*r
    print("Area of sphere is",a)
def peris(r):
    p=6.283*r
    print("perimeter of sphere is:",p)


    num = int(input("Enter a number: "))


    sum = 0

    # find the sum of the cube of each digit
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    # display the result
    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")
