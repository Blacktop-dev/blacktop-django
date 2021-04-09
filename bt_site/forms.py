from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm

# need to add model here when using a form to fill it
from .models import UserProfile, TeeTime
from friendship.models import Friend, Follow, Block

# responsible for username, email, password part of form
class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        help_texts = {
            'username': None,
        }

    def save(self, commit=True):
        new_user = User.objects.create_user(self.cleaned_data['username'],
                                            self.cleaned_data['email'],
                                            self.cleaned_data['password'])
        # new_user.first_name = self.cleaned_data['first_name']
        # new_user.last_name = self.cleaned_data['last_name']
        if commit:
            new_user.save()
        return new_user

# responsible for phone number part of form (and maybe neighborhood and others)
class ProfileForm(ModelForm):
    class Meta:
        # this controls what model is filled with the contents of this form
        model = UserProfile
        # these fields are the model fields that are shown on the form
        fields = ['user_phone_number']


class FriendRequestForm(ModelForm):
    class Meta:
        model = Friend
        fields = {'to_user'}

    def save(self, commit=True):
        other_user = User.objects.get(pk=1)
        #new_request_sent = Friend.objects.add_friend(request.user, other_user, message="Let's be fwands")
        new_request_sent = Friend.to_user(1)

class TeeTimeForm(ModelForm):
    class Meta:
        model = TeeTime
        fields = ['tee_time_course', 'tee_time_date']