# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

@login_required
def profile(request):
    user = request.user
    try:
        profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # If the user profile doesn't exist, create one
        profile = UserProfile(user=user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            # Update user profile information based on the form data
            user.save()
            form.save()  # This will save the UserProfile instance with the updated data
            # return render(request, 'profile/profile.html', context);  # Redirect to the profile page after updating
    else:
        # If it's a GET request, initialize the form with current user data
        form = UserProfileForm(instance=profile)

    context = {
        'username': user.username,
        'email': user.email,
        'phone_number': profile.phone_number,
        'profile_picture': profile.profile_picture,
        'form': form,
    }

    return render(request, 'profile/profile.html', context)
