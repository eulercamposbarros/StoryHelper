from django import forms

textarea_widget = forms.Textarea(attrs={'style': 'width: 100%; height: 100px'})

class HistoriaForm(forms.Form):
    parte = forms.CharField(label='Continuação...', max_length=1024, widget=textarea_widget)

class AvaliacaoForm(forms.Form):
    LEVEL = (
        ('1', 'Péssimo'),
        ('2', 'Ruim'),
        ('3', 'Aceitável'),
        ('4', 'Bom'),
        ('5', 'Ótimo'),
    )
    coerencia = forms.ChoiceField(label='Coerência do enredo',choices=LEVEL,initial='4')
    diversao = forms.ChoiceField(label='Nível de diversão',choices=LEVEL,initial='4')
    comentario = forms.CharField(label='Comentários, sugestões ou críticas', max_length=1024, widget=textarea_widget)

class IniciarHistoriaForm(forms.Form):
    estilos = (
        ('1', 'Contos Literários'),
        #('2', 'Fatos Jornal\u00edsticos'),
    )
    estilo = forms.ChoiceField(label='Estilo', choices=estilos)