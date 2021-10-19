def arithmetic_arranger(problems, ans=False):
    top_equation = ""
    bottom_equation = ""
    final_dash = ""
    answer = ""
    answer_exists = ""

    # Possible Error 1
    # If there are more than 5 problems.
    if not len(problems) > 5:
        # Looping through each problem
        for i in problems:

            # Possible Error 2
            # If the operators are not addition or subtraction.
            if '+' in i or '-' in i:
                expr = i.partition('+') if '+' in i else i.partition('-')
                first_num = expr[0].strip()
                second_num = expr[2].strip()

                # Possible Error 3
                # If the input given is not a number.
                if first_num.isdigit() and second_num.isdigit():
                    operator = expr[1]
                else:
                    return 'Error: Numbers must only contain digits.'

                # Possible Error 4
                # If the number length is greater than four.
                if len(first_num) > 4 or len(second_num) > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                else:
                    num_length = len(max([first_num, second_num], key=len))
                    top = f"{first_num.rjust(num_length + 2)}    "
                    bottom = f"{operator}{second_num.rjust(num_length + 1)}    "
                    dash = f"{'-' * (num_length + 2)}    "
            else:
                return "Error: Operator must be '+' or '-'."

            top_equation += top
            bottom_equation += bottom
            final_dash += dash
            if ans:
                answer += f"{str(eval(i)).rjust(num_length + 2)}    "
                answer_exists = "\n"

        return f"{top_equation.rstrip()}\n{bottom_equation.rstrip()}\n{final_dash.rstrip()}{answer_exists}{answer.rstrip()}"

    # If the number of problems is greater than 5 then an error is returned.
    return 'Error: Too many problems.'
