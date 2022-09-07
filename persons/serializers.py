from persons.models import Person
from rest_framework.serializers import ModelSerializer

class PersonsSerializers(ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'code', 
            'tipe_identification',
            'identification_number',
            'names',
            'last_name',
            'email',
            'address',
            'hobbie',
            'state',
        )

