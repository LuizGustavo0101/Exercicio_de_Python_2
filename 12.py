def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
       
        median = sorted_numbers[n // 2]
    else:

        middle1 = sorted_numbers[(n // 2) - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2

    return median

numbers = [12, 8, 15, 7, 20]
median = calculate_median(numbers)
print("Mediana:", median)
