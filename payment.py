a = int(input('enter amount to withdraw : '))
balance = 50000

if a>balance :
    print('insufficient balance')
elif a==balance:
    balance-=a
    print('transaction successful')
    print(f"balance left : {balance} you need to maintain minimum balance of 2000")
else:
    balance-=a
    print('transaction successful')
    print(f"balance left : {balance}")