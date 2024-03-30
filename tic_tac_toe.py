# 初始化棋盘位置
position1 = position2 = position3 = position4 = position5 = position6 = position7 = position8 = position9 = ' '

# 打印初始棋盘
def print_board():
    print(f"{position1}{position2}{position3}")
    print(f"{position4}{position5}{position6}")
    print(f"{position7}{position8}{position9}")

# 判断游戏是否结束
def check_winner():
    # 检查每行
    for i in range(0, 9, 3):
        if position1 == position2 == position3 != ' ':
            return position1
        elif position4 == position5 == position6 != ' ':
            return position4
        elif position7 == position8 == position9 != ' ':
            return position7
    # 检查每列
    for i in range(3):
        if position1 == position4 == position7 != ' ':
            return position1
        elif position2 == position5 == position8 != ' ':
            return position2
        elif position3 == position6 == position9 != ' ':
            return position3
    # 检查对角线
    if position1 == position5 == position9 != ' ':
        return position1
    elif position3 == position5 == position7 != ' ':
        return position3
    # 检查是否平局
    if ' ' not in [position1, position2, position3, position4, position5, position6, position7, position8, position9]:
        return 'Tie'
    return None

# 初始化变量
turn = 0

# 游戏循环
while True:
    # 判断当前玩家
    if turn % 2 == 0:
        player = "User one\'s"
        symbol = "o"
    else:
        player = "User two\'s"
        symbol = "x"
    
    # 提示玩家输入位置
    valid_input = False
    while not valid_input:
        position = int(input(f"""{player} turn to input now.
Select input position 1~9："""))
        if position < 1 or position > 9:
            continue
        elif position == 1 and position1 == ' ':
            position1 = symbol
            valid_input = True
        elif position == 2 and position2 == ' ':
            position2 = symbol
            valid_input = True
        elif position == 3 and position3 == ' ':
            position3 = symbol
            valid_input = True
        elif position == 4 and position4 == ' ':
            position4 = symbol
            valid_input = True
        elif position == 5 and position5 == ' ':
            position5 = symbol
            valid_input = True
        elif position == 6 and position6 == ' ':
            position6 = symbol
            valid_input = True
        elif position == 7 and position7 == ' ':
            position7 = symbol
            valid_input = True
        elif position == 8 and position8 == ' ':
            position8 = symbol
            valid_input = True
        elif position == 9 and position9 == ' ':
            position9 = symbol
            valid_input = True
        else:
            continue
    
    # 打印当前棋盘
    print_board()
    
    # 判断游戏是否结束
    winner = check_winner()

    if winner == 'o':
        winner = 'user1'
        
    elif winner == 'x':
        winner = 'user2'
    
    if winner is not None:
        if winner == 'Tie':
            print("Tie")
        else:
            print(f"{winner} win")
        break
    
    # 轮到下一位玩家
    turn += 1

