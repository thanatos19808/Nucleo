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

    # Get a paciente
    def get(self, request, pk, *args, **kwargs):
        try:
            paciente = Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        paciente = self.get_queryset(pk)
        if(request.user in paciente.editors.all()): # If editors is who makes request
            serializer = PacienteSerializer(paciente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {
                    'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


    # Update a paciente
    def put(self, request, pk, *args, **kwargs):
        try:
            paciente = Paciente.objects.get(pk=pk)
        except Paciente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        paciente = self.get_queryset(pk)
        if(len(paciente.editors.all())==0):
            paciente.editors.add(request.user)
        if(request.user in paciente.editors.all()): # If editors is who makes request
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

    # Delete a paciente
    def delete(self, request, pk, *args, **kwargs):
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

    # Get all pacientes
    def get(self, request, *args, **kwargs):
        content = {
                'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Create a new paciente
    def post(self, request):
        content = {
                'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)


class get_delete_update_expediente(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpedienteSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            expediente = Expediente.objects.get(pk=pk)
        except Expediente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return expediente

    # Get a expediente
    def get(self, request, pk, *args, **kwargs):
        try:
            expediente = Expediente.objects.get(pk=pk)
        except Expediente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        expediente = self.get_queryset(pk)
        if (expediente.Paciente.id==request.user.profile.id_sem):  # If editors is who makes request
            serializer = ExpedienteSerializer(expediente)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Update a expediente
    def put(self, request, pk, *args, **kwargs):
        try:
            expediente = Expediente.objects.get(pk=pk)
        except Expediente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        expediente = self.get_queryset(pk)
        if (expediente.Paciente.id==request.user.profile.id_sem):  # If editors is who makes request
            serializer = ExpedienteSerializer(expediente, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a expediente
    def delete(self, request, pk, *args, **kwargs):
        try:
            expediente = Expediente.objects.get(pk=pk)
        except Expediente.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        expediente = self.get_queryset(pk)
        if (expediente.Paciente.id==request.user.profile.id_sem):  # If editors is who makes request
            expediente.delete()
            content = {
                'status': 'NO CONTENT'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

class get_post_expedientes(ListCreateAPIView):
    serializer_class = ExpedienteSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       expedientes = Expediente.objects.all()
       return expedientes

    # Get all expedientes
    def get(self, request, *args, **kwargs):
        expedientes = self.get_queryset()
        expedientes = expedientes.filter(Paciente = request.user.profile.id_sem)
        paginate_queryset = self.paginate_queryset(expedientes)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new expediente
    def post(self, request):
            paciente = Paciente.objects.get(id=request.user.profile.id_sem)
            serializer = ExpedienteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(Paciente=paciente)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class get_delete_update_sucursal(RetrieveUpdateDestroyAPIView):
    serializer_class = SucursalSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            sucursal = Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return sucursal

    # Get a sucursal
    def get(self, request, pk, *args, **kwargs):
        try:
            sucursal = Sucursal.objects.get(pk=pk)
        except Sucursal.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        sucursal = self.get_queryset(pk)
        serializer = SucursalSerializer(sucursal)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # Update a sucursal
    def put(self, request, pk, *args, **kwargs):
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a sucursal
    def delete(self, request, pk, *args, **kwargs):
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class get_post_sucursals(ListCreateAPIView):
    serializer_class = SucursalSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       sucursals = Sucursal.objects.all()
       return sucursals

    # Get all sucursals
    def get(self, request, *args, **kwargs):
        sucursal = self.get_queryset()
        paginate_queryset = self.paginate_queryset(sucursal)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new sucursal
    def post(self, request):
        content = {
                'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)


class get_delete_update_disponibilidadServicio(RetrieveUpdateDestroyAPIView):
    serializer_class = DisponibilidadServicioSerializer
    
    def get_queryset(self, pk):
        try:
            disponibilidadServicio = DisponibilidadServicio.objects.get(pk=pk)
        except DisponibilidadServicio.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return disponibilidadServicio

    # Get a disponibilidadServicio
    def get(self, request, pk, *args, **kwargs):
        try:
            disponibilidadServicio = DisponibilidadServicio.objects.get(pk=pk)
        except DisponibilidadServicio.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        disponibilidadServicio = self.get_queryset(pk)        
        serializer = DisponibilidadServicioSerializer(disponibilidadServicio)
        return Response(serializer.data, status=status.HTTP_200_OK)

		
    # Update a disponibilidadServicio
    def put(self, request, pk, *args, **kwargs):
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)


    # Delete a disponibilidadServicio
    def delete(self, request, pk, *args, **kwargs):
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)

class get_post_disponibilidadServicios(ListCreateAPIView):
    serializer_class = DisponibilidadServicioSerializer
    pagination_class = CustomPagination
    
    def get_queryset(self):
       disponibilidadServicios = DisponibilidadServicio.objects.all()
       return disponibilidadServicios

    # Get all disponibilidadServicios
    def get(self, request, *args, **kwargs):
        disponibilidadServicios = self.get_queryset()
        paginate_queryset = self.paginate_queryset(disponibilidadServicios)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new disponibilidadServicio
    def post(self, request):
        content = {
            'status': 'UNAUTHORIZED'
        }
        return Response(content, status=status.HTTP_401_UNAUTHORIZED)
