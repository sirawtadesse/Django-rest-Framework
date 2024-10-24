from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit=False)
        # Add custom logic, e.g., setting a default role for social signup
        if not user.role:
            user.role = 'football_player'
        if commit:
            user.save()
        return user
