# Print "Printing current and previous number sum in a range(10)"
print("Printing current and previous number sum in a range(10)")
# Looping from 1 to 10
p_num = 0
for r_num in range(0, 11):
    # Addition Function
    cp_num = p_num + r_num
# Print "Current Number 0 Previous Number 0 Sum: 0"
    print("Current Number", r_num, "Previous Number", p_num, "Sum: ", cp_num)
    p_num = r_num
