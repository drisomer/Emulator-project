# decimal to binary list conversion
def decimal_to_binary_list(num):
    binary_list = [0]*8

    binary_list[0] = num//128
    num -= 128 * binary_list[0]

    binary_list[1] = num//64
    num -= 64 * binary_list [1]

    binary_list[2] = num//32
    num -= 32 * binary_list[2]

    binary_list[3] =num//16
    num -=16 * binary_list[3]

    binary_list [4] = num//8
    num -= 8 * binary_list[4]
    
    binary_list [5] = num//4
    num -= 4 * binary_list[5]

    binary_list [6] = num//2
    num -= 2* binary_list[6]

    binary_list [7] = num//1
    num -= 1* binary_list[7]

    return binary_list

def decimalBin2twos_complement(num, bit_position=7):
    if num >= 0:
        return bin(num)[2:].zfill(8)
    else:
        if bit_position < 0:
            raise ValueError("Binary rep requires 8 bits")
        abs_binary = decimalBin2twos_complement(abs(num), bit_position - 1)
        inverted_bit = "1" if abs_binary[bit_position] == "0" else "0"
        return abs_binary[:bit_position] + inverted_bit + abs_binary[bit_position + 1:]

#converting a non-negative binary num to decimal
def base2list_to_unsigned (base2list):
    def loop (base2list, acc, pow2):
        if not base2list:
            return acc
        else:
            return loop(base2list[1:], acc + (base2list[0] * pow2), pow2 // 2)
    return loop(base2list, 0, 128)
#binary_list = [1, 0, 1, 1, 0, 1, 0, 1]
#result = base2list_to_unsigned(binary_list)
#print(result)

#Binary Addition Operation
def decimal_to_binary(decimal):
    return bin(int(decimal) & 0xFF)[2:].zfill(8)  # Use 8 bits for binary representation

def binary_addition(bin_num1, bin_num2):
    length = max(len(bin_num1), len(bin_num2))
    bin_num1 = bin_num1.zfill(length)
    bin_num2 = bin_num2.zfill(length)

    result = ''
    carry = 0

    for i in range(length - 1, -1, -1):
        digit1 = int(bin_num1[i])
        digit2 = int(bin_num2[i])
        temp_sum = digit1 + digit2 + carry

        result = str(temp_sum % 2) + result
        carry = temp_sum // 2

    if carry:
        result = '1' + result

    return result

def binary_subtraction(bin_num1, bin_num2):
    length = max(len(bin_num1), len(bin_num2))
    bin_num2 = bin_num2.zfill(length)

    # Take the two's complement of bin_num2
    #bin_num2 = ''.join('1' if bit == '0' else '0' for bit in bin_num2)
    inverted_bits = '' .join('1' if bit == '0' else '0' for bit in bin_num2)
    # Add 1 to complete the two's complement
    bin_num2 = binary_addition(inverted_bits, '00000001')

    result = binary_addition(bin_num1, bin_num2)
     # If the result is longer than expected, remove the leading 1
    if len(result) > length:
        result = result[1:]
    return result

def perform_binary_subtraction(num1, num2):
    binary_num1 = decimal_to_binary(num1)
    binary_num2 = decimal_to_binary(num2)

    result = perform_binary_subtraction(binary_num1, binary_num2)

    return result
''' print(f"1. {num1} --> {binary_num1}")
    print(f"2. {num2} --> {binary_num2} (two's complement)")
    print("============================")

    binary_result = binary_subtraction(binary_num1, binary_num2)

    print(f"{num1 - num2} --> {binary_result}")'''

###########################
def add_binary(a, b, carry =0, result =" "):
    if not a and not b and not carry:
        return result
    bit_a = int(a[-1]) if a else 0
    bit_b = int(b[-1]) if b else 0

    current_sum = bit_a ^ bit_b ^ carry
    current_carry = (bit_a & bit_b) | (bit_b & carry) | (bit_a & carry)

    next_result = str(current_sum) + result
    return add_binary(a[: -1], b[: -1], current_carry, next_result)


def binary_Add (num1, num2):
    binary_num1 = format(num1, "08b")[2: ]
    binary_num2 = format(num2, "08b") [2: ]

    max_length = max(len(binary_num1), len(binary_num2), 8)
    binary_num1 = binary_num1.zfill(8)
    binary_num2 = binary_num2.zfill(8)


    result = add_binary(binary_num1, binary_num2)

    return result

#AND logical function
def bitwise_AND(x, y, result=0, bit_position=0):
    if x == 0 or y == 0:
        return result
    elif x % 2 == 1 and y % 2 == 1:
        return bitwise_AND(x // 2, y // 2, result + (1 << bit_position), bit_position + 1)
    else:
        return bitwise_AND(x // 2, y // 2, result, bit_position + 1)

#OR logial function
    
#####################
def bitwise_OR(x, y, result = 0, bit_position =0 ):
    if x == 0 and y ==0:
        return result
    elif x % 2 == 1 or y % 2 ==1:
        return bitwise_OR(x // 2, y // 2, result + (1 << bit_position), bit_position +1 )
    else:
        return bitwise_OR( x // 2, y // 2, result, bit_position + 1) 

###################
#XOR logical function
def bitwise_XOR(x, y ):
    result = 0 
    bit_position =0
    
    while x > 0 or y > 0:
        if (x % 2) != (y % 2):
            result += 1 << bit_position 
        x //= 2
        y //= 2
        bit_position +=1 
    return result

#NOT logical function
def bitwise_NOT(x, bit_position=7):
    return (~x) & ((1 << bit_position + 1) - 1)
#else:
  #      return bitwise_NOT(x // 2, bit_position + 1) + ((x % 2) ^ 1) << bit_position

#########################################################
def decimal_to_binary(decimal):
    return bin(int(decimal) & 0xFF)[2:].zfill(8)  # Use 8 bits for binary representation

def hex_to_binary(hex_num):
    return bin(int(hex_num, 16))[2:].zfill(8)

def input_to_binary(input_str):
    if input_str.startswith("0x"):
        return hex_to_binary(input_str)
    else:
        return decimal_to_binary(input_str)

def main():
    print("Select Operation Type to Perform")
    print("1. Arithmetic Operation")
    print("2. Logical Operation")

    choice = int(input("Select your choice (1 or 2): "))

    if choice == 1:
        operation_choice = input("Choose operation (+ for Addition, - for Subtraction): ")
        num1_str = input("Enter the first number (decimal or hexadecimal): ")
        num2_str = input("Enter the second number (decimal or hexadecimal): ")

        binary_num1 = input_to_binary(num1_str)
        binary_num2 = input_to_binary(num2_str)

        if operation_choice == "+":
            result = binary_addition(binary_num1, binary_num2)
            print(f"1. {num1_str} --> {binary_num1}")
            print(f"2. {num2_str} --> {binary_num2}")
            print("========================")
            print(f"4. {int(num1_str, 0) + int(num2_str, 0)} --> {result}")
        elif operation_choice == "-":
            result = binary_subtraction(binary_num1, binary_num2)
            print(f"1. {num1_str} --> {binary_num1}")
            print(f"2. {num2_str} --> {binary_num2}")
            print("=========================")
            print(f"4. {int(num1_str, 0) - int(num2_str, 0)} --> {result} (two's complement)")
        else:
            print("Error! Invalid Operation Selected: Enter + for addition or - for subtraction")
    elif choice == 2:
        print("Select Logical Operation:")
        print("1. AND")
        print("2. OR")
        print("3. XOR")
        print("4. NOT")

        bitwise_choice = int(input("Select your choice (1 - 4): "))
        if bitwise_choice == 4:
            x = int(input("Enter the number for NOT operation in hexadecimal format: "), 16)
            operation = "NOT"
            x_bin = format(x, '08b')
            print(f"{operation} {x}")
            print(f"1. {x_bin}")

            result = bitwise_NOT(x)
            result_bin = format(result, '08b')
            print("========================")
            print(f"3. {result} --> {result_bin}")
        elif 1 <= bitwise_choice <= 3:
            x = int(input("Enter the first number in hexadecimal format: "), 16)
            y = int(input("Enter the second number in hexadecimal format: "), 16)

            if bitwise_choice == 1:
                result = bitwise_AND(x, y)
                operation = "AND"
            elif bitwise_choice == 2:
                result = bitwise_OR(x, y)
                operation = "OR"
            elif bitwise_choice == 3:
                result = bitwise_XOR(x, y)
                operation = "XOR"

            x_bin = format(x, '08b')
            y_bin = format(y, '08b')

            print(f"{operation} Operation")
            print(f"1. {x} --> {x_bin}")
            print(f"2. {y} --> {y_bin}")

            result_bin = format(result, '08b')
            print("=========================")
            print(f"4. {result} --> {result_bin}")
        else:
            print("Error! Invalid choice selected. Enter a number between 1 and 4")
    else:
        print("Error! Invalid Operation Type. Enter a number between 1 and 2")


if __name__ == "__main__":
    main()
