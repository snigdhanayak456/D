import math
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--principal', type=int, required=False, help='Enter the credit principal:')
parser.add_argument('--periods', type=int, required=False, help='Enter the number of periods:')
parser.add_argument('--interest', type=float, required=False, help='Enter the credit interest:')
parser.add_argument('--payment', type=float, required=False, help='Enter the credit payment:')
parser.add_argument('--type', type=str, required=False, help='type of payment: "annuity" or "diff"')
args = parser.parse_args()

if args.type is None:
    print('Incorrect parameters')

elif len(sys.argv) < 4:
    print("Incorrect parameters")

elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")

elif args.type == "diff":
    if args.principal is None or args.periods is None or args.interest is None or args.principal < 0 or args.periods < 0 or args.interest < 0:
        print("Incorrect Parameters")
    else:
        i = args.interest / (12 * 100)
        amount = []
        for m in range(1, int(args.periods + 1)):
            D = (args.principal / args.periods) + i * (args.principal - ((args.principal * (m - 1)) / args.periods))
            print(f'Month {m}: payment is {math.ceil(D)}')
            amount.append(math.ceil(D))
        Overpayment = sum(amount) - args.principal
        print('Overpayment =', Overpayment)

elif args.type == "annuity":
    if args.payment is None:
        if args.interest is None or args.principal < 0 or args.periods < 0 or args.interest < 0:
            print("Incorrect Parameters")
        else:
            i = args.interest / (12 * 100)
            A = (args.principal * i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1)
            overpayment = (args.periods * math.ceil(A)) - args.principal
            print(f'Your annuity payment = {math.ceil(A)}!')
            print(f'Overpayment = {math.ceil(overpayment)}')

    elif args.principal is None:
        if args.interest is None or args.payment < 0 or args.periods < 0:
            print("Incorrect Parameters")
        else:
            i = args.interest / (12 * 100)
            pr = args.payment * (math.pow(1 + i, args.periods) - 1) / (i * math.pow(1 + i, args.periods))
            overpayment = (args.periods * args.payment) - pr
            print(f'Your loan principal = {math.floor(pr)}!')
            print(f'Overpayment = {math.ceil(overpayment)}')

    elif args.periods is None:
        if args.interest is None or args.payment < 0 or args.principal < 0 or args.interest < 0:
            print("Incorrect Parameters")
        else:
            i = args.interest / (12 * 100)
            a = args.payment / (args.payment - i * args.principal)
            N = math.ceil(math.log(a, 1 + i))
            years = N // 12
            months = int(N % 12)
            overpayment = (N * args.payment) - args.principal
            if months == 0:
                print(f'It will take {years} years to repay this credit!')

            elif months == 1:
                print(f'It will take {months} month to repay this credit!')

            elif years == 1:
                print(f'It will take {years} year to repay this credit!')

            elif years == 0:
                print(f'It will take {months} months to repay this credit!')

            elif years == 1 and months > 1:
                print(f'It will take {years} year and {months} months to repay this credit!')

            elif years > 1 and months == 1:
                print(f'It will take {years} years and {months} month to repay this credit!')

            else:
                print(f'It will take {years} years and {months} months to repay this credit!')
            print(f'Overpayment = {math.ceil(overpayment)}')






