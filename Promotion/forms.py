from django.forms import ModelForm
from  Promotion. models import Contact
from django.utils.translation import gettext_lazy as _
#  Form不再使用静态HTML写法,使用Django-bootstrap3取而代之
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
