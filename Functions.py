import re


def is_duplicate(val, st):
    c_val = 0
    for i in st:
        if str(val) == i:
            c_val += 1
    if c_val > 1:
        return True
    else:
        return False


def u_name_validate(u_name):
    if u_name[0].isalpha():
        pass
    else:
        return False
    if bool(is_duplicate('@', u_name)):
        return False
    else:
        if bool(re.search('@', u_name)):
            pass
        else:
            return False
    if bool(is_duplicate('.', u_name)):
        if bool(re.search('.', u_name)):
            ind = 0
            for i in range(len(u_name)):
                if u_name[i] == '.':
                    ind = i
            if ind - u_name.index('@') > 2:
                pass
            else:
                return False

        else:
            return False

    else:
        if bool(re.search('.', u_name)):
            if u_name.index('.') - u_name.index('@') > 2:
                pass
            else:
                return False
        else:
            return False

    return True


def pwd_validate(pwd):
    if bool(re.search('[a-z]', pwd)):
        pass
    else:
        return False
    if bool(re.search('[A-Z]', pwd)):
        pass
    else:
        return False
    if any(map(str.isdigit, pwd)):
        pass
    else:
        return False
    if 5 < len(pwd) < 16:
        pass
    else:
        return False
    return True


def login():
    file1 = open('user_name_password.txt', 'r')
    test = list(map(str, file1.read().split('\n')))
    file1.close()
    upstring = []
    up_req = False
    valid = False
    x = input('Please enter your email: ')
    y = input('\nPlease enter your password: ')
    for i in test:
        uname, pword = map(str, i.split())
        if x == uname:
            valid == True
            if pword == y:
                print("login successful")
                break
            else:
                inp = input('Do you like to retreive the old password? \nIf yes type "Yes" \nif No provide a new password\n')
                if inp.upper() == 'YES':
                    print('Your old password is : ', pword)
                    exit()
                else:
                    if bool(pwd_validate(inp)):
                        pword = inp
                    else:
                        inp = input('Please enater valid passowoed with 1 Capital 1 Small and 1 digit also the password must be lessthan 16 chaarecters and less than 5 charecters:\n')
                        if bool(pwd_validate(inp)):
                            pword = inp
                            up_req = True
                        else:
                            print('entered wrong password exitting')
                            exit()
            i = uname + ' ' + pword
        upstring.append(i + '\n')
    if bool(valid):
        if bool(up_req):
            file1 = open('user_name_password.txt', 'w+')
            file1.writelines(upstring)
            file1.close()
    else:
        reg = input("User does not exist! Do you wish to Register?\nTo register Type 'Yes'\nTo exit Type 'No'\n")
        if reg.upper() == 'YES':
            register()
        else:
            exit()


def register():

    u_name = input('Please enter your emailid: ')
    pwd = input('\nPlease enter your new password\tPassword must contain: \n\t1 uppercase letter \n\t1 lowercase letter \n\t1 digit\n\tThe password must have atleaset 5 cahreccter and max of 16 charecters: ')
    # Chcek if the email already existed
    file1 = open('User_name_password.txt', 'r')
    test = list(map(str, file1.read().split('\n')))
    file1.close()
    for i in test:
        u_name_dat, pwd_dat = map(str, i.split())
        if u_name_dat == u_name:
            print("user already existed! Please try login")
            exit()

    file1 = open('user_name_password.txt', 'a+')
    if bool(u_name_validate(u_name)) and bool(pwd_validate(pwd)):
        x = '\n' + u_name + ' ' + pwd
        file1.writelines(x)
        file1.close()
        print("Successfully registered")
    else:
        if not bool(u_name_validate(u_name)):
            print('\nPlease enter valid email id')
        if not bool(pwd_validate(pwd)):
            print('\nPlease enter valid password')

