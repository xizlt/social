from .models import Action


def notification(request):
    if request.user.is_authenticated:
        following_ids = request.user.following.values_list('id', flat=True)
        actions = Action.objects.exclude(user=request.user).filter(user_id__in=following_ids)
        actions_count = actions.select_related('user', 'user__profile').prefetch_related('target')
        actions = actions_count[:5]
    else:
        actions = []
        actions_count = []
    return {'notifications': actions, 'actions_count': actions_count}
