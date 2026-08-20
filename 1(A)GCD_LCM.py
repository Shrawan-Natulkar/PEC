def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


gcd_value = gcd(num1, num2)


lcm_value = (num1 * num2) // gcd_value


print("GCD =", gcd_value)
print("LCM =", lcm_value)