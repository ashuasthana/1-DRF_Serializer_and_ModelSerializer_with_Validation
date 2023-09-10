run This command in terminal:
#Get object and convert in Python Native data type(dict) by serializers

$ py manage.py shell
>>> from app_api.models import Employee
>>> from app_api.serializers import EmployeeSerializer
>>> emp=Employee.objects.get(id=2)
>>> emp.id
2
>>> emoserializer=EmployeeSerializer(emp)
>>> emoserializer.data
{'eno': 2, 'ename': 'Raj Kumar Bind', 'esal': 150000.0, 'eaddr': 'Gurugram'}

#Get data Native data type(dict) to JSON Form by JSONRenderer()

>>> from rest_framework.renderers import JSONRenderer
>>> json_data=JSONRenderer().render(emoserializer.data)
>>> json_data
b'{"eno":2,"ename":"Raj Kumar Bind","esal":150000.0,"eaddr":"Gurugram"}'
>>>

#How to convert query set to Python Native data type(dict) and convert in json_data by serializers

>>> qs=Employee.objects.all()
>>> qs
<QuerySet [<Employee: Employee object (1)>, <Employee: Employee object (2)>, <Employee: Employee object (3)>]>
>>> emoserializer=EmployeeSerializer(qs,many=True)  
>>> emoserializer.data
[OrderedDict([('eno', 1), ('ename', 'Ashish Asthana'), ('esal', 25000.0), ('eaddr', 'Delhi')]), OrderedDict([('eno', 2), ('ename', 'Raj Kumar Bind'), ('esal', 150000.0), ('eaddr', 'Gurugram')]), OrderedDict([('eno', 3), ('ename', 'Anil Verma'), ('esal', 150000.0), ('eaddr', 'Noida')])]
>>> json_data=JSONRenderer().render(emoserializer.data)
>>> json_data
b'[{"eno":1,"ename":"Ashish Asthana","esal":25000.0,"eaddr":"Delhi"},{"eno":2,"ename":"Raj Kumar Bind","esal":150000.0,"eaddr":"Gurugram"},{"eno":3,"ename":"Anil Verma","esal":150000.0,"eaddr":"Noida"}]'
>>>