import json
from django.core.serializers.json import Serializer

from backend.models_dir.Game import Game


class GameSerializer(Serializer):
    def get_dump_object(self, model: Game):
        dump = {}

        for field in model._meta.fields:
            if field.name == 'area':
                dump[field.name] = json.loads(field.value_to_string(model))
            else:
                dump[field.name] = field.value_to_string(model)
        return dump
