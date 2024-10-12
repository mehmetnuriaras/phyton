import json

def writeUserList(userList):
    with open('notlar.txt', 'w') as file:
        json.dump(userList, file)
        

def getUserList():
    with open('notlar.txt','r') as file:
        userList=json.load(file)
    return userList

