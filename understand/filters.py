from django.contrib.auth.models import User
import django_filters
from understand.models import Result
from django_filters import DateFilter, CharFilter

class ResultFilter(django_filters.FilterSet):
	title = CharFilter(field_name="title",lookup_expr="icontains")

	class Meta:
		mdoel = Result
		fields = ['title']