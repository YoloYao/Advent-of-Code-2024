import traceback


def ori_check_1(numbers):
    signs = []
    # 找到n-1个元素和下一个元素的大小关系，增加或减少或相等
    for i in range(len(numbers) - 1):
        if numbers[i + 1] < numbers[i]:
            signs.append('-')
        elif numbers[i + 1] > numbers[i]:
            signs.append('+')
        else:
            signs.append('=')
    flag = 'INCREASING' if signs.count(
        '+') > signs.count('-') else 'DECREASING'

    if 'INCREASING' == flag:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] <= numbers[i]:
                return False
    else:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] >= numbers[i]:
                return False
    return True


def check_1(numbers):
    signs = []
    # 找到n-1个元素和下一个元素的大小关系，增加或减少或相等
    for i in range(len(numbers) - 1):
        if numbers[i + 1] < numbers[i]:
            signs.append('-')
        elif numbers[i + 1] > numbers[i]:
            signs.append('+')
        else:
            signs.append('=')
    flag = 'INCREASING' if signs.count(
        '+') > signs.count('-') else 'DECREASING'
    # 出现至少2次异常情况，无法修复
    if 'INCREASING' == flag and signs.count('-') + signs.count('=') > 1:
        return False
    if 'DECREASING' == flag and signs.count('+') + signs.count('=') > 1:
        return False
    # 出现1次异常情况，移除异常值
    if signs.count('=') > 0:
        # print(numbers, signs)
        # print("Before remove:", numbers)
        index = [i for i, str in enumerate(signs) if str == '=']
        numbers.pop(index[0])
        # print("After remove:", numbers)
    else:
        if 'INCREASING' == flag and signs.count('-') > 0:
            index = [i for i, str in enumerate(signs) if str == '-']
            numbers.pop(index[0])
        if 'DECREASING' == flag and signs.count('+') > 0:
            index = [i for i, str in enumerate(signs) if str == '+']
            numbers.pop(index[0] + 1)
    # 移除后再次判断
    if 'INCREASING' == flag:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] <= numbers[i]:
                return False
    else:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] >= numbers[i]:
                return False
    return True


def ori_check_2(numbers):
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) > 3:
            return False
    print(numbers)
    return True


def check_21(numbers):
    # 数组首尾可能存在相差3以上的数，可移除。中间存在时无法通过移除解决问题
    # 移除第一个元素
    if len(numbers) > 1 and abs(numbers[0] - numbers[1]) > 3:
        # print("before 1:", numbers)
        numbers.pop(0)
        # print("after 1:", numbers)
    elif len(numbers) > 1 and abs(numbers[-1] - numbers[-2]) > 3:
        # print("before 2:", numbers)
        numbers.pop(len(numbers) - 1)
        # print("after 2:", numbers)

    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) > 3:
            # print(numbers)
            return False
    print(numbers)
    return True


def check_2(numbers):
    new_nums = []
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) > 3:
            # print(numbers)
            new_nums = list.copy(numbers)
    # 数组首尾可能存在相差3以上的数，可移除。中间存在时无法通过移除解决问题
    # 移除第一个元素
    if len(numbers) > 1 and abs(numbers[0] - numbers[1]) > 3:
        # print("before 1:", numbers)
        numbers.pop(0)
        # print("after 1:", numbers)
    elif len(numbers) > 1 and abs(numbers[-1] - numbers[-2]) > 3:
        # print("before 2:", numbers)
        numbers.pop(len(numbers) - 1)
        # print("after 2:", numbers)

    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) > 3:
            # print(numbers)
            return False
    print(numbers)
    return True


if __name__ == "__main__":
    try:
        # matrix = [[7, 6, 4, 2, 1],
        #           [1, 2, 7, 8, 9],
        #           [9, 7, 6, 2, 1],
        #           [1, 3, 2, 4, 5],
        #           [8, 6, 4, 4, 1],
        #           [1, 3, 6, 7, 9]]
        matrix = []
        with open('data_day2.txt', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
        for i in range(len(lines)):
            numbers = lines[i].split(' ')
            matrix.append(list(map(int, numbers)))

        count = 0
        for i in range(len(matrix)):
            if check_1(matrix[i]) == False:
                continue
            if check_21(matrix[i]) == False:
                continue
            count += 1

        print("Result 1:", count)
    except Exception as e:
        print(f"Error:{e}")
        traceback.print_exc()
