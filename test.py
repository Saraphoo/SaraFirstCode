
def main():
    weeklyHour = int(input("How many hours did you work: "))
    ratePay = float(input("Your rate of Pay: "))
    overTime = (weeklyHour - 40)
    overTimePay = 0
    if (overTime > 0):
        overTimePay = (overTime * (ratePay * 1.5))
    grossPay = ((weeklyHour * ratePay) + overTimePay)
    print(f'grosspay: {grossPay}\n')
    if (grossPay > 401):
        netPay = (grossPay - ((grossPay - 400) *.05))
        print(f'Your netpay is under 400 {netPay}')
        if (netPay > 1000):
            netPay = (netPay - ((netPay - 1000) * .10))
            print(f'Your netpay is over 1000 {netPay}')
      

if __name__ == "__main__":
    main()