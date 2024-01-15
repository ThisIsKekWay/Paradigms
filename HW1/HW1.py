from random import sample


def sort_list_imperative(numbers):
    flag = True
    while flag:
        flag = False
        for i in range(len(numbers) - 1):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    return numbers


# Declarative style
def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers


my_list = sample(range(1, 101), 10)
print('Несортированный список:\n',my_list)
print(f"Imperative style -> {sort_list_imperative(my_list)}")
print(f"Declarative style -> {sort_list_imperative(my_list)}")
