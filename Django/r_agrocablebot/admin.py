from django.contrib import admin
from django import forms
from .models import *
# Register your models here.

admin.site.register(acciones)
admin.site.register(tipoSensor)
admin.site.register(sensor)
admin.site.register(tipoCultivo)

class sensoresxCultivo(admin.ModelAdmin):
    filter_horizontal=['sensores',]   

admin.site.register(cultivo,sensoresxCultivo) 

class CalendarioAdmin(admin.ModelAdmin):
    def get_cultivo(self, obj):
        return ", ".join([cultivo.nombre for cultivo in obj.cultivo.all()])
    get_cultivo.short_description = 'cultivo'

    def get_planta(self, obj):
        return ", ".join([plantas.nombre for plantas in obj.plantas.all()])
    get_planta.short_description = 'plantas'
    
    list_display = ['acciones', 'get_cultivo', 'get_planta', 'fecha_inicio', 'repeticion']
    list_filter = ['repeticion']
    filter_horizontal = ['cultivo','plantas']
    search_fields = ['acciones__nombre']
admin.site.register(calendarios, CalendarioAdmin)

class plantasAdmin(admin.ModelAdmin):
    list_display = ['numeroPlanta', 'coordenadaX', 'coordenadaY', 'cultivo']
    ordering=('numeroPlanta',)

admin.site.register(plantas,plantasAdmin)  
admin.site.register(imagenesxPlanta)  

admin.site.register(Sensor_MQTT)
class eventosCalendariosAdmin(admin.ModelAdmin):
    list_display=['title','start']
    list_filter=['start']
admin.site.register(eventosCalendarios,eventosCalendariosAdmin)

admin.site.register(RutinaCodigoG)  


