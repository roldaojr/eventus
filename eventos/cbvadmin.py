import cbvadmin
from comum.views import DetailView
from .models import Atividade, Inscricao, TipoInscricao


@cbvadmin.register(Atividade)
class AtividadeAdmin(cbvadmin.ModelAdmin):
    list_display = ('nome', 'tipo', 'local')
    menu_weight = 2


@cbvadmin.register(TipoInscricao)
class TipoInscricaoAdmin(cbvadmin.ModelAdmin):
    list_display = ('nome', 'preco')
    menu_weight = 4


@cbvadmin.register(Inscricao)
class InscricaoAdmin(cbvadmin.ModelAdmin):
    list_display = ('usuario', 'tipo', 'alojamento', 'deficiencia')
    filter_fields = ('tipo', 'alojamento', 'deficiencia')
    detail_view_class = DetailView
    default_object_action = 'detail'
    menu_weight = 3

    def get_actions(self):
        actions = super().get_actions()
        del actions['add']
        actions.update({'detail': 'object'})
        return actions
