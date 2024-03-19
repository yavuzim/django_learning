'''Django REST Framework içinde, Python nesnelerini ve Django modellerini 
JSON veya diğer veri formatlarına dönüştürmek için kullanılan yapılardır'''

from rest_framework import serializers
from haberler.models import Makale

class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayimlama_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncelleme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayimlama_tarihi = validated_data.get('yayimlama_tarihi', instance.yayimlama_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance