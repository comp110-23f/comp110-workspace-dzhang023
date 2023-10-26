"""Practice with lists."""
grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list.pop(2)
print(len(grocery_list))


def only_evens(list_ints: list[int]) -> list[int]:
    """Given a list, the function returns a list with only the even values of the given."""
    even_ints = []
    for num in list_ints:
        if num % 2 == 0:
            even_ints.append(num)
    return even_ints


def concat(list1: list[int], list2: list[int]) -> list[int]:
    """Combines two given lists."""
    big_list = []
    for num in list1:
        big_list.append(num)
    for num in list2:
        big_list.append(num)
    return big_list


def sub(list_ints: list[int], start_ind: int, end_ind: int) -> list[int]:
    """Creates a subarray based on two intervals."""
    end_list = []
    for num in list_ints[start_ind:end_ind]:
        end_list.append(num)
    return end_list
