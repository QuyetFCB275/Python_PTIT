def ThapHN(n, sour, bet, des):
    if (n == 1):
        print(f'{sour} -> {des}')
        return
    ThapHN(n-1, sour, des, bet)
    ThapHN(1, sour, bet, des)
    ThapHN(n-1, bet, sour, des)
    
if __name__ == "__main__":
    n = int(input())
    ThapHN(n, 'A', 'B', 'C')