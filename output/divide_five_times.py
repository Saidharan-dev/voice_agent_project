# Repeatedly divide 10 by 5 five times and print the result of each division
def repeated_division():
    number = 10
    divisor = 5
    iterations = 5

    results = []
    for _ in range(iterations):
        result = number / divisor
        results.append(result)
        number = result  # update the dividend for the next iteration
        divisor = 2 * divisor  # double the divisor for each subsequent division

    return results

# Example usage:
print(repeated_division())