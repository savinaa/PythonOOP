matrix= [ [ i for i in input().split(' ') ] for j in range(8) ]

def find_symbol(symbol):
    for row in range(8):
        for col in range(8):
            if matrix[row][col]==symbol:
                return row,col

king_pos:tuple=find_symbol('K')
list_of_queens=[]
for row in range(8):
    for col in range(8):
        if matrix[row][col]=='Q':
            queen_pos=row,col
            list_of_queens.append(queen_pos)


def checkVerticals(tup):
    queen_row, queen_col=tup
    king_row, king_col=king_pos
    if king_col!=queen_col:
        return False
    for position in range(min(king_row,queen_row)+1,max(king_row,queen_row)):
        if matrix[position][king_col]=='Q':
            return False
    else:
            return True


def checkHorizontals():
    queen_row, queen_col=tup
    king_row, king_col=king_pos
    if king_row!=queen_row:
        return False
    for position in range(min(king_col,queen_col)+1,max(king_col,queen_col)):
        if matrix[king_row][position]=='Q':
            return False
    else:
            return True

def checkDiagonals():
    queen_row, queen_col=tup
    king_row, king_col=king_pos
    row_diff=abs(queen_row-king_row)
    col_diff=abs(queen_col-king_col)
    if row_diff!=col_diff:
        return False
    else:
        queen_direction=0
        if king_col>queen_col:
            queen_direction=1 #QK
        else:
            queen_direction=-1 #KQ
        if queen_direction == 1:
            for position in range(min(king_row, queen_row) + 1, max(king_row, queen_row)):
                queen_col+=1
                if matrix[position][queen_col]=='Q':
                    return False
            else:
                return True
        else:
            for position in range(min(king_row, queen_row) +1, max(king_row, queen_row)):
                queen_col-=1
                if matrix[position][queen_col]=='Q':
                    return False
            else:
                return True



result_list=[]
for tup in list_of_queens:
   if checkVerticals(tup) or checkHorizontals() or checkDiagonals():
       result_list.append(tup)


if result_list:
    for tup in result_list:
        row,col=tup
        print(f'[{row}, {col}]')
else:
    print(f'The king is safe!')
