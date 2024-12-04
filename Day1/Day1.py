if __name__ == "__main__":
    try:
        # numbers_1 = [3,4,2,1,3,3]
        # numbers_2 = [4,3,5,3,9,3]
        numbers_1 = []
        numbers_2 = []
        with open('data_day1.txt', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
        for i in range(len(lines)):
            num_1 = lines[i].split('   ')[0]
            num_2 = lines[i].split('   ')[1]
            numbers_1.append(int(num_1))
            numbers_2.append(int(num_2))
        # 排序数组
        sorted_numbers_1 = sorted(numbers_1)
        sorted_numbers_2 = sorted(numbers_2)

        result_1 = 0
        result_2 = 0
        for i in range(len(sorted_numbers_1)):
            result_1 += abs(sorted_numbers_1[i] - sorted_numbers_2[i])
            result_2 += sorted_numbers_1[i] * \
                sorted_numbers_2.count(sorted_numbers_1[i])

        print("Result 1:", result_1)
        print("Result 2:", result_2)
    except Exception as e:
        print(e)
