from rest_framework  import serializers
from .models import Student



def starts_with(value):
    '''this is a validator function which will check if the value starts with letter a'''
    if value[0] != 'a':
        raise serializers.ValidationError('Name Does not statrs with A')
    return value
    

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100,validators=[starts_with])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length = 100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instace,validated_data):
        instace.name = validated_data.get('name',instace.name)
        print(instace.name)
        instace.roll = validated_data.get('roll',instace.roll)
        instace.city = validated_data.get('city',instace.city)
        instace.save()
        return instace

    def validate_roll(self,value):
        '''this function is user to validate a single field that is roll field '''
        if value > 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    def validate(self,data):
        '''this function will validate multiple fields first the above validation will be done i.e., the above function will get executed and then this function'''
        nm= data.get('name')
        ct = data.get('city')
        if nm.lower() == 'ayra' and ct != 'delhi':
            raise serializers.ValidationError('Invalid')
        return data