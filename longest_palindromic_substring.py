def longest_palindromic_substring(string):
    max_length = 1
    longest_palindrome = string[0]

    for center in range(1, 2 * len(string) - 1):
        left = center // 2
        right = left + center % 2

        while left >= 0 and right < len(string) and string[left] == string[right]:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                longest_palindrome = string[left:right + 1]

            left -= 1
            right += 1

    return longest_palindrome


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print("Longest palindromic substring is : ", longest_palindromic_substring(input_string))
