# -*- coding: utf-8 -*-
"""
Sudoku checker

Checks if a sudoku game is valid. Rules are:
    Each row contains numbers 1-9 non-repeating
    Each column contains numbers 1-9 non-repeating
    Each block of 3x3 numbers contains numbers 1-9 non-repeating

Example solved, valid game:
arr_v = [
[4,3,5,2,6,9,7,8,1],
[6,8,2,5,7,1,4,9,3],
[1,9,7,8,3,4,5,6,2],
[8,2,6,1,9,5,3,4,7],
[3,7,4,6,8,2,9,1,5],
[9,5,1,7,4,3,6,2,8],
[5,1,9,3,2,6,8,7,4],
[2,4,8,9,5,7,1,3,6],
[7,6,3,4,1,8,2,5,9]]

Example invalid game:
arr_iv = [
[1,2,3,4,5,6,7,8,9],
[2,3,1,5,6,4,8,9,7],
[3,1,2,3,4,5,9,7,8],
[4,5,6,7,8,9,1,2,3],
[5,6,4,8,9,7,2,3,1],
[6,4,5,9,7,8,3,9,2],
[7,8,9,1,2,3,4,5,6],
[8,9,7,2,3,1,5,6,4],
[9,7,8,3,1,2,6,4,5]]
"""


def sudocheck(arr):
    checklist = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    def checkset(s_arr):
        print(s_arr)
        if checklist.issubset(s_arr):
            return True

    if len(arr) == 9:
        group = []
        rows_checked = cols_checked = grids_checked = False

        # check rows
        print("\nChecking rows...")
        for i in range(len(arr)):
            group.clear()
            for j in range(len(arr[i])):
                group.append(arr[i][j])

            if checkset(group):
                if i == 8:
                    rows_checked = True
                continue
            else:
                print(f"Check failed at row {i}. Breaking...")
                break

        # check columns
        print("\nChecking columns...")
        for i in range(9):  # TODO: find a better way to represent range?
            group.clear()
            for j in range(len(arr)):
                group.append(arr[j][i])

            if checkset(group):
                if i == 8:
                    cols_checked = True
                continue
            else:
                print(f"Check failed at column {i}. Breaking...")
                break

        # check grids
        print("\nChecking grids...")
        for i in range(9):
            group.clear()
            for j in range(3):  # TODO: find a better way to represent range?
                for k in range(3):
                    group.append(arr[3 * (i // 3) + j][3 * (i % 3) + k])

            if checkset(group):
                if i == 8:
                    grids_checked = True
                continue
            else:
                print(f"Check failed at grid {i}. Breaking...")
                break

        if rows_checked and cols_checked and grids_checked:
            # all checks passed, game is valid
            print("\nSudoku board is valid.")
        else:
            print("\nSudoku board is not valid!")

    else:
        print("Check board (length < 9)")
