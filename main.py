def addNumbers(number1, *numbers):
    result = number1
    for number in numbers:
        result += number

    return result

