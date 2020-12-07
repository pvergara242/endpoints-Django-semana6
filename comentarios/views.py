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

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicaciones(self, request, pk=None) :
        Comentario = self.get_object()
        if request.method == 'GET' :
            serialized = PublicacionSerializer(Comentario.publicaciones, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        # if request.method == 'POST' :
        #     publicacion_id = request.data['publicaciones']
        #     for publicacion_id in publicaciones_ids :
        #         publicaciones = Publicacion.objects.get(id=int(publicacion_id))
        #         publicacion_id.publicaciones.add(publicaciones)
        #         return Response(status=status.HTTP_201_CREATED)
        # if request.method == 'DELETE' :
        #     publicaciones_id = request.data['publicaciones']
        #     for tag_id in publicaciones_id :
        #         tag = Tags.objects.get(id=int(tag_id))
        #         publicaciones.tags.remove(tag)
        #         return Response(status=status.HTTP_204_NO_CONTENT)