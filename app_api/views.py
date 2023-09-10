from django.shortcuts import render
from django.views.generic import View
from .utils import is_json,get_obj_by_id
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Employee
from app_api.serializers import EmployeeSerializer
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCURDCBV(View):
    def get(self,request,*args,**kwargs):
        print("heollo")
        json_data=request.body
        print(json_data)
        try:
            stream=io.BytesIO(json_data)
            py_data=JSONParser().parse(stream)
        except Exception as e:
            # print(e)
            json_data=JSONRenderer().render({'msg':'Pleaes send only JSON Data.'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        else:
            id=py_data.get('id',None)
            #send response with all records.
            if id is None:
                qs=Employee.objects.all()
                eserializer=EmployeeSerializer(qs,many=True)
                json_data=JSONRenderer().render(eserializer.data)
                return HttpResponse(json_data,content_type='application/json')
            #send response with particular record 
            emp_obj=get_obj_by_id(id)# emp_obj=Employee.objects.get(id=id)
            print(id)
            print(emp_obj)
            if emp_obj is None:
                print(type(json_data))
                json_data=JSONRenderer().render({'msg':'Given Id is not available.'}) 
                return HttpResponse(json_data, content_type='application/json', status=404)
            eserializer=EmployeeSerializer(emp_obj)
            json_data=JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json')
        
    def post(self,request,*args,**kwargs):
        json_data=request.body
        try:
            stream=io.BytesIO(json_data)
            p_data=JSONParser().parse(stream)
        except Exception as e:
            # If there's an exception (e.g., if the data isn't valid JSON),
            # handle it here
            print("An error occurred:", e)
            json_data = JSONRenderer().render({'msg': 'Please send only JSON Data.'})
            return HttpResponse(json_data,content_type='application/json',status=400)
        else:
            serializer=EmployeeSerializer(data=p_data)
            if serializer.is_valid():
                serializer.save()
                json_data = JSONRenderer().render({'msg': 'Record Added Successfully.'})
                return HttpResponse(json_data,content_type='application/json')
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json',status=400)
        
    def put(self,request,*args,**kwargs):
        json_data=request.body  
        stream=io.BytesIO(json_data) 
        pdata=JSONParser().parse(stream) 
        id=pdata.get('id')
        print(id)
        obj=get_obj_by_id(id)
        if obj is None:
            json_data = JSONRenderer().render({'msg': 'Id is not Available.'})
            return HttpResponse(json_data,content_type='application/json',status=404)
        serializer=EmployeeSerializer(obj,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render({'msg': 'Record Updated Successfully.'})
            return HttpResponse(json_data,content_type='application/json')
        # Return a JSON response with validation errors and a 400 status code
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json',status=400)
    
    def delete(self,request,*args,**kwargs):
        json_data=request.body  
        stream=io.BytesIO(json_data) 
        pdata=JSONParser().parse(stream) 
        id=pdata.get('id')
        print(id)
        obj=get_obj_by_id(id)
        if obj is not None:
            status,detail=obj.delete()
            if status==1:
                json_data = JSONRenderer().render({'msg': 'Record Deleted Successfully.'})
                return HttpResponse(json_data,content_type='application/json')
            json_data = JSONRenderer().render({'msg': 'Record Not Deleted try again.'})
            return HttpResponse(json_data,content_type='application/json',status=500)
        json_data = JSONRenderer().render({'msg': 'Id is not Available.'})
        return HttpResponse(json_data,content_type='application/json',status=404)
        
                
            
 

