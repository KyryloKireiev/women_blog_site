from django import forms
from django.core.exceptions import ValidationError

from women.models import Women, Category


class AddNewArticle(forms.ModelForm):
    """
    title = forms.CharField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 20}))
    is_published = forms.BooleanField(required=False)
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Category not selected")
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cat"].empty_label = "Category not selected"

    class Meta:
        model = Women
        fields = ("title",
                  "content",
                  "photo",
                  "is_published",
                  "cat")

        widgets = {"title": forms.TimeInput(attrs={"class": "form-input"}),
                   "content": forms.Textarea(attrs={"cols": 100, "rows": 20})}

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 2:
            raise ValidationError("Name can't be too short!")
        if len(title) > 30:
            raise ValidationError("Name can't be too long!")

        return title
