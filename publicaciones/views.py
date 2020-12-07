from publicaciones.serializer import PublicacionSerializer
from tags.serializer import TagsSerializer
from tags.models import Tags
from publicaciones.models import Publicacion
from comentarios.serializer import ComentarioSerializer
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
            publicacion_id = request.data['publicaciones']
            for tag_id in publicacion_id :
                tags = Publicacion.objects.get(id=int(tag_id))
                publicacion_id.publicaciones.add(tags)
                return Response(status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' :
            publicaciones_id = request.data['publicaciones']
            for tag_id in publicaciones_id :
                tag = Tags.objects.get(id=int(tag_id))
                publicaciones.tags.remove(tag)
                return Response(status=status.HTTP_204_NO_CONTENT)

