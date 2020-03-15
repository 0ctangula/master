from .models import Profile


def profile(request):
    profile = Profile.objects.filter(user=request.user)
    for profile in profile:
        return {'userprofile': profile}
    else:
        userprofile = {
            'picture': 'https://wikicdn.web.app/media/cat.png',
        }
        return {'userprofile': userprofile}
