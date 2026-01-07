# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    output = ""

    for i in range(n):
        for j in range (n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                output += "*"
            else:
                output += " "      
        if i == n - 1:
            output += ""
        else:
            output += "\n" 
    
    return output


# 1
# 12
# 123
# 1234
def number_pattern(n):
    output = ""
    i = 1

    while i in range(n + 1):
        j = 1
        i += 1
        while j in range(i):
            output += str(j)
            j += 1
        if j == n + 1:
            output += ""
        else:
            output += "\n"
   
    return output


# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    sum = 0
    i = 0

    while i < (n + 1):
        sum += i
        i += 1
    
    return sum

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    output = ""
    for i in range(1, n + 1):

        for j in range(n - i):
            output += " "
     
        for k in range(1, 2*i):
            output += "*"    
        output += "\n"

    return output.rstrip()
