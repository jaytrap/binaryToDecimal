# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
def bit_to_dec():
    dc_num = 0
    bin_num = str(input("Enter a binary number: "))
    if not bin_num:
        print("Please enter a valid binary number.")
    else:

        for n in range(len(bin_num) - 1, -1, -1):
            if bin_num[n] != '0' and bin_num[n] != '1':
                print('Enter a valid binary number')
                exit()
            elif bin_num[n] != '0':
                dc_num += 2 ** (len(bin_num) - 1 - n)
        print(f"In decimal: {dc_num}")


def bit_to_dec_1():
    dc_num = 0
    bin_num = str(input("Enter a binary number: "))
    counter = len(bin_num)
    if not bin_num:
        print("Please _____")
    else:
        print(counter)
        print(bin_num)
        print(bin_num[counter - 1])
        while counter > 0:
            if bin_num[counter - 1] != '0' and bin_num[counter - 1] != '1':
                print('Enter a valid binary number')
                exit()
            elif bin_num[counter - 1] != '0':
                dc_num += 2 ** (counter-1)
                counter -= 1
            else:
                counter -= 1
        print(f"In decimal: {dc_num}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bit_to_dec_1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
