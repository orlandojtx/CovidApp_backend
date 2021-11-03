from rest_framework import serializers
from covid_app.models import pais,vacuna,tipodoc,persona, solicitud, vacunaacep

class paisSerializer(serializers.ModelSerializer):
    class Meta:
        model=pais
        fields=('pais_id', 'pais_nombre')

class tipodocSerializer(serializers.ModelSerializer):
    class Meta:
        model=tipodoc
        fields=('docum_tipo_id', 'docum_tipo')

class vacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model=vacuna
        fields=('vacuna_id', 'vacuna_nombre')

class personaSerializer(serializers.ModelSerializer):
    class Meta:
        model=persona
        fields=('psn_id', 'docum_tipo_id_fk', 'psn_docum_numero', 'psn_nombres', 
                'psn_apellidos', 'psn_fecha_nto', 'psn_genero', 'vacuna_aplicada_id_fk')

class solicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model=solicitud
        fields=('permiso_id', 'permiso_fecha', 'psn_cc_fk', 'pais_id_fk', 
                'resultado_prueba', 'permiso_autorizado')

class vacunaacepSerializer(serializers.ModelSerializer):
    class Meta:
        model=vacunaacep
        fields=('vacuna_aceptada_id', 'pais_id_fk', 'vacuna_id_fk')
