import requests
import json

BASE_URL="http://127.0.0.1:8000/"
END_POINT="api/"

# Start:For get all records and specific record via id========================
def get_resource(id=None):
    data={}
    #if id is not None so get only specific record get via id.  
    if id is not None:
        data={'id':id}
    resp=requests.get(BASE_URL + END_POINT,data=json.dumps(data))
    data=resp.json()
    print(resp.status_code)
    print(data)  
# End:For get all records and specific record via id========================
    

# Start:For create records========================
def create_resource():
    new_emp={'ename':'sunny','eno':5,'eaddr':'Canada','esal':3500,}
    resp=requests.post(BASE_URL + END_POINT,data=json.dumps(new_emp))
    print(type(new_emp))
    print(resp.status_code)
    print(resp.text)
    # print(resp.json)
# End:For create records========================    

# Start:For update particular records via id========================
def update_resource(id):
    new_emp={'id':id,'ename':'Ashish Asthana','eaddr':'Hyderabad','esal':125000,}
    resp=requests.put(BASE_URL + END_POINT,data=json.dumps(new_emp))
    print(resp.status_code)
    # print(resp.json)
    print(resp.text)   
# End:For update particular records via id========================

# Start:For delete particular records via id========================
def del_resource (id):
    new_emp={'id':id}
    resp=requests.delete(BASE_URL + END_POINT,data=json.dumps(new_emp))
    print(resp.status_code)
    # print(resp.json)
    print(resp.text)       
# End:For delete particular records via id========================


#******Action via calling functionn  *********
# get_resource(1)#For get paticular records via id
# get_resource(300)
# get_resource()#For get all records 
create_resource()
# update_resource(1)
# del_resource('4')

