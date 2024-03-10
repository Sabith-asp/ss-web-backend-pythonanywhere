from rest_framework import serializers
from .models import ManagementCouncil, DirectorBoard, Chairman, Manager, MCQA, MCQAmember, Principal

class ManagementCouncilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagementCouncil
        fields = '__all__'

class DirectorBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectorBoard
        fields = '__all__'

class ChairmanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chairman
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class MCQASerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQA
        fields = '__all__'

class MCQAmemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = MCQAmember
        fields = '__all__'

class PrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Principal
        fields = '__all__'
