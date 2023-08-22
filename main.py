def sum_of_squares(nums, test_case_number, total_test_cases):
    if test_case_number > total_test_cases:
        return

    print("Total number of integers for test case " + str(test_case_number) + " :")
    x = int(input())

    print("Enter "+ str(x) + " space separated integers :")
    y_values = list(map(int, input().split()))
    result = calculate_sum_of_squares(y_values)
    print("Calculated Sum of Squares of the integers :" + str(result))

    sum_of_squares(nums, test_case_number + 1, total_test_cases)

def calculate_sum_of_squares(nums):
    if not nums:
        return 0
    else:
        num = nums[0]
        if num >= 0:
            return num * num + calculate_sum_of_squares(nums[1:])
        else:
            return calculate_sum_of_squares(nums[1:])

print("Number of test cases :")
total_test_cases = int(input())

sum_of_squares([], 1, total_test_cases)
