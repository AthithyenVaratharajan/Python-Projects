from operator import truediv


def ryerson_letter_grade(pct):
    tens = pct // 10
    ones = pct % 10
    char = ''
    if pct < 50:
        return 'F'
    if tens == 5:
        char = 'D'
    elif tens ==6:
        char = 'C'
    elif tens ==7:
        char = 'B'
    elif tens ==8:
        char = 'A'
    elif tens ==9:
        return 'A+'
    for i in range(0, 5):
        if ones == i:
            return char + "-"
    for j in range(6, 10):
        if ones == j:
            return char + "+"
    if ones == 5:
        return char

# Time Complexity - Big O(n)
# Space complexity - O(n)

def is_ascending(items):
    #  iterate through array
    # check if previous element is smaller than current element
    # if next element bigger than current element return true else return false
    if len(items) == 1 or len(items) == 0:
        return True
    for i in range(len(items)-1):
        if items[i] < items[i+1]:
            return True
    return False

items = [[] ,
[-5, 10, 99, 123456],
[2, 3, 3, 4, 5],
[-99],
[4, 5, 6, 7, 3, 7, 9],
[1, 1, 1, 1]]

for item in items:
    print(is_ascending(item))
