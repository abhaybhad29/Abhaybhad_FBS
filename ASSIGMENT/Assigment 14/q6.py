#Write a Python program to find the two numbers whose product is
#maximum among all the pairs in a given list of numbers. Use the
#Python set.
def maximum_product(numbers):
    num_set = set(numbers)
    max_product = None
    max_pair = ()

    for num1 in  num_set:
        for num2 in num_set:
            if num1 != num2:
                product = num1 * num2

                if max_product is None or product > max_product:
                    max_product = product
                    max_pair = (num1,num2)

    return max_pair,max_product
numbers = [2,5,3,8,6,4]
pair,product = maximum_product(numbers)  
print("Pair with maximum product:", pair)
print("Maximum product:", product)              