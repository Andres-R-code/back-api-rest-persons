from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from persons.serializers import (
    PersonsSerializers,
)

class PersonsViewSet(viewsets.ModelViewSet):
    serializer_class = PersonsSerializers

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(code=pk, state=True).first()

    def list(self, request):
        person_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": person_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Persona creada correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        person = self.get_queryset(pk)
        if person:
            person_serializer = PersonsSerializers(person)
            return Response(person_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Persona con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            person_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if person_serializer.is_valid():
                person_serializer.save()
                return Response({'message':'Persona actualizada correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message':'', 'error':person_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        person = self.get_queryset().filter(code=pk).first() # get instance        
        if person:
            person.state = False
            person.save()
            return Response({'message':'Persona eliminada correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe una Persona con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)