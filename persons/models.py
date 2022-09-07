import uuid
from django.db import models


VISIVILITY_CHOICES_TIPE_IDENTIFICATION = [
    ('cédula', 'cédula'),
    ('cédula de extrangería', 'cédula de extrangería'),
    ('pasaporte', 'pasaporte'),
    ('targeta de identidad', 'targeta de identidad'),
] 


class Person(models.Model):

    code = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )

    tipe_identification = models.CharField(
        choices = VISIVILITY_CHOICES_TIPE_IDENTIFICATION,
        max_length = 42,
        blank = False, 
        null=False
        )

    identification_number = models.CharField(
        max_length = 10,
        unique = True,
        blank = False, 
        null=False
        )

    
    names = models.CharField(
        max_length = 100, 
        blank = False, 
        null = False
        )

    last_name = models.CharField(
        max_length = 100, 
        blank = False, 
        null=False
        )

    email = models.EmailField(
        unique = True,
        max_length = 100, 
        blank = False, 
        null = False
        )

    address = models.CharField(
        unique = True,
        max_length=300, 
        blank = False, 
        null = False
        )

    hobbie = models.CharField(
    max_length = 200, 
    blank = False, 
    null = False
    )

    state = models.BooleanField('Estado',default = True)

    created = models.DateField(auto_now_add = True, auto_now = False)
    modified = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

    def __str__(self):
        return f'code: {self.code} tipo de identificación: {self.tipe_identification} numero de identificación: {self.identification_number} names{self.names} apellidos: {self.last_name} email: {self.email} address: {self.address}  hobbie: {self.hobbie}'