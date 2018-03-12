from rest_framework import serializers
from .models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    created_date = serializers.SerializerMethodField()

    class Meta:
        model = Publication
        fields = ('name', 'description',
                  'image',
                  'featured',
                  'created',
                  'created_date')

    def get_created_date(self, obj):

        return obj.created.strftime('%Y/%m/%d a las %H:%M:%S')
