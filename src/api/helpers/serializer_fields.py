from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class SerializeField(serializers.Field):
    """
    This field with serialize and deserialize foreign keys.
    Had to override this since there was no viable solution to receive foreign
     key id and respond with its object
    """

    def __init__(self, **kwargs):
        """we have to get the model and object used for serialisation in
        which error will be raised of key error
        :param kwargs contains the model and serializer
        used for deserialization and serialization
        """
        self.model = kwargs.pop("model")
        self.serializer = kwargs.pop("serializer")
        super(SerializeField, self).__init__(**kwargs)

    def to_representation(self, value):
        """
        Convert primitive python data types to json field
        :param values: python model objects
        :return: json data
        """
        # On respond we deserialize the value
        data = self.serializer(value, context=self.context)
        return data.data

    def to_internal_value(self, data):
        """
        convert json field to python datatype
        :param data: data from user
        :return: Object from the model
        """
        if not self.allow_null and not data:
            raise ValidationError("This field may not be null.")
        try:
            int(data)
        except ValueError:
            raise ValidationError("Kindly provide a integer")
        try:
            model_object = self.model.objects.get(pk=data)
        except self.model.DoesNotExist:
            raise ValidationError(f'Pk \"{data}\" for {self.label} object does not exist.')
        except ValueError:
            raise ValidationError("Kindly provide and integer")
        return model_object


class SerializeManyToManyField(serializers.Field):
    """
    This field with serialize and deserialize Many to Many keys.
    Had to override this since there was no viable solution to receive foreign
     key id and respond with its object
    """

    def __init__(self, **kwargs):
        """Used to get custom keywords and pass the rest to the parent
        :param: model: The model that will be used to serialize and deserialize
                serializer: Serializer to be used for serialize and deserialize
                **kwargs: passed to parent
        """
        self.model = kwargs.pop("model")
        self.serializer = kwargs.pop("serializer")
        super(SerializeManyToManyField, self).__init__(**kwargs)

    def to_representation(self, values):
        """
        Convert primitive python data types to json field
        :param values: python model objects
        :return: json data
        """
        # On respond we deserialize the value
        data = self.serializer(values, context=self.context, many=True)
        return data.data

    def to_internal_value(self, data):
        """
        convert json field to python datatype
        :param data: data from user
        :return: Object from the model
        """
        if not isinstance(data, list):
            raise ValidationError("Kindly provide a list of Primary Keys")
        if not self.allow_null and not data:
            raise ValidationError("This field may not be null.")
        user_objects = []
        for user in data:
            try:
                model_object = self.model.objects.get(pk=user)
                user_objects.append(model_object)
            except self.model.DoesNotExist:
                raise ValidationError(f'Pk \"{user}\" for {self.label} object does not exist.')
            except ValueError:
                raise ValidationError("Kindly provide and integer")
        return user_objects
