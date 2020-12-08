from rest_framework import serializers
from publicaciones.models import Publicacion
from tags.serializer import TagsSerializer
from tags.models import Tags

class PublicacionSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(Tags,many=True)
    class Meta:
        model=Publicacion
        fields='__all__'