def arithmetic_arranger(problems, ans=False):
    top_equation = ""
    bottom_equation = ""
    final_dash = ""
    answer = ""

    # Possible Error 1
    # If there are more than 5 problems.
    if not len(problems) > 5:
        # Looping through each problem
        for i in problems:

            # Possible Error 2
            # If the operators are not addition or subtraction.
            if '+' in i or '-' in i:
                expr = i.partition('+') if '+' in i else i.partition('-')
            else:
                print("Error: Operator must be '+' or '-'.")
                break

            # Possible Error 3
            # If the input given is not a number.
            if expr[0].strip().isdigit() and expr[2].strip().isdigit():
                first = int(expr[0])
                oper = expr[1]
                second = int(expr[2])
            else:
                print('Error: Numbers must only contain digits.')
                break

            # Possible Error 4
            # If the number length is greater than four.
            if len(expr[0].strip()) > 4 or len(expr[2].strip()) > 4:
                print('Error: Numbers cannot be more than four digits.')
                break

            if first == second:
                # Returning the string
                top = f"  {expr[0].strip()} " + "    "
                bottom = f"{oper} {expr[2].strip()} " + "    "

                dash_length = len(expr[0].strip()) + 2
                dash = f'{"-" * dash_length}' + "     "
            else:
                # Find the biggest number
                greatest = first if first > second else second
                great = str(greatest)

                # Returning the string
                x = len(great) - len(expr[0].strip())
                y = len(great) - len(expr[2].strip())

                top = "  " + f"{' ' * x}" + str(expr[0].strip()) + "    "
                bottom = f'{oper}' + " " + f'{" " * y}' + str(expr[2].strip()) + "    "

                dash_length = len(f'{oper}' + " " + f'{" " * y}' + str(expr[2].strip()))
                dash = f'{"-" * dash_length}' + f'{" " * 4}'

            if ans:
                whitespace = dash_length - len(str(eval(i)))
                answer += f'{" "*whitespace}{eval(i)}    ' if not first == second else f'{" "*whitespace}{eval(i)}     '

            top_equation += top
            bottom_equation += bottom
            final_dash += dash

    # If the number of problems is greater than 5 then an error is returned.
    else:
        print('Error: Too many problems.')

    print(top_equation)
    print(bottom_equation)
    print(final_dash)
    print(answer)


arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'], True)
