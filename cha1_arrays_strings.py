# https://ryanym.com/posts/ctci-on-leetcode/
# does string contain only unique letters
def is_unique(word: str()) -> bool:
    # time complexity: O(n), space complexity: O(1)
    if len(word) > 128: return False

    char_table = [False] * 128
    for index, letter in enumerate(word):
        val_letter = ord(letter)
        if char_table[val_letter]:
            return False
        char_table[val_letter] = True
    
    return True

word = "abcdc"
# print(f"is_unique returns: {is_unique(word)}")


# is string a permutation of another string
def permutation_1(s: str(), t: str()) -> bool:
    # time complexity O(n log n)
    sorted_s = ''.join(sorted(list(s)))
    sorted_t = ''.join(sorted(list(t)))
    if len(s) != len(t): return False
    if sorted_s == sorted_t: return True
    else: return False

def permutation_2(s: str(), t: str()) -> bool:
    # time complexity O(n)
    if len(s) != len(t): return False

    char_table = [0] * 128
    
    for letter in s:
        char_table[ord(letter)] += 1

    for l in t:
        char_table[ord(l)] -= 1
        if char_table[ord(l)] < 0: return False
    
    return True

s = "abd"
t = "dba"
t2 = "abc"
# print(f"is t a permutation of s? {permutation_1(s, t)}")
# print(f"is t2 a permutation of s? {permutation_1(s, t2)}")
# print(f"is t a permutation of s? {permutation_2(s, t)}")
# print(f"is t2 a permutation of s? {permutation_2(s, t2)}")


# URLify string: for a fixed length of string, replace space with "%20"
def urlify(s: str(), true_length: int()) -> str:
    #  two scan approach: first scan, get the num of spaces, second scan, edit the string backward, and triple the spaces.
    space_count = 0

    for letter in s:
        if letter == ' ':
            space_count += 1
    
    new_s = [1] * (true_length + space_count * 2)
    index = true_length + space_count * 2
    for i in range(true_length-1, -1, -1):
        if s[i] != ' ':
            new_s[index-1] = s[i]
            index -= 1
        else:
            new_s[index-1] = '0'
            new_s[index-2] = '2'
            new_s[index-3] = '%'
            index -= 3
    return ''.join(new_s)

s = "Mr John Smith"
t = "Mr%20John%20Smith"
# print(f"URLify string {s} returns: {urlify(s, 13)}. Is this the same as {t}? {urlify(s, 13) == t}")


# palindrome permutation
# check if a string is a permutation of a palindrome. a palindrome is a word or phrase that is the same forwards and backwards. can be numeric or alphanumeric.
def is_palindrome_perm_1(s: str()) -> bool:
    # hash map
    # time complexity O(n)
    s_no_space = s.replace(' ', '')
    letter_set = set(s_no_space)
    count_dict = dict()
    for letter in letter_set:
        count_dict[letter.lower()] = 0

    for letter in s_no_space:
        count_dict[letter.lower()] += 1
    print(count_dict)
    odd_count_letters = 0    
    for letter, ct in count_dict.items():
        if ct % 2 == 1:
            odd_count_letters += 1

    return (odd_count_letters == 0 or odd_count_letters == 1)


def is_palindrome_perm_2(s: str()) -> bool:
    # single pass
    s_no_space = s.replace(' ', '')
    letter_set = set(s_no_space)
    count_dict = dict()
    count_odd = 0

    for letter in letter_set:
        count_dict[letter.lower()] = 0

    for letter in s_no_space:
        count_dict[letter.lower()] += 1
        if count_dict[letter.lower()] % 2 == 1:
            count_odd += 1
        else:
            count_odd -= 1

    return  count_odd <= 1


# s = 'Tact Coa'
# print(f"check if s is a palindrome permutation: {is_palindrome_perm_2(s)}.")  
# s = 'Tact Coad'
# print(f"check if s is a palindrome permutation: {is_palindrome_perm_2(s)}.")   
# s = 'tactcoapapa'
# print(f"check if s is a palindrome permutation: {is_palindrome_perm_2(s)}.")   
# s = 'AaBb//a'
# print(f"check if s is a palindrome permutation: {is_palindrome_perm_2(s)}.")     


# one away: given two strings, there are only 1 of the 3 types of operations can be happen to generate one and the other string:
# remove, insert, or replace one letter
def one_away(s: str(), t: str()) -> bool:
    if len(s) - len(t) > 1:
        return False

    sup = s if len(s) >= len(t) else t
    sub = s if len(t) > len(s) else t

    for index in range(len(sub)):
        if sub[index] != sup[index]:
            if len(sup) == len(sub):
                return sub[index+1:] == sup[index+1:]
            else:
                return sub[index:] == sup[index+1:]

    return len(sub) + 1 == len(sup)


# s = "pale"
# t = "ple"
# print(f"{s} and {t} are one away: {one_away(s, t)}")
# s = "pales"
# t = "pale"
# print(f"{s} and {t} are one away: {one_away(s, t)}")
# s = "pale"
# t = "bale"
# print(f"{s} and {t} are one away: {one_away(s, t)}")
# s = "pale"
# t = "bake"
# print(f"{s} and {t} are one away: {one_away(s, t)}")
# s = "abcd"
# t = "bbd"
# print(f"{s} and {t} are one away: {one_away(s, t)}")


# string compression: compress string with duplicate consecutive letters into numbers
# Run Length Encoding problem, RLE
def str_compr(s: str()) -> str:
    str_arr = list(s)
    output = []
    i = j = 0
    while (j < len(str_arr)):
        if str_arr[j] != str_arr[i]:
            output.extend([str_arr[i], str(j-i)]) if (j-i) != 1 else output.extend([str_arr[i]])
            i = j
        j += 1
    output.extend([str_arr[i], str(j-i)]) if (j-i) != 1 else output.extend([str_arr[i]])

    return ''.join(output)

s = 'aabcccccaa'
s = 'aabbccc'
s = 'a'
s = 'abbbbbbbbbbbb'
# print(f"compress string {s} to {str_compr(s)}")


# rotate matrix N*N by 90 degrees clockwise
def rotate(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    layer = 0
    while layer < n/2:
        first = layer
        last = n - layer - 1
        for i in range(first, last):
            offset = i - first
            tmp = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = tmp
        layer += 1
    return matrix

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# print(f"rotate matrix {matrix} 90 degrees clockwise to {rotate(matrix)}")


# zero matrix: in matrix M*N, if an element is 0, set entire column and row to 0
def setZeroes(matrix: [[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    pos = []
    for j in range(m):
        for i in range(n):
            if matrix[j][i] == 0:
                pos.append((j, i))

    for element in pos:
        index1 = element[0]
        index2 = element[1]
        for j in range(n):
            matrix[index1][j] = 0
        for i in range(m):
            matrix[i][index2] = 0
    
    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(f"set zero for matrix {matrix} to {setZeroes(matrix)}")

# string rotation:
# We are given two strings, A and B.
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position. 
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.
def rotateString(A: str, B: str) -> bool:
    res = 0
    for i in range(len(A)):
        if B == A[i:] + A[:i]:
            res += 1
    
    return bool(res)

def rotateString2(A: str, B: str) -> bool:
    return len(A) == len(B) and B in A+A

A = 'abcde'
B = 'bcdea'
print(rotateString(A, B))
print(rotateString2(A, B))