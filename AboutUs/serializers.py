from rest_framework import serializers
from .models import *

class MissionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionVision
        fields = '__all__'

class HistoryofCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryofCollege
        fields = '__all__'

class AboutCollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCollege
        fields = '__all__'

class SisterInstituitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SisterInstituition
        fields = '__all__'

class FormerPrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormerPrincipal
        fields = '__all__'

class AccreditationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accreditation
        fields = '__all__'

class RecognitionandAwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecognitionandAward
        fields = '__all__'

class StrategicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicPlan
        fields = '__all__'

class RTISerializer(serializers.ModelSerializer):
    class Meta:
        model = RTI
        fields = '__all__'
