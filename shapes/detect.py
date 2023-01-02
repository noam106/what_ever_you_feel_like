def is_rectangle(list_of_nums: list[float]) -> bool:
    for i in list_of_nums:
        if type(i) == float or type(i) == int:
            if list_of_nums[0] == sum(list_of_nums) / 4:
                return False
    for num in list_of_nums:
        if num <= 0:
            return False
    if len(list_of_nums) == 4:
        if list_of_nums[0] == list_of_nums[1]:
            if list_of_nums[2] == list_of_nums[3]:
                return True
        elif list_of_nums[0] == list_of_nums[2]:
            if list_of_nums[1] == list_of_nums[3]:
                return True
        elif list_of_nums[0] == list_of_nums[3]:
            if list_of_nums[1] == list_of_nums[2]:
                return True
    else:
        return False


def is_square(list_of_num: list[float]) -> bool:
    for i in list_of_num:
        if type(i) == float or type(i) == int:
            for num in list_of_num:
                if num <= 0:
                    return False
    if len(list_of_num) == 4:
        if list_of_num[0] == sum(list_of_num) / 4:
            return True
    else:
        return False


def is_triangle(list_of_side: list[float]) -> bool:
    for i in list_of_side:
        if type(i) == float or type(i) == int:
            for num in list_of_side:
                if num <= 0:
                    return False
    if len(list_of_side) == 3:
        if list_of_side[0] + list_of_side[1] > list_of_side[2]:
            if list_of_side[0] + list_of_side[2] > list_of_side[1]:
                if list_of_side[0] < list_of_side[1] + list_of_side[2]:
                    return True
    else:
        return False



