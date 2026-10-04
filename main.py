import json
import random
import string
from pathlib import Path

class Bank:

    database = 'bank_management/data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                content = fs.read()
                data = json.loads(content) if content else []
        else:
            print("no such file exists ")
    except Exception as err:
        print(f"an exception occured as {err}")


    @staticmethod
    def __update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerated(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = spchar + num + alpha
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name" : input("enter your name : "),
            "age" : int(input("enter your age : ")) ,
            "email" : input("enter your email : "),
            "pin" : int(input("enter your  4 number pin : ")),
            # "accountNo": random.randint(1000, 9999),   # ✅ unique account number
            "accountNo" : Bank.__accountgenerated(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("sorry you cannot create your account")
        else:
            print("account has been created successfully ")

            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnum = input("please enter your account number : ")
        pin = int(input("please enter your pin number : "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no such data found! ")

        else:
            amount = int (input("how much money you want to deposit : "))
            if amount > 10000 or amount < 0:
                print("you can enter the amount between 10000 and 0 only.")
            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")
                print(userdata)

    def withdrawmoney(self):
        accnum = input("please enter your account number : ")
        pin = int (input("plrase enter your pin number : "))

        userdata =[i for i in Bank.data if i['accountNo']==accnum and i['pin']==pin]

        if userdata == False:
            print("sorry no such data found! ")
        else:
            amount = int (input("enter the amount of money you want to withdraw : "))
            if amount > userdata[0]['balance']:
                print("not sufficient balance!")
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrawn successfully")
                print(userdata)


    def showdetails(self):
        accnum = input("please enter your account number : ")
        pin = int (input("please enter your pin number : "))

        userdata =[i for i in Bank.data if i['accountNo']==accnum and i['pin']==pin]

        if userdata == False:
            print("sorry no such data found! ")
        else:
            for i in userdata[0]:
                print(f" {i} : {userdata[0][i]}")
        

    def updatedetails(self):
        accnum = input("please enter your account number : ")
        pin = int (input("please enter your pin number : "))

        userdata =[i for i in Bank.data if i['accountNo']==accnum and i['pin']==pin]

        if userdata == False:
            print("sorry no such data found! ")
        else:
            print("you cannot change age, account number and balance!")
            print("Fill the details or leave it empty if no change!")

            newdata ={
                "name" : input("enter new name or press enter to skip : " ),
                "email" : input("enter new email or press enter to skip : " ),
                "pin" : input("enter new pin or press enter to skip : " )
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Details are updated successfully!")

    def delete(self):
        accnum = input("please enter your account number : ")
        pin = int (input("please enter your pin number : "))

        userdata =[i for i in Bank.data if i['accountNo']==accnum and i['pin']==pin]

        if userdata == False:
            print("sorry no such data found! ")
        else:
            check = input("press y if you actually want to delete the account!")
            if check == 'y' or check == 'Y':
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                Bank.__update()
                print("Account deletd successfully!")
            else:
                print("Account deletion bypassed!")


user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in an account")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response : "))

if check == 1:
    user.createaccount()

if check == 2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()
