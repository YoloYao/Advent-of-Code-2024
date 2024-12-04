import traceback


def check(matrix, i, j):
    try:
        if i < 0 or j < 0:
            return False
        str = matrix[i][j]
        return True
    except Exception as e:
        return False


def count_xmas1(matrix, aim_str):
    count_1 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ori_count = count_1
            if matrix[i][j] != 'X':
                continue
            # 从横向顺时针检查8个方向
            # 1.从左向右
            if check(matrix, i, j) and check(matrix, i, j + 1) and check(matrix, i, j + 2) and check(matrix, i, j + 3):
                local_str = matrix[i][j] + matrix[i][j +
                                                     1] + matrix[i][j+2] + matrix[i][j+3]
                if aim_str == local_str:
                    count_1 += 1
            # 2.左上到右下
            if check(matrix, i, j) and check(matrix, i+1, j + 1) and check(matrix, i+2, j + 2) and check(matrix, i+3, j + 3):
                local_str = matrix[i][j] + matrix[i + 1][j +
                                                         1] + matrix[i+2][j+2] + matrix[i+3][j+3]
                if aim_str == local_str:
                    count_1 += 1
            # 3.从上到下
            if check(matrix, i, j) and check(matrix, i+1, j) and check(matrix, i+2, j) and check(matrix, i+3, j):
                local_str = matrix[i][j] + matrix[i +
                                                  1][j] + matrix[i+2][j] + matrix[i+3][j]
                if aim_str == local_str:
                    count_1 += 1
            # 4.右上到左下
            if check(matrix, i, j) and check(matrix, i+1, j-1) and check(matrix, i+2, j-2) and check(matrix, i+3, j-3):
                local_str = matrix[i][j] + matrix[i + 1][j -
                                                         1] + matrix[i+2][j-2] + matrix[i+3][j-3]
                if aim_str == local_str:
                    count_1 += 1
            # 5.从右到左
            if check(matrix, i, j) and check(matrix, i, j-1) and check(matrix, i, j-2) and check(matrix, i, j-3):
                local_str = matrix[i][j] + matrix[i][j -
                                                     1] + matrix[i][j-2] + matrix[i][j-3]
                if aim_str == local_str:
                    count_1 += 1
            # 6.右下到左上
            if check(matrix, i, j) and check(matrix, i-1, j-1) and check(matrix, i-2, j-2) and check(matrix, i-3, j-3):
                local_str = matrix[i][j] + matrix[i - 1][j -
                                                         1] + matrix[i-2][j-2] + matrix[i-3][j-3]
                if aim_str == local_str:
                    count_1 += 1
            # 7.从下到上
            if check(matrix, i, j) and check(matrix, i-1, j) and check(matrix, i-2, j) and check(matrix, i-3, j):
                local_str = matrix[i][j] + matrix[i -
                                                  1][j] + matrix[i-2][j] + matrix[i-3][j]
                if aim_str == local_str:
                    count_1 += 1
            # 8.左下到右上
            if check(matrix, i, j) and check(matrix, i-1, j+1) and check(matrix, i-2, j+2) and check(matrix, i-3, j+3):
                local_str = matrix[i][j] + matrix[i - 1][j +
                                                         1] + matrix[i-2][j+2] + matrix[i-3][j+3]
                if aim_str == local_str:
                    count_1 += 1
            # if ori_count != count_1:
            #     print(f"{matrix[i][j]}, x:{i}, y:{
            #         j}, add:{count_1-ori_count}")
    return count_1


def count_xmas2(matrix, aim_str):
    count_2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            ori_count = count_2
            if matrix[i][j] != 'A':
                continue
            side_1 = False
            side_2 = False
            # 左上到右下（包括反向）
            if check(matrix, i-1, j-1) and check(matrix, i+1, j+1):
                local_str_1 = matrix[i-1][j-1] + \
                    matrix[i][j] + matrix[i+1][j+1]
                local_str_2 = matrix[i+1][j+1] + \
                    matrix[i][j] + matrix[i-1][j-1]
                if aim_str == local_str_1 or aim_str == local_str_2:
                    side_1 = True
                else:
                    continue
            # 右上到左下（包括反向）
            if check(matrix, i-1, j+1) and check(matrix, i+1, j-1):
                local_str_1 = matrix[i-1][j+1] + \
                    matrix[i][j] + matrix[i+1][j-1]
                local_str_2 = matrix[i+1][j-1] + \
                    matrix[i][j] + matrix[i-1][j+1]
                if aim_str == local_str_1 or aim_str == local_str_2:
                    side_2 = True
                else:
                    continue

            if side_1 and side_2:
                count_2 += 1

            # if ori_count != count_2:
            #     print(f"{matrix[i][j]}, x:{i}, y:{
            #         j}, add:{count_2-ori_count}")

    return count_2


if __name__ == "__main__":
    try:
        matrix = []
        with open('data_day4.txt', 'r', encoding='utf-8') as file:
            lines = file.read().splitlines()
        # lines = ["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX", "XMASAMXAMM",
        #          "XXAMMXXAMA", "SMSMSASXSS", "SAXAMASAAA", "MAMMMXMMMM", "MXMXAXMASX"]
        # lines = [".M.S......", "..A..MSMS.", ".M.S.MAA..", "..A.ASMSM.", ".M.S.M....",
            #  "..........", "S.S.S.S.S.", ".A.A.A.A..", "M.M.M.M.M.", ".........."]
        for i in range(len(lines)):
            strs = list(lines[i])
            matrix.append(strs)
        aim_str_1 = "XMAS"
        aim_str_2 = "MAS"
        count_1 = count_xmas1(matrix, aim_str_1)
        count_2 = count_xmas2(matrix, aim_str_2)

        print("Result 1:", count_1)
        print("Result 2:", count_2)
    except Exception as e:
        print(f"Error:{e}")
        traceback.print_exc()
