from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import *
from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import *
from .pagination import CustomPagination

class get_delete_update_paciente(RetrieveUpdateDestroyAPIView):
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            paciente = Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return paciente

    # Get a Paciente
    def get(self, request, pk):

        paciente = self.get_queryset(pk)
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a Paciente
    def put(self, request, pk):
        
        paciente = self.get_queryset(pk)

        if(request.user == paciente.creator): # If creator is who makes request
            serializer = PacienteSerializer(paciente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a Paciente
    def delete(self, request, pk):

        paciente = self.get_queryset(pk)

        if(request.user == paciente.creator): # If creator is who makes request
            paciente.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_pacientes(ListCreateAPIView):
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       pacientes = Paciente.objects.all()
       return pacientes

    # Get all Pacientes
    def get(self, request):
        pacientes = self.get_queryset()
        paginate_queryset = self.paginate_queryset(pacientes)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new Paciente
    def post(self, request):
        serializer = PacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

