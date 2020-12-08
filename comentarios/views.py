from django.shortcuts import render
from rest_framework import viewsets
from comentarios.serializer import ComentarioSerializer
from publicaciones.serializer import PublicacionSerializer
from comentarios.models import Comentario
from rest_framework.decorators import action
from rest_framework import generics, viewsets, status
from rest_framework.response import Response



# Create your views here.
class Comentario(viewsets.ModelViewSet) :
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(methods=['GET'], detail=True)
    def publicaciones(self, request, pk=None) :
        comentario = self.get_object()
        serialized = PublicacionSerializer(comentario.publicaciones)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST' :
            publicacion = request.data['comentarios']
            for publicacion_id in publicaciones_ids :
                publicaciones = publicacion.objects.get(id=int(publicacion_id))
                publicacion_id.comentarios.add(publicaciones)
                return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' :
            publicaciones_id = request.data['comentarios']
            for comentario_id in publicaciones_id :
                comentario =Comentario.objects.get(id=int(comentario_id))
                publicaciones.comentario.remove(comentario)
                return Response(status=status.HTTP_204_NO_CONTENT)