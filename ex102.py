# Function to Calculate a factorial of any value

def factorial(n, show=False):
    """
    -> This function calculates the factorial of a number n.
    :param n: Number to be calculated.
    :param show: (Optional) Show or not show the calculation.
    :return: return the result of factorial.
    """
    k = n
    result = 1
    if show == True:
        while k > 0:
            if k != 1:
                result *= k
                print(f'{k}', end=' x ')
                k -= 1
            else:
                print(f'{k}', end=' = ')
                k -= 1
        return result
    else:
        while k > 0:
            result *= k
            k -= 1
        return result


print(factorial(12, show=True))

help(factorial)
