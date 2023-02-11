def main():
    print(get_avg())

def get_avg():
    add_marks = input("Do you want to add marks Y or N ?\n ")
    if add_marks == "y" or add_marks == "Y":
        n = int(input("Number of times : "))
        if n > 0:
            final_mark = 0
            for _ in range(n):
                mark = int(input("Enter mark : "))
                final_mark = final_mark + mark

        else:
            print("Invalid input!!!!")

    else:
        print("No mark to be added")

    avg = final_mark/ n

    return avg

main()
