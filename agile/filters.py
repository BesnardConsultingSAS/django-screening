from django_filters import rest_framework as filters
from agile.models import Agile


class AgileFilter(filters.FilterSet):
    class Meta:
        model = Agile
        fields = {"name": ["icontains"], "type": ["exact"]}
