from django.conf.urls import url
from covid_app import views

urlpatterns=[

                #pais
                url(r'^pais$',views.paisApi),
                url(r'^pais/([0-9]+)$',views.paisApi),
                #vacuna
                url(r'^vacuna$',views.vacunaApi),
                url(r'^vacuna/([0-9]+)$',views.vacunaApi),
                #tipodoc
                url(r'^tipodoc$',views.tipodocApi),
                url(r'^tipodoc/([0-9]+)$',views.tipodocApi),
                #persona
                url(r'^persona$',views.personaApi),
                url(r'^persona/([0-9]+)$',views.personaApi),
                #solicitud
                url(r'^solicitud$',views.solicitudApi),
                url(r'^solicitud/([0-9]+)$',views.solicitudApi),
                #vacunaacep
                url(r'^vacunaacep$',views.vacunaacepApi),
                url(r'^vacunaacep/([0-9]+)$',views.vacunaacepApi)
            ]