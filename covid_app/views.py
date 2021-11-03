from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from covid_app.models import pais,vacuna,tipodoc,persona, solicitud, vacunaacep
from covid_app.serializers import paisSerializer,vacunaSerializer,tipodocSerializer,personaSerializer, solicitudSerializer, vacunaacepSerializer
#############
##   pais  ##
#############
@csrf_exempt
def paisApi(request,id=0):
    if request.method=='GET':
        Pais = pais.objects.all()
        pais_serializer=paisSerializer(Pais,many=True)
        return JsonResponse(pais_serializer.data,safe=False)
    elif request.method=='POST':
        pais_data=JSONParser().parse(request)
        pais_serializer=paisSerializer(data=pais_data)
        if pais_serializer.is_valid():
            pais_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        pais_data=JSONParser().parse(request)
        Pais=pais.objects.get(pais_id=pais_data['pais_id'])
        pais_serializer=paisSerializer(Pais,data=pais_data)
        if pais_serializer.is_valid():
            pais_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Pais=pais.objects.get(pais_id=id)
        Pais.delete()
        return JsonResponse("Deleted Successfully",safe=False)

##############
##  vacuna  ##
##############

@csrf_exempt
def vacunaApi(request,id=0):
    if request.method=='GET':
        Vacuna = vacuna.objects.all()
        vacuna_serializer=vacunaSerializer(Vacuna,many=True)
        return JsonResponse(vacuna_serializer.data,safe=False)
    elif request.method=='POST':
        vacuna_data=JSONParser().parse(request)
        vacuna_serializer=vacunaSerializer(data=vacuna_data)
        if vacuna_serializer.is_valid():
            vacuna_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        vacuna_data=JSONParser().parse(request)
        Vacuna=vacuna.objects.get(vacuna_id=vacuna_data['vacuna_id'])
        vacuna_serializer=vacunaSerializer(Vacuna,data=vacuna_data)
        if vacuna_serializer.is_valid():
            vacuna_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Vacuna=vacuna.objects.get(vacuna_id=id)
        Vacuna.delete()
        return JsonResponse("Deleted Successfully",safe=False)


##############
## tipo doc ##
##############

@csrf_exempt
def tipodocApi(request,id=0):
    if request.method=='GET':
        Tipodoc = tipodoc.objects.all()
        tipodoc_serializer=tipodocSerializer(Tipodoc,many=True)
        return JsonResponse(tipodoc_serializer.data,safe=False)
    elif request.method=='POST':
        tipodoc_data=JSONParser().parse(request)
        tipodoc_serializer=tipodocSerializer(data=tipodoc_data)
        if tipodoc_serializer.is_valid():
            tipodoc_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        tipodoc_data=JSONParser().parse(request)
        Tipodoc=tipodoc.objects.get(docum_tipo_id=tipodoc_data['docum_tipo_id'])
        tipodoc_serializer=tipodocSerializer(Tipodoc,data=tipodoc_data)
        if tipodoc_serializer.is_valid():
            tipodoc_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Tipodoc=tipodoc.objects.get(docum_tipo_id=id)
        Tipodoc.delete()
        return JsonResponse("Deleted Successfully",safe=False)


#############
## persona ##
#############

@csrf_exempt
def personaApi(request,id=0):
    if request.method=='GET':
        Persona = persona.objects.all()
        persona_serializer=personaSerializer(Persona,many=True)
        return JsonResponse(persona_serializer.data,safe=False)
    elif request.method=='POST':
        persona_data=JSONParser().parse(request)
        persona_serializer=personaSerializer(data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        persona_data=JSONParser().parse(request)
        Persona=persona.objects.get(psn_id=persona_data['psn_id'])
        persona_serializer=personaSerializer(Persona,data=persona_data)
        if persona_serializer.is_valid():
            persona_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Persona=persona.objects.get(psn_id=id)
        Persona.delete()
        return JsonResponse("Deleted Successfully",safe=False)


###############
## solicitud ##
###############

@csrf_exempt
def solicitudApi(request,id=0):
    if request.method=='GET':
        Solicitud = solicitud.objects.all()
        solicitud_serializer=solicitudSerializer(Solicitud,many=True)
        return JsonResponse(solicitud_serializer.data,safe=False)
    elif request.method=='POST':
        solicitud_data=JSONParser().parse(request)
        solicitud_serializer=solicitudSerializer(data=solicitud_data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        solicitud_data=JSONParser().parse(request)
        Solicitud=solicitud.objects.get(solicitud_id=solicitud_data['solicitud_id'])
        solicitud_serializer=solicitudSerializer(Solicitud,data=solicitud_data)
        if solicitud_serializer.is_valid():
            solicitud_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Solicitud=solicitud.objects.get(solicitud_id=id)
        Solicitud.delete()
        return JsonResponse("Deleted Successfully",safe=False)


#################
## vacunaacep  ##
#################

@csrf_exempt
def vacunaacepApi(request,id=0):
    if request.method=='GET':
        Vacunaacep = vacunaacep.objects.all()
        vacunaacep_serializer=vacunaacepSerializer(Vacunaacep,many=True)
        return JsonResponse(vacunaacep_serializer.data,safe=False)
    elif request.method=='POST':
        vacunaacep_data=JSONParser().parse(request)
        vacunaacep_serializer=vacunaacepSerializer(data=vacunaacep_data)
        if vacunaacep_serializer.is_valid():
            vacunaacep_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        vacunaacep_data=JSONParser().parse(request)
        Vacunaacep=vacunaacep.objects.get(vacunaacep_id=vacunaacep_data['vacunaacep_id'])
        vacunaacep_serializer=vacunaacepSerializer(Vacunaacep,data=vacunaacep_data)
        if vacunaacep_serializer.is_valid():
            vacunaacep_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Vacunaacep=vacunaacep.objects.get(vacunaacep_id=id)
        Vacunaacep.delete()
        return JsonResponse("Deleted Successfully",safe=False)

