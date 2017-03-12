from django import forms

textarea_widget = forms.Textarea(attrs={'style': 'width: 100%; height: 100px'})

class HistoriaForm(forms.Form):
    parte = forms.CharField(label='Continua\u00e7\u00e3o...', max_length=1024, widget=textarea_widget)

class AvaliacaoForm(forms.Form):
    LEVEL = (
        ('1', 'P\u00e9ssimo'),
        ('2', 'Ruim'),
        ('3', 'Aceit\u00e1vel'),
        ('4', 'Bom'),
        ('5', '\u00d3timo'),
    )
    coerencia = forms.ChoiceField(label='Coer\u00eancia do enredo',choices=LEVEL,initial='4')
    diversao = forms.ChoiceField(label='N\u00edvel de divers\u00e3o',choices=LEVEL,initial='4')
    comentario = forms.CharField(label='Coment\u00e1rios, sugest\u00e3es ou cr\u00edticas', max_length=1024, widget=textarea_widget)

class IniciarHistoriaForm(forms.Form):
    estilos = (
        ('1', 'Contos Liter\u00e1rios'),
        ('2', 'Fatos Jornal\u00edsticos'),
    )
    estilo = forms.ChoiceField(label='Estilo', choices=estilos)