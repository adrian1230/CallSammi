from django.contrib.auth.models import User
import django_filters
from understand.models import Result
from understand.models import categories
from django_filters import DateFilter, CharFilter
from django_filters import ChoiceFilter

class ResultFilter(django_filters.FilterSet):
	title = CharFilter(field_name="title",lookup_expr="icontains")
	category = ChoiceFilter(field_name="category",choices=categories)
	class Meta:
		mdoel = Result
		fields = ['title','category']