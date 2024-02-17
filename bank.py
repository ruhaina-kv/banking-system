'''Write a Python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal'''
#additional feature added is to quit
#google drive link: https://drive.google.com/file/d/1LaRn8NN9CQyZ8ZGR18-AqXEjjn0d5qwp/view?usp=drive_link

import random
def main():
    print("WELCOME TO THE BANKING SYSTEM")
    name_list, acc_num_list, acc_blc_list = read_file()
    option = 0
    while option != 4:
        banking_menu = ["1. ACCOUNT LOGIN.","2. AMOUNT DEPOSITION","3. AMOUNT WITHDRAWAL","4. QUIT"]
        for option in banking_menu:
            print(option)
        user_input = False
        while not user_input:
            try:
                option = int(input("please enter an option: "))
                if 0<option<5:
                    user_input = True
                else:
                    print("\n plese enter a valid option\n")
                    for option in banking_menu :
                        print(option)
            except:
                print("\n ERROR---- please enter a valid option")
                for option in banking_menu :
                    print(option)
        if option==1:
            name_list ,acc_num_list ,acc_blc_list = open_acc(name_list ,acc_num_list ,acc_blc_list)
        elif option==2:
            name_list, acc_num_list, acc_blc_list = cash_in(name_list, acc_num_list, acc_blc_list)
        elif option==3:
            name_list, acc_num_list, acc_blc_list = cash_out(name_list, acc_num_list, acc_blc_list)
        elif option==4:
            exit(name_list ,acc_num_list ,acc_blc_list)
def read_file():
    name_list = []
    acc_num_list = []
    acc_blc_list = []
    f = open("bank","r")
    lines = f.readlines()
    for line in lines:
        information = line.split()
        acc_num_list.append(information[0])
        name_list.append(information[1])
        acc_blc_list.append(float(information[2]))
    return name_list , acc_num_list , acc_blc_list

def open_acc(name_list ,acc_num_list ,acc_blc_list):
    name = input("Please enter your name: ")
    print("Your name: ",name)
    name_list .append(name)
    number=str(random.randint(1,100000) )
    print("your account number : ", number)
    acc_num_list.append(number)
    acc_blc_list .append(0.0)
    return name_list , acc_num_list , acc_blc_list
def cash_in(name_list ,acc_num_list ,acc_blc_list):
    account_number = input("\nEnter your account number:\n")
    index = 0
    acc = False
    for i in acc_num_list :
        if i == account_number :
            acc = True
            break
        index = index +1
    if acc :
        problem = True
        while problem :
            try:
                deposit_amount =  float (input("Enter the amount you want to deposite: "))
                if deposit_amount < 0:
                    print("ERROR--- imput a valid amount.")
                    break
                amount= acc_blc_list [index] + deposit_amount
                if amount > 0:
                    acc_blc_list [index] = acc_blc_list [index] + deposit_amount
                    print("An amount of ",deposit_amount ,"is added to your account")
                    print("Your current balance is ",acc_blc_list [index])
                    problem = False
                else:
                    print("ERROR--- imput a valid amount")
                    print("Your current balance is ", acc_blc_list[index])
                    break
            finally:
                return name_list ,acc_num_list ,acc_blc_list
    else:
        print("\nsorry the account number does not exist.\n ")
        return name_list ,acc_num_list ,acc_blc_list
def cash_out(name_list ,acc_num_list ,acc_blc_list):
    account_number = input("\nEnter your account number:\n")
    index = 0
    acc = False
    for i in acc_num_list:
        if i == account_number:
            acc = True
            break
        index = index + 1
    if acc:
        problem = True
        while problem:
            try:
                withdraw_amount = float(input("Enter the amount you want to withdraw:"))
                if withdraw_amount < 0 :
                    print("ERROR----enter a valid amount")
                    break
                amount = acc_blc_list [index] - withdraw_amount
                if amount > 0:
                    acc_blc_list [index] = acc_blc_list [index] - withdraw_amount
                    print("an amount of ",withdraw_amount ," is removed from your account")
                    print("your current balance is ",acc_blc_list [index])
                    problem = False
                else:
                    print("you dont have enough balance to withdraw this amount ")
                    print("your current balance is ",acc_blc_list [index])
                    break
            finally:
                return name_list ,acc_num_list ,acc_blc_list
    else:
        print("\nsorry the account number does not exist\n ")
        return name_list ,acc_num_list ,acc_blc_list
def exit(name_list ,acc_num_list ,acc_blc_list):
    print("THANK YOU FOR USING THIS BANKING SYSTEM")
    quit_file = open("bank","w")
    for i in range(len(acc_num_list)):
        save = acc_num_list [i] +" "+name_list [i]+" "+str (acc_blc_list [i])+"\n"
        quit_file.write(save)
    quit_file.close()
main()