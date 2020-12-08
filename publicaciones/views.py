from publicaciones.serializer import PublicacionSerializer
from comentarios.serializer import ComentarioSerializer
from tags.serializer import TagsSerializer
from tags.models import Tags
from publicaciones.models import Publicacion
from comentarios.models import Comentario
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class Publicacion(viewsets.ModelViewSet) :
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def tags(self, request, pk=None) :
        Publicacion = self.get_object()
        if request.method == 'GET' :
            serialized = TagsSerializer(Publicacion.tags, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST' :
            tags = request.data['tags']
            for tag_id in tags:
                tags = Tags.objects.get(id=int(tag_id))
                Publicacion.tags.add(tags)
            return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' :
            publicaciones_id = request.data['publicaciones']
            for tag_id in publicaciones_id :
                tag = Tags.objects.get(id=int(tag_id))
                Publicacion.tags.remove(tag)
                return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def comentarios(self, request, pk=None) :
            publicacion = self.get_object()
            if request.method == 'GET' :
                serialized = ComentarioSerializer(publicacion.comentarios, many=True)
                return Response(status=status.HTTP_200_OK, data=serialized.data)
            if request.method == 'POST' :
                publicaciones_id = request.data['comentarios']
                for comentarios_id in publicaciones_id :
                    comentarios = Comentario.objects.get(id=int(comentarios_id))
                    publicacion.comentarios.add(comentarios)
                return Response(status=status.HTTP_201_CREATED)
            if request.method == 'DELETE' :
                comentario_id = request.data['comentarios']
                for comentario_id in comentario_id :
                    comentario = Comentario.objects.get(id=int(comentario_id))
                    publicacion.comentarios.remove(comentario)
                    return Response(status=status.HTTP_204_NO_CONTENT)