from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset
from django import forms

from .models import order
from crispy_forms.helper import FormHelper



CITY_CHOICES = (
    ('الرياض', 'الرياض'),
    ('الجبيل', 'الجبيل'),
    ('الطائف', 'الطائف'),
    ('حايل', 'حايل'),
    ('جده', 'جده'),
    ('الدمام', 'الدمام'),
    ('المدينة المنورة', 'المدينة المنورة'),
    ('حفر الباطن', 'حفر الباطن'),
    ('تبوك', 'تبوك'),
    ('جيزان', 'جيزان'),
    ('الخرج', 'الخرج'),
    ('نجران', 'نجران'),
    ('ابها', 'ابها'),
    ('مكه', 'مكه'),
    ('الاحساء', 'الاحساء'),
    ('القصيم', 'القصيم'),
    ('بيشه', 'بيشه')
)

COUNTRY_CHOICES = (
    ('السعودية', 'السعودية')
)


class OrderCreateForm(forms.ModelForm):
    country = forms.ChoiceField(choices=order.COUNTRY_CHOICES, label='الدولة'),
    city = forms.ChoiceField(choices=order.CITY_CHOICES, label='المدينة')
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['country'].required = True
        self.fields['country'].choices = [('', '........اختر الدولة .....')] + order.COUNTRY_CHOICES
        self.fields['city'].choices = [('', '........اختر المدينة .....')] + order.CITY_CHOICES
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address',
            Row(
                Column('phone', css_class='form-group col-md-4 mb-0'),
                Column('country', css_class='form-group col-md-4 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Submit order', css_class='btn morpheus-den-gradient')
        )
    class Meta:
        model = order
        fields = ['first_name', 'last_name', 'address', 'phone', 'country', 'city']
        # widgets = {
        # 'first_name' : forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'الاسم الاول '})),
        # 'last_name' : forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'الاسم الاخير '})),
        #  'address':  forms.CharField(max_length=128,widget=forms.TextInput(attrs={'placeholder': 'العنوان / اسم الشارع'})),
        #  'country':  forms.CharField(choices=COUNTRY_CHOICES),
        #  'city':  forms.CharField(choices=CITY_CHOICES),
        #  'phone': forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'رقم التلفون'})),
        # }
        # labels = {
        #     'first_name': '',
        #     'last_name': '',
        #     'address': '',
        #     'country': '',
        #     'city': '',
        #     'phone': '',
        # }


# class OrderCreateForm(forms.Form):
#     first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
#     last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
#     address = forms.CharField(
#         label='Address',
#         widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
#     )
#     country = forms.ChoiceField(choices=COUNTRY_CHOICES)
#     city = forms.ChoiceField(choices=CITY_CHOICES)
#     phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+0123456789'}))
#
