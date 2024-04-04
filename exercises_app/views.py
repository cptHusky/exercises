from rest_framework.viewsets import ModelViewSet
from .models import Exercise
from .serializers import ExerciseSerializer


class ExerciseViewSet(ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()
        type = self.request.query_params.get('type')
        level = self.request.query_params.get('level')
        if type is not None:
            queryset = queryset.filter(type=type)
        if level is not None:
            queryset = queryset.filter(level=level)
        return queryset
