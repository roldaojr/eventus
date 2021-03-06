from django_filters import FilterSet, CharFilter
from .models import Inscricao


class InscricaoFilter(FilterSet):
    class Meta:
        model = Inscricao
        fields = ('nome', 'tipo', 'alojamento', 'deficiencia')

    nome = CharFilter(
        field_name='usuario',
        lookup_expr='nome_completo__icontains',
        label='Nome completo'
    )
