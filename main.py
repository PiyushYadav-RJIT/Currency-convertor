from forex_python.converter import CurrencyRates

c = CurrencyRates()
con = 'yes'
while con.lower() == 'yes':
    print('Enter the currency you want to convert from (e.g., USD):')
    from_currency = input().upper()
    print('Enter the currency you want to convert to (e.g., EUR):')
    to_currency = input().upper()
    print('Enter the amount you want to convert:')
    
    try:
        amount = float(input())
        result = c.convert(from_currency, to_currency, amount)
        print(f'{amount} {from_currency} is equal to {result:.2f} {to_currency}.')
    except ValueError:
        print('Invalid amount entered. Please enter a valid number.')
    except Exception as e:
        print(f'Error: {e}')
    
    print('Do you want to convert again? (yes/no)')
    con = input().lower()

print('Goodbye!')
