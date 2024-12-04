
def can_trans_to_int(str):
    try:
        int(str)
        return True
    except Exception as e:
        return False


def check_range(do, dont, start, end, next_start):
    # 当前子串开始位置前有dont
    if dont != -1 and dont < start:
        # 最近的do在don't前，无法阻挡don't
        if do != -1 and do < dont:
            return 0
        # 最近的do在子串开始位置之后，无法阻挡don't
        elif do != -1 and do > start:
            return 0
        # do把don't解除的场景
        elif do != -1 and do > dont and do < start:
            return 2
        # 没有do
        elif do == -1:
            return 0
    if end == -1:
        return 0
    if end != -1 and (end < next_start or next_start == -1):
        return 1
    return 0


def match_strs(input):
    i = 0
    # 两个三位数加逗号的最大长度
    matches = []
    do = input.find('do()', 0)
    dont = input.find('don\'t()', 0)
    while i < len(input):
        if input[i:i+4] == "mul(":
            start = i
            end = input.find(')', start)
            next_start = input.find('mul(', start + 4)
            check_result = check_range(do, dont, start, end, next_start)
            if check_result != 0:
                sub_str = input[start+4:end]
                matches.append(sub_str)
                # don't被do解除后，更新最近的don't位置
                if check_result == 2:
                    dont = input.find('don\'t()', i) if input.find(
                        'don\'t()', i) != -1 else dont
        # 仅后续存在时才刷新
            do = input.find('do()', i) if input.find('do()', i) != -1 else do
        i += 1
    return matches


if __name__ == "__main__":
    try:
        with open('data_day3.txt', 'r', encoding="utf-8") as file:
            content = file.read()
        pattern = r'mul\((.{1,7})\)'
        matches = match_strs(content)

        result = 0
        for i in range(len(matches)):
            pair = matches[i].split(',')
            if len(pair) != 2:
                continue
            if can_trans_to_int(pair[0]) and can_trans_to_int(pair[1]):
                result += int(pair[0])*int(pair[1])
        print("Result:", result)
    except Exception as e:
        print(e)
