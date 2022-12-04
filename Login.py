import re


def u_name_validate(u_name):
    if u_name[0].isalpha():
        pass
    else:
        return False
    if bool(re.search('@', u_name)):
        pass
    else:
        return False
    if bool(re.search('.', u_name)):
        if u_name.index('.') - u_name.index('@') > 2:
            pass
        else:
            return False
    else:
        return False
    #print('correcct username')
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
    if any(map(str.isdigit,pwd)):
        pass
    else:
        return False
    if 5 < len(pwd) < 16:
        pass
    else:
        return False
    #print('Correct pass')
    return True


def login():
    file1 = open('userr_name_password.txt', 'r')
    test = list(map(str, file1.read().split('\n')))
    file1.close()
    #print(test)
    upstring = []
    up_req = False
    valid = False
    x = input('Please enter your email')
    y = input('\nPlease enter your password')
    for i in test:
        uname, pword = map(str, i.split())
        if x == uname:
            valid == True
            if pword == y:
                print("login successful")
                break
            else:
                inp = input('Do you like to retrive the old password? if "Yes" else provide a new password')
                if inp.upper() == 'YES':
                    print(pword)
                    exit()
                else:
                    if bool(pwd_validate(inp)):
                       pword = inp
                    else:
                        inp =input('Please enater valid passowoed with 1 Capital 1 Small and 1 digit also the password must be lessthan 16 chaarecters and less than 5 charecters:\n')
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
            file1 = open('userr_name_password.txt', 'w+')
            file1.writelines(upstring)
            file1.close()
    else:
        reg = input("User does not exist! Do you wish to Register?\nTo register Type 'Yes'\nTo exit Type 'No")
        if reg.upper() == 'YES':
            register()
        else:
            exit()


def register():
    file1 = open('userr_name_password.txt', 'a+')

    u_name = input('Please enter your emailid: ')
    pwd = input('\nPlease enter your new password\bPassword must contain 1 uppercase letter \n1 lowercase letter \n1 digit\nThe password must have atleaset 5 cahreccter and max of 16 charecters')

    if bool(u_name_validate(u_name)) and bool(pwd_validate(pwd)):
        x = '\n' + u_name + ' ' + pwd
        file1.writelines(x)
        file1.close()
        print("Successfully registered")


log_reg = int(input("If you are an existing user please lggin else Register. \nPress: \n\t1 - To log in \n\t2 - to Register\n\t"))
if log_reg == 1:
    login()
elif log_reg ==2:
    register()
