from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MissionVision, HistoryofCollege, AboutCollege, SisterInstituition, FormerPrincipal, Accreditation, RecognitionandAward, StrategicPlan, RTI
from .serializers import MissionVisionSerializer, HistoryofCollegeSerializer, AboutCollegeSerializer, SisterInstituitionSerializer, FormerPrincipalSerializer, AccreditationSerializer, RecognitionandAwardSerializer, StrategicPlanSerializer, RTISerializer

class MissionVisionList(APIView):
    def get(self, request):
        missions = MissionVision.objects.all()
        serializer = MissionVisionSerializer(missions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MissionVisionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HistoryofCollegeList(APIView):
    def get(self, request):
        history = HistoryofCollege.objects.all()
        serializer = HistoryofCollegeSerializer(history, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HistoryofCollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AboutCollegeList(APIView):
    def get(self, request):
        about = AboutCollege.objects.all()
        serializer = AboutCollegeSerializer(about, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AboutCollegeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SisterInstituitionList(APIView):
    def get(self, request):
        sister_institutions = SisterInstituition.objects.all()
        serializer = SisterInstituitionSerializer(sister_institutions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SisterInstituitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormerPrincipalList(APIView):
    def get(self, request):
        principals = FormerPrincipal.objects.all()
        serializer = FormerPrincipalSerializer(principals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FormerPrincipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AccreditationList(APIView):
    def get(self, request):
        accreditations = Accreditation.objects.all()
        serializer = AccreditationSerializer(accreditations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccreditationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RecognitionandAwardList(APIView):
    def get(self, request):
        awards = RecognitionandAward.objects.all()
        serializer = RecognitionandAwardSerializer(awards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecognitionandAwardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StrategicPlanList(APIView):
    def get(self, request):
        plans = StrategicPlan.objects.all()
        serializer = StrategicPlanSerializer(plans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StrategicPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RTIList(APIView):
    def get(self, request):
        rtis = RTI.objects.all()
        serializer = RTISerializer(rtis, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RTISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
