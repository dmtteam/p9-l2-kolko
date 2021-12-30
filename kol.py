bad_taken="Bad move. Position is taken. Try again."
bad_range="Bad range. Use 1 to 9. Try again."
move="What's Your move?"
human_first_move = 0
human_second_move = 0
human_third_move = 0
human_fourth_move = 0
machine_first_move = 5
machine_second_move = 0
machine_third_move = 0
machine_fourth_move = 0
machine_fifth_move = 0
p1="-"
p2="-"
p3="-"
p4="-"
p5="X"
p6="-"
p7="-"
p8="-"
p9="-"

print('#' *25)
print("Matrix:")
print(f"123\n345\n789")
print("Machine started with X...")
print(f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}\nX=machine, O=human")
print('#' *25)


while True:     # human chose 1 move
    print(move)
    human_first_move=int(input())
    if human_first_move <1 or human_first_move >9:
        print(bad_range)
        continue
    if human_first_move == machine_first_move:
        print(bad_taken)
        continue

    if human_first_move == 1:
        p1="0"
        break
    if human_first_move == 2:
        p2="0"
        break
    if human_first_move == 3:
        p3="0"
        break
    if human_first_move == 4:
        p4="0"
        break
    if human_first_move == 6:
        p6="0"
        break
    if human_first_move == 7:
        p7="0"
        break
    if human_first_move == 8:
        p8="0"
        break
    if human_first_move == 9:
        p9="0"
        break

print('#' *25)
print("Human move...")
print(f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}\n")
print('#' *25)

while True:     # machine second move
    print("Next Machine move is...")
    if human_first_move == 1:
        machine_second_move = 3
        p3="X"
        break
    if human_first_move == 2:
        machine_second_move = 1
        p1= "X"
        break
    if human_first_move == 3:
        machine_second_move = 1
        p1= "X"
        break
    if human_first_move == 4:
        machine_second_move = 1
        p1= "X"
        break
    if human_first_move == 6:
        machine_second_move = 3
        p3= "X"
        break
    if human_first_move == 7:
        machine_second_move = 1
        p1= "X"
        break
    if human_first_move == 8:
        machine_second_move = 7
        p7= "X"
        break
    if human_first_move == 9:
        machine_second_move = 7
        p7= "X"
        break

print('#' *25)
print("Machine move...")
print(f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}\n")
print('#' *25)


while True:  # human second move
    print(move)
    human_second_move=int(input())

# start of 1st block
    if human_second_move <1 or human_second_move >9:
        print(bad_range)
        continue
    if human_second_move == 5:
        print(bad_taken)
        continue
    if human_second_move == human_first_move:
        print(bad_taken)
        continue
    if human_second_move == machine_first_move or human_second_move == machine_second_move :
        print(bad_taken)
        continue
# end of 1st block
# rest input checkout, few position twice checked - to improve in the future....
    if human_second_move == 1:
        p1 = "O"
        break
    if human_second_move == 2:
        p2 = "O"
        break
    if human_second_move == 3:
        p3 = "O"
        break
    if human_second_move == 4:
        p4 = "O"
        break
    if human_second_move == 6:
        p6 = "O"
        break
    if human_second_move == 7:
        p7 = "O"
        break
    if human_second_move == 8:
        p8 = "O"
        break
    if human_second_move == 9:
        p9 = "O"
        break
# end of checkout

print('#' * 25)
print("Human move...")
print(f"{p1}{p2}{p3}\n{p4}{p5}{p6}\n{p7}{p8}{p9}\n")
print('#' * 25)


while True:     # machine third move
    print("Next Machine move is...")

    break

print('END')

