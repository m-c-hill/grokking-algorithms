from typing import List

# Problem 1 - Single Number
def find_missing_number_in_range(arr: List[int]) -> int:
    """
    PARTIAL SUM ^ MISSING NUMBER = TOTAL
    TOTAL ^ PARTIAL SUM = MISSING NUMBER
    """

    total = 0
    for i in range(2, len(arr) + 2):
        total ^= i

    partial_sum = arr[0]
    for num in arr[1:]:
        partial_sum ^= num

    return partial_sum ^ total


# Problem 2 - Two Single Numbers
def find_two_single_numbers(arr: List[int]) -> List[int]:
    """
    A ^ B ^ A = B since A ^ A = 0 and B ^ 0 = B
    """

    n1xn2 = 0
    for n in arr:
        n1xn2 ^= n

    # Retrieve the rightmost bit that is 1 - here the numbers differ
    rightmost_set_bit = 1
    while (rightmost_set_bit & n1xn2) == 0:
        # Shift the rightmost bit until we find where the first bit set to one is
        rightmost_set_bit = rightmost_set_bit << 1

    num1, num2 = 0, 0
    for num in arr:
        # separate number in array into nums that have the rightmost bit set and
        #   those that do not. num1 will fall in one side, num2 the other.
        if (num & rightmost_set_bit) != 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]


# Problem 3 - Complement of Base 10 Number
def compliment_of_base_10(num: int) -> int:
    """
    num ^ compliment = all bit set,
        so all_bit_set ^ num = compliment

    where all bit set is binary num with all 1s equal in length to num and comp
    """

    # Calculate the all bit set
    bit_count = 0
    n = num
    while n > 0:
        bit_count += 1
        n = n >> 1

    all_bit_set = 2 ** (bit_count) - 1

    return all_bit_set ^ num


# Problem Challenge 1 - Flip and Invert an Image
def flip_and_invert(image: List[List[int]]) -> List[List[int]]:
    """
    Flip horizontally, then invert
    """
    n = len(image)
    for row in image:
        for i in range((n + 1) // 2):
            row[i], row[(n - 1) - i] = row[(n - 1) - i] ^ 1, row[i] ^ 1

    return image
