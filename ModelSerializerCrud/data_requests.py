import requests
import json

url = 'http://127.0.0.1:8000/student'

def create_new_record(data,url):
    json_data = json.dumps(data)
    r = requests.post(url=url+'/create', data=json_data)
    data = r.json()
    return data


def update_record(data,stud_id,url):
    json_data = json.dumps(data)
    r = requests.put(url=url+f"/update/{stud_id}", data=json_data)
    data = r.json()
    return data

def delete_record(stud_id,url):
    r = requests.get(url=url+f"/delete/{stud_id}")
    data = r.json()
    return data



print("Please Enter 1 for Create and 2 for update and 3 for delete")
input_type = int(input("Create or Update or Delete ? "))

if input_type not in [1,2,3]:
    print("please select right option,Try Again ")
else:
    if input_type == 1:
        name = input("Enter Name ")
        email = input("Enter Email ")
        created_response = create_new_record(data={'name':name, 'email':email},url=url)
        print(created_response)
    elif input_type == 2:
        print("Enter What you need to update else leave it blank")
        name = input("Enter Name ")
        email = input("Enter Email ")
        student_id = int(input("Enter Student ID "))
        data = {}
        if name and email:
            data = {'name': name, 'email': email}
        elif name:
            data = {'name': name}
        elif email:
            data = {'email': email}
        else:
            print("You have nothing to update")
        if data:
            update_response = update_record(data=data,stud_id = student_id,url=url)
            print(update_response)
    elif input_type == 3:
        print("Your Record going to delete ")
        student_id = int(input("Enter Student ID"))
        left_students = delete_record(student_id,url=url)
        print(left_students)
