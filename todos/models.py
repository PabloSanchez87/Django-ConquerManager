from django.db import models

## Los modelos es donde vamos a definir nuestras entidades de la app.

# Create your models here.
# https://docs.djangoproject.com/es/5.0/topics/db/models/


# Clase creada para explicar la RELACIÓN MANY-TO-ONE.

# Manager y modelos personalizados.
class PersonManager(models.Manager):
    def adults(self):
        return self.filter(age__gt=18)
    def childs(self):
        return self.filter(age__lt=18)


class Family(models.Model):
    name = models.CharField(
        max_length=140,
        unique=True
        )
    
    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Familia"
        verbose_name_plural = "Familias"

class Person(models.Model):
    # Creado para probar Many-to-one
    family = models.ForeignKey(   
        Family, on_delete=models.CASCADE,
        related_name="members"
    )
    
    """
    # Creado para Many-to-many
    family = models.ManyToManyField(   
        Family
    )  """  
    
    first_name = models.CharField(
        verbose_name="Nombre",
        max_length=30
        )
    last_name = models.CharField(
        "Apellidos",  # Si es el primer campo ya coge por defecto el valor para Verbose_name.
        max_length=30,
        )
    age = models.IntegerField(
        "Edad",
        default=18,
        help_text="Introduce tu edad en formato número."
        )
    dni = models.CharField(
        "DNI",
        max_length=9,
        unique=True
        )
    
    objects = PersonManager()
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    # Meta attribute. Esto interfiere en la bd, tenemos que migrarte.
    class Meta:
       ordering = ["age"] 
       verbose_name = "Persona"
       verbose_name_plural = "Personas"
       
    
    
    





""" 
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):                                          ## Referencia al model tipo Musician.
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)  ## Le indicamos que si se borra el Musician, se borran los artistas.
    name = models.CharField(max_length=100)                         
    release_date = models.DateField()
    num_stars = models.IntegerField()
"""