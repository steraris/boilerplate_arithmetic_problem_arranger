def arithmetic_arranger(problems,solve=False):
    #Setting Variables
    arranged_problems = ''
    listed_problems = []
    top_row = ""
    bot_row = ""
    dashes = ""
    answers = ""
    answer = ""
    #Arranging the problems in a list
    for i in problems:
        a = i.split()
        listed_problems.append(a)
    # Error Handling
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems
    for i in listed_problems:
        if i[1] == '*' or i[1] == '/':
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems
        if len(i[0]) > 4 or len(i[2]) > 4:
            arranged_problems = 'Error: Numbers cannot be more than four digits.'
            return arranged_problems
        try:
            value_1 = int(i[0])
            value_2 = int(i[2])
        except:
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems

    #Solving the problems
    if solve == True:
        for i in listed_problems:
            if i[1] == '+':
                answer = str(int(i[0]) + int(i[2]))
                if len(i[0]) > len(i[2]):
                    answers += f'''{(' ')*((len(i[0])+2)-len(answer))}{answer}    '''
                if len(i[0]) < len(i[2]):
                    answers += f'''{(' ')*((len(i[2])+2)-len(answer))}{answer}    '''
                if len(i[0]) == len(i[2]):
                    answers += f'''{(' ')*((len(i[2])+2)-len(answer))}{answer}    '''
            if i[1] == '-':
                answer = str(int(i[0]) - int(i[2]))
                if len(i[0]) > len(i[2]):
                    answers += f'''{(' ')*((len(i[0])+2)-len(answer))}{answer}    '''
                if len(i[0]) < len(i[2]):
                    answers += f'''{(' ')*((len(i[2])+2)-len(answer))}{answer}    '''
                if len(i[0]) == len(i[2]):
                    answers += f'''{(' ')*((len(i[2])+2)-len(answer))}{answer}    '''

    # Making the top_row, bot_row and dashes
    for i in listed_problems:
        if len(i[0]) > len(i[2]):
            top_row += f'  {i[0]}    '
            bot_row += f'''{i[1]}{(' ') * ((len(i[0]) - len(i[2])) + 1)}{i[2]}    '''
            dashes += f'''{('-') * (len(i[0]) + 2)}    '''
        if len(i[0]) < len(i[2]):
            top_row += f'''{(' ') * ((len(i[2]) + 2) - len(i[0]))}{i[0]}    '''
            bot_row += f'''{i[1]} {i[2]}    '''
            dashes += f'''{('-') * (len(i[2]) + 2)}    '''
        if len(i[0]) == len(i[2]):
            top_row += f'''  {i[0]}    '''
            bot_row += f'''{i[1]} {i[2]}    '''
            dashes += f'''{('-') * (len(i[2]) + 2)}    '''



    # Removing the last four '    '
    top_row = top_row[:-4]
    bot_row = bot_row[:-4]
    dashes = dashes[:-4]
    answers = answers[:-4]

    #Adding the top_row, bot_row and dashes, into one string
    if solve == True:
        arranged_problems = '\n'.join((top_row,bot_row,dashes,answers))
    else:
        arranged_problems = '\n'.join((top_row,bot_row,dashes))

    return arranged_problems