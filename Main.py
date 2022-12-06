import functions

log_reg = int(input("If you are an existing user please lggin else Register. \nPress: \n\t1 - To log in \n\t2 - to Register\n\t"))
if log_reg == 1:
    functions.login()
elif log_reg == 2:
    functions.register()
