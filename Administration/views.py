from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ManagementCouncil, DirectorBoard, Chairman, Manager, MCQA, MCQAmember, Principal
from .serializers import ManagementCouncilSerializer, DirectorBoardSerializer, ChairmanSerializer, ManagerSerializer, MCQASerializer, MCQAmemberSerializer, PrincipalSerializer

class ManagementCouncilList(APIView):
    def get(self, request):
        management_council = ManagementCouncil.objects.all()
        serializer = ManagementCouncilSerializer(management_council, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagementCouncilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DirectorBoardList(APIView):
    def get(self, request):
        director_board = DirectorBoard.objects.all()
        serializer = DirectorBoardSerializer(director_board, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DirectorBoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChairmanList(APIView):
    def get(self, request):
        chairmen = Chairman.objects.all()
        serializer = ChairmanSerializer(chairmen, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChairmanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManagerList(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MCQAList(APIView):
    def get(self, request):
        mcqa = MCQA.objects.all()
        serializer = MCQASerializer(mcqa, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MCQASerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MCQAmemberList(APIView):
    def get(self, request):
        mcqa_members = MCQAmember.objects.all()
        serializer = MCQAmemberSerializer(mcqa_members, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MCQAmemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PrincipalList(APIView):
    def get(self, request):
        principals = Principal.objects.all()
        serializer = PrincipalSerializer(principals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PrincipalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
