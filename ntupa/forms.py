from extra_views import InlineFormSet

from . import models

class UserProfileInline(InlineFormSet):
    model = models.UserProfile
    fields = ['cellphone']
    can_delete = False

    def get_object(self):
        return models.UserProfile.objects.get(user=self.request.user)