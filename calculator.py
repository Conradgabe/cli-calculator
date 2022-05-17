print('***************You can perform Addition, Substraction, Multiplications, Divisions and Modulo Operations*************\n')
print('----Enter add to perform Addition----\n'
      '----Enter sub to perform Substraction----\n'
      '----Enter mul to perform Multiplication----\n'
      '----Enter div to perform Division----\n'
      '----Enter mod to perform Modulo----\n'
    )

Operation = input('\t*******What Operation do you want to perform?---')
print('\n*******Note: Your other value will be addend, divisor....*******')

while True:
    End_program = input('Do you want to quit (press "q" to quit, press Enter to continue)? ') 
        
    if End_program == 'q':
        break
        
    try:
        value_1 = int(input('\nInput your first value (Press Enter to continue): '))
        value_2 = int(input('Input your other value: '))

        if Operation == 'add':
            print(f'-------------This is the Result:>>>>>>> { value_1 + value_2}\n')
            break
        if Operation == 'sub':
            print(f'-------------This is the Result:>>>>>>> { value_1 - value_2}\n')
            break
        if Operation == 'mul':
            print(f'-------------This is the Result:>>>>>>> { value_1 * value_2}\n')
            break
        if Operation == 'div':
            print(f'-------------This is the Result:>>>>>>> { value_1 / value_2}\n')
            break
        if Operation == 'mod':
            print(f'-------------This is the Result:>>>>>>> { value_1 % value_2}\n')
            break

    except:
        print('------------Input an integer value-----------')
        continue

Operation_2 = input('\t<<<<<<<*********Do you want to continue calculating (Enter "y" to continue or Enter "n" to end)? ************>>>>>>\n')

if Operation_2 == 'y':

    while True:
        End_program = input('Do you want to quit (Enter "q" to quit, press Enter to continue)? ') 
        
        if End_program == 'q':
            break
        Operation = input('\t*******What Operation do you want to perform?---')

        try:
            value_1 = int(input('\nInput your first value (Press Enter to continue): '))
            value_2 = int(input('Input your other value: '))

            if Operation == 'add':
                print(f'-------------This is the Result:>>>>>>> { value_1 + value_2}\n')
                print('Good Bye...')
                break
            if Operation == 'sub':
                print(f'-------------This is the Result:>>>>>>> { value_1 - value_2}\n')
                print('Good Bye...')
                break
            if Operation == 'mul':
                print(f'-------------This is the Result:>>>>>>> { value_1 * value_2}\n')
                print('Good Bye...')
                break
            if Operation == 'div':
                print(f'-------------This is the Result:>>>>>>> { value_1 / value_2}\n')
                print('Good Bye...')
                break
            if Operation == 'mod':
                print(f'-------------This is the Result:>>>>>>> { value_1 % value_2}\n')
                print('Good Bye...')
                continue

        except:
            print('------------Input an integer value-----------')
            continue
        
else:
    print('Alright, Good Bye :)')
