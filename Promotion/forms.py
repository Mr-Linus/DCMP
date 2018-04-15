from django.forms import ModelForm
from  . models import Contact
from django.utils.translation import gettext_lazy as _
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = { 'name': 'Name','email':'E-mail','text':'Message', }
        help_texts = {
            'name':_('Please input your real name.'),
            'email':_('Please ensure the E-mail is available.')
        }
        error_messages= {
            'name':{
                'max_length': _("The name is too long"),
            },
        }
