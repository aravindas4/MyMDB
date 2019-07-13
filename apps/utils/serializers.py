from rest_framework import serializers

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self.choices = choices
        self.to_repr = {v: k for k, v in self.choices._identifier_map.items()}
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self.to_repr[obj]

    def to_internal_value(self, data):
        if data in self.choices._identifier_map.keys():
            return self.choices._identifier_map[data]

        raise serializers.ValidationError(
            "Acceptable values are {0}.".format(
                list(self.choices._identifier_map.keys())))
