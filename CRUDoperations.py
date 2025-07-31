import json

#load JSON file
def read_data():
    with open('data.json', "r") as f:
        return json.load(f)

def write_data(data):        
    with open('data.json', "w") as f:
        json.dump(data,f,indent = 4)

#CRUD operations
def create_user(user):
    data = read_data()
    data.append(user)
    write_data(data)
    print('user added successfully')

def read_user():
    data = read_data()
    print(data)

def update_user(user_id,updated_fields):
    data = read_data()
    found = False
    for user in data:
        if user['id'] == user_id:
            user.update(updated_fields)
            found = True
            break
    if found:
        write_data(data)
        print("user updated successfully")
    else:
        print('user not found')

def delete_user(user_id):
    data = read_data()
    for user in data:
        if user['id'] == user_id:
            data.remove(user)
            write_data(data)
            print('user deleted successfully')
            return
    print('user not found')

x = int(input('select operation: 1.Create 2.Read 3.Update 4.Delete'))
match x:
    case 1:
        new_user = json.loads(input('enter new user information'))
        create_user(new_user)
    case 2:
        print('all users:')
        read_user()
    case 3:
        update_user(2, {"name": "Bobby", "email": "bobby_new@example.com"})
    case 4:
        delete_user(1)