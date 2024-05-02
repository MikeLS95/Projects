class NegativeError(Exception):
    pass


try:
    n = int(input('Enter an integer numerator: '))
    d = int(input('Enter an integer denominator: '))

    if n < 0 or d < 0:
        raise NegativeError()

    q = n / d

    print(q)

except ZeroDivisionError:
    print('Mate, you cannot divide by zero..')

except ValueError:
    print('Mate, only enter integers!')

except NegativeError:
    print('Positive numbers only mate.')

except Exception as e:
    print(f'Something went wrong: {e}')

else:
    # Happens if the entire try block executed successfully with no exceptions
    print('NOICE!')

finally:
    # Happens always, regardless of whether there was an exception or not
    print('You are done mate.')

# try:
    # open file for writing
    # write something to file - may cause exception
# except:
    # handle exception
# finally:
    # close file