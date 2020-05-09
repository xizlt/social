import django_filters
from django.contrib.auth.models import User
from django_filters import DateFilter, CharFilter, IsoDateTimeFilter

from posts.models import Post


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'first_name']


class PostFilter(django_filters.FilterSet):
    start_date = IsoDateTimeFilter(field_name="created", lookup_expr='gte')
    end_date = IsoDateTimeFilter(field_name="created", lookup_expr='lte')
    description = CharFilter(field_name='description', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')

    # class Meta:
    #     model = Post
    #     fields = ['created']
