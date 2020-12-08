from tags.serializer import TagsSerializer
from tags.models import Tags
from rest_framework import generics, viewsets, status
from publicaciones.serializer import PublicacionSerializer
from rest_framework.response import Response
from rest_framework.decorators import action


# Create your views here.
class Tags(viewsets.ModelViewSet) :
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

    @action(methods=['GET', 'POST', 'DELETE'], detail=True)
    def publicaciones(self, request, pk=None) :
        tag = self.get_object()
        if request.method == 'GET' :
            id =Publicacion.objects.filter(tags=int(tag.id))
            serialized = PublicacionSerializer(id, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
        if request.method == 'POST' :
            publicacion = PublicacionSerializer(data=request.data)
            if publicacion.is_valid() :
                publicacion.save()
                return Response(status=status.HTTP_201_CREATED)
            else :
                return Response(status=status.HTTP_400_BAD_REQUEST, data=publicacion.errors)
        if request.method == 'DELETE' :
            publicaciones_id = request.data['id']
            for publicaciones_id in publicaciones_id :
                publicaciones = Publicacion.objects.get(id=int(publicaciones_id))
                publicaciones.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)