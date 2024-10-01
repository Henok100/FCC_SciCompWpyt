def arithmetic_arranger(problems, show_answers=True):
    first_line = []
    second_line = []
    dash = []
    resutls = []
    if len(problems) > 5:
        print("Error: Too many problems.")
        return 
    #1 separate lists(problems)
    for problem in problems:
        #2 get operand, operator
        ans = None
        op1 = problem.split()[0]
        len1 = len(op1)
        if len1 > 4:
            print("Error: Numbers cannot be more than four digits.")
            return 
        if not op1.isdigit():
            print("Error: Numbers must only contain digits.")
            return 

        op = problem.split()[1]

        op2 = problem.split()[2]
        len2 = len(op2)
        if len2 > 4:
            print("Error: Numbers cannot be more than four digits.")
            return 
        if not op2.isdigit():
            print("Error: Numbers must only contain digits.")
            return 
        
        if op == '+':
            ans = int(op1) + int (op2)
        elif op == '-':
            ans = int(op1) - int(op2)
        else:
            #error
            print("Error: Operator must be '+' or '-'.")
            return 
        
        totalSpace = max(len2, len1) + 2
        spaces_1 = ' '*(totalSpace - len1) # For op1
        spaces_2 = ' '*(totalSpace - len2-1) #for op2
        dashes = '-'*totalSpace # dashes before the result

        if ans > 0 and show_answers: #
            rspaces = ' '*(totalSpace - len(str(ans)))
        else:
            rspaces = ' '*(totalSpace - 1 - len(str(ans)))

        first_line.append(spaces_1)
        first_line.append(op1)
        first_line.append('    ')
        second_line.append(op)
        second_line.append(spaces_2)
        second_line.append(op2)
        second_line.append('    ')
        dash.append(dashes)
        dash.append('    ')
        if ans > 0:
            resutls.append(rspaces)
            resutls.append(str(ans))
            resutls.append('    ')
        else:
            resutls.append(rspaces)
            resutls.append(str(ans))
            resutls.append('    ')
    print(f"{''.join(first_line)}\n{''.join(second_line)}\n{''.join(dash)}")
    if show_answers:
        print(f"{''.join(resutls)}")
    return

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])