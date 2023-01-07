while True:
    print(('who are you?\n') +'Input your name: ')
    name_input = input().lower()
    if name_input != 'xj':
        print('Put wrong name. Again!')
        continue

    print('Hello xj, what is the password (It is a plant in your department)')
    pswd_input = input().lower()
    if pswd_input == 'cereus':
        break
    print('Put wrong password. Again!')
print ('Access granted.')