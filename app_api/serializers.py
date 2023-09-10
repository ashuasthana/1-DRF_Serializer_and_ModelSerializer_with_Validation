from rest_framework import serializers
from .models import Employee

 #Start==================Field Level Validation============================ 
def multiples_of_1000(value):
    print("Validation by using validator.")
    if value % 1000 != 0:
        raise serializers.ValidationError("Employee salary must be in multiples of 1000.")
    return value

#End==================Field Level Validation===============================


# Create your serializers here.
class EmployeeSerializer(serializers.Serializer):
    eno=serializers.IntegerField()
    ename=serializers.CharField(max_length=30)
    esal=serializers.FloatField(validators=[multiples_of_1000,])
    eaddr=serializers.CharField(max_length=64)

    #Start==================Field Level Validation============================ 
    def validate_esal(self,value):
        print("Validation at Field Level.")
        if value<5000:
            raise serializers.ValidationError("Employee salary must be grater then Rs. 5000.")
        return value

    #End==================Field Level Validation===============================
    #Start==================Object Level Validation============================ 
    def validate(self,data):
        print("Validation at Object Level.")
        ename=data.get('ename')
        esal=data.get('esal')
        if ename.lower()=='sunny':
            if esal<60000:
                raise serializers.ValidationError("Sunny salary must be grater then Rs. 60000.")
        return data

    #End==================Object Level Validation============================

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance