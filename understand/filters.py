from django.contrib.auth.models import User
import django_filters
from understand.models import Result
from django_filters import DateFilter, CharFilter

class ResultFilter(django_filters.FilterSet):
	# date = DateFilter(field_name="date",lookup_expr="gte")
	title = CharFilter(field_name="title",lookup_expr="icontains")

	class Meta:
		mdoel = Result
		fields = ['title']