from rest_framework import serializers

class SumSerializer(serializers.Serializer):
    choices=['+','-','*','%']
    num1 = serializers.IntegerField(max_value=None, min_value=None)
    num2 = serializers.IntegerField(max_value=None, min_value=None)
    option=serializers.ChoiceField(choices)

    Sum = serializers.IntegerField(max_value=None, min_value=None,required=False,read_only=True)
    diff=serializers.IntegerField(max_value=None, min_value=None,required=False,read_only=True)
    mul =serializers.IntegerField(max_value=None, min_value=None,required=False,read_only=True)
    div =serializers.FloatField(max_value=None, min_value=None,required=False,read_only=True)
    
    def create(self,validated_data):
    	return Sum(**validated_data)