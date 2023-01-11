alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shortest_string_add(num):
    string = ""
    while num != 0:
        if num >= 26:
            string += "z"
            num -= 26
        else:
            string += alphabet[num - 1]
            num = 0
    
    print(string)

def shortest_string_concat(num):
    string = ""
    
    num_list = list(str(num))

    while len(num_list) != 0:
        # Base case
        if len(num_list) < 2:
            string += alphabet[int(num_list[0]) - 1]
            num_list.pop()

        # Convert first two to int
        first_two_num = int("".join([num_list[0], num_list[1]]))

        # if first_two_num < 26, return the corresponding letter, chop off first two
        if first_two_num < 26:
            string += alphabet[first_two_num - 1]
            num_list.pop()
            num_list.pop()
        # if > 26, then you have to split the digits
        else:
            string += alphabet[int(num_list.pop()) - 1] + alphabet[int(num_list.pop()) - 1]

    print(string)

shortest_string_add(56)
shortest_string_concat(482493874949)