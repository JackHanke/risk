from numpy import zeros

# NOTE this function returns the probability of a attackers beating b defenders in the board game RISK
def get_risk_probability(a, b):
    table = zeros((a+1, b+1))
    for i in range(2,a+1): table[i][0] = 1
    for i in range(3,a+1): table[i][1] = 1-(21/36)*(91/216)*(441/1296)**(i-3)
    for j in range(1,b+1): table[2][j] = (15/36)*(55/216)**(j-1)

    temp = table[3][0]
    for j in range(2,b+1,2): 
        temp = (295/1296)*temp + (15/36)*(420/1296)*(55/216)**(j-2)
        table[3][j] = temp

    temp = table[3][1]
    for j in range(3,b+1,2): 
        temp = (295/1296)*temp + (15/36)*(420/1296)*(55/216)**(j-2)
        table[3][j] = temp

    for i in range(4,a+1):
        for j in range(2,b+1):
            table[i][j] = (2890/7776)*table[i][j-2] + (2611/7776)*table[i-1][j-1] +(2275/7776)*table[i-2][j]

    return table[a][b]

if __name__ == '__main__':
    a, b = 5, 2
    prob_val = get_risk_probability(a=a, b=b)
    print(f'\nProbability of {a} attackers defeating {b} defenders in RISK is {100*prob_val:.4f}%\n')
