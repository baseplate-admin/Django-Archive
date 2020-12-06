from django import forms


class ModelBitrate(forms.Form):
    hour = forms.IntegerField(label="Hour:")
    minute = forms.IntegerField(label="Minute:")
    second = forms.IntegerField(label="Second:")
    size = forms.DecimalField(label="Preferred Size in GB(Upto 2 decimal value allowed)", decimal_places=2)
    episode = forms.IntegerField(label="No of Episodes:")
