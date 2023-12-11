def topple_dominoes(dominoes):
    n = len(dominoes)
    touched = [0] * n  # 记录每个多米诺骨牌被触碰到的次数
    stack = [-1]  # 单调栈，保存多米诺骨牌的索引，初始加入虚拟多米诺骨牌

    for i in range(n):
        x, h = dominoes[i]  # 获取当前多米诺骨牌的坐标和高度

        # 处理栈中所有能够被当前多米诺骨牌推倒的骨牌
        while stack and dominoes[stack[-1]][0] < x + h - 1:
            idx = stack.pop()  # 弹出栈顶多米诺骨牌的索引
            if dominoes[idx][0] > x:  # 之前的多米诺骨牌的坐标 x 大于当前多米诺骨牌的坐标 x
                touched[i] += touched[idx]  # 将之前弹出的多米诺骨牌的触碰次数累加到当前多米诺骨牌上

        # 将当前多米诺骨牌入栈
        stack.append(i)

    return touched


# 主程序
while True:
    try:
        n = int(input())  # 输入多米诺骨牌的数量
        dominoes = []
        for _ in range(n):
            x, h = map(int, input().split())  # 输入多米诺骨牌的坐标和高度
            dominoes.append((x, h))

        touched = topple_dominoes(dominoes)  # 模拟多米诺骨牌的倒下过程

        # 输出每个多米诺骨牌被触碰到的次数
        for i in range(n):
            print(touched[i], end=' ')
        print()

    except EOFError:
        break
