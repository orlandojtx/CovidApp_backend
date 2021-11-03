from django.db import models

####################################################################################################
#                                                                                                  #
#                                            'pais' TABLE                                          #
####################################################################################################
class pais(models.Model):
    pais_id              = models.AutoField(primary_key=True)
    pais_nombre          = models.CharField(max_length=30)

####################################################################################################
#                                                                                                  #
#                                            'tipodoc' TABLE                                       #
####################################################################################################
class tipodoc(models.Model):
    docum_tipo_id           = models.AutoField(primary_key=True)
    docum_tipo              = models.CharField(max_length=25)


####################################################################################################
#                                                                                                  #
#                                            'vacuna' TABLE                                        #
####################################################################################################

class vacuna(models.Model):
    vacuna_id           = models.AutoField(primary_key=True)
    vacuna_nombre       = models.CharField(max_length=20)


####################################################################################################
#                                                                                                  #
#                                            'persona' TABLE                                       #
####################################################################################################

class persona(models.Model):
    psn_id                 = models.AutoField(primary_key=True)
    docum_tipo_id_fk       = models.ForeignKey(tipodoc, on_delete=models.CASCADE)
    psn_docum_numero       = models.IntegerField(default=0)
    psn_nombres            = models.CharField(max_length=50)
    psn_apellidos          = models.CharField(max_length=50)
    psn_fecha_nto          = models.DateField(auto_now_add=False, blank=False)
    psn_genero             = models.CharField(max_length=2)
    vacuna_aplicada_id_fk  = models.ForeignKey(vacuna, on_delete=models.CASCADE)


####################################################################################################
#                                                                                                  #
#                                            'solicitud' TABLE                                     #
####################################################################################################

class solicitud(models.Model):
    
    permiso_id          = models.AutoField(primary_key=True)
    permiso_fecha       = models.DateField(auto_now_add=False, blank=False)
    psn_cc_fk           = models.ForeignKey(persona, on_delete=models.CASCADE)
    pais_id_fk          = models.ForeignKey(pais, on_delete=models.CASCADE)
    resultado_prueba    = models.BooleanField(default=False)
    permiso_autorizado  = models.BooleanField(default=False)

####################################################################################################
#                                                                                                  #
#                                            'vacunaacep' TABLE                                    #
####################################################################################################

class vacunaacep(models.Model):
    vacuna_aceptada_id     = models.AutoField(primary_key=True)
    pais_id_fk             = models.ForeignKey(pais, on_delete=models.CASCADE)
    vacuna_id_fk           = models.ForeignKey(vacuna, on_delete=models.CASCADE)
