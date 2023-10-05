def cacti_number(plot):
    num = 0
    row = len(plot)
    idx = len(plot[0])

    for i in range(1,row):
        if len(plot[0]) != len(plot[i]):
            return 0

    for i in range(0, row):
        for j in range(0, idx):
            if plot[i][j] == 0:
               #four corners of the plot
                if i == 0 and j == 0:
                     if plot[i][j+1] == 0 and plot[i+1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                elif i == 0 and j == idx-1:
                    if plot[i][j-1] == 0 and plot[i+1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                elif i == row-1 and j == 0:
                    if plot[i][j+1] == 0 and plot[i-1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                elif i == row-1 and j == idx-1:
                    if plot[i][j-1] == 0 and plot[i-1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                #top row
                elif i == 0:
                    if plot[i][j-1] == 0 and plot[i][j+1] and plot[i+1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                #left-hand side
                elif j == 0:
                    if plot[i+1][j] == 0 and plot[i-1][j] == 0 and plot[i][j+1] == 0:
                        num +=1
                        plot[i][j] = 1
                #right-hand side
                elif j == idx-1:
                    if plot[i+1][j] == 0 and plot[i-1][j] == 0 and plot[i][j-1] == 0:
                        num +=1
                        plot[i][j] = 1
                #bottom row
                elif i == row-1:
                    if plot[i][j-1] == 0 and plot[i][j+1] == 0 and plot[i-1][j] == 0:
                        num += 1
                        plot[i][j] = 1
                #other cases
                elif i != 0 and i != row-1 and j != 0  and j != idx-1:
                    if plot[i][j-1] == 0 and plot[i][j+1] == 0 and plot[i+1][j] == 0 and plot[i-1][j] == 0:
                        num += 1
                        plot[i][j] = 1 
    return num