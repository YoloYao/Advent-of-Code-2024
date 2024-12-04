#293<430
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
    flag = 'INCREASING' if signs.count('+') > signs.count('-') else 'DECREASING'
    # 出现至少2次异常情况，无法修复
    if 'INCREASING' == flag and signs.count('-') + signs.count('=') > 1:
        return False
    if 'DECREASING' == flag and signs.count('+') + signs.count('=') > 1:
        return False
    # 出现1次异常情况，移除异常值
    print("Before remove:", numbers)
    if signs.count('=') > 0:
        index = [i for i, str in enumerate(signs) if str == '=']
        numbers.pop(index[0])
    else :
        if 'INCREASING' == flag and signs.count('-') > 0:
            index = [i for i, str in enumerate(signs) if str == '-']
            numbers.pop(index[0])
        if 'DECREASING' == flag and signs.count('+') > 0:
            numbers.pop(index[0] + 1)
    if 'INCREASING' == flag:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] <= numbers[i]:
                return False
    else:
        for i in range(len(numbers) - 1):
            if numbers[i + 1] >= numbers[i]:
                return False
    print("After remove:", numbers)
    return True

def check_2(numbers):
    # 数组首尾可能存在相差3以上的数，可移除。中间存在时无法通过移除解决问题
    # 移除第一个元素
    if len(numbers) > 1 and abs(numbers[0] - numbers[1]) > 3:
        numbers.pop(0)
    elif len(numbers) > 1 and abs(numbers[-1] - numbers[-2]) > 3:
        numbers.pop(len(numbers) - 1)
    for i in range(len(numbers) - 1):
        if abs(numbers[i + 1] - numbers[i]) > 3:
            return False
        
    return True

# numbers = [16, 13, 12, 9, 6, 5]
# numbers = [1, 3, 2, 4, 9]
numbers = [16, 17, 18, 19, 20, 17, 19, 20]
print(check_1(numbers))