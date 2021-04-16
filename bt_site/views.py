from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.views.generic import TemplateView, ListView, CreateView
from django.views.generic.base import View
from friendship.models import Friend, Follow, Block

from .forms import ProfileForm, TeeTimeForm
from .forms import UserForm#, FriendRequestForm
from .models import User, UserProfile, TeeTime, TeeTimeGroup
from .filters import UserFilter
from django.contrib.auth.decorators import login_required


try:
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
except ImportError:
    from django.contrib.auth.models import User

    user_model = User

### TEMPLATE VIEWS ###

class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        ctx = super(SignUpView, self).get_context_data(**kwargs)
        ctx['user_form'] = UserForm(prefix='user')
        ctx['profile_form'] = ProfileForm(prefix='profile')
        return ctx

    def post(self, request, *args, **kwargs):
        user_form = UserForm(request.POST, prefix='user')
        profile_form = ProfileForm(request.POST, request.FILES, prefix='profile')
        if profile_form.is_valid() and user_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            user.save()
            profile.user = user
            profile.save()
            return HttpResponse("Signed Up!<br><a href='/'>Go to home</a>")
        else:
            return HttpResponse("Error : <a href='/signup'>Try again</a>!")

class LoginView(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['loggedIn'] = False
        if self.request.user.is_authenticated:
            ctx['loggedIn'] = True
        return ctx

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('Error: User authentication error <a href="/login"">Try again</a>')
        else:
            return HttpResponse('Error: Username or password is empty <a href="/login">Try again</a>')

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['loggedIn'] = False
        if self.request.user.is_authenticated:
            ctx['loggedIn'] = True
        return ctx

#Jess - tee time create view
class AddTeeTimeView(TemplateView):
    template_name = 'add_tee_time.html'

    def get_context_data(self, **kwargs):
        ctx = super(AddTeeTimeView, self).get_context_data(**kwargs)
        ctx['tee_time_form'] = TeeTimeForm(prefix='tee')
        ctx['loggedIn'] = False
        if self.request.user.is_authenticated:
            ctx['loggedIn'] = True
        return ctx

    def post(self, request, *args, **kwargs):
        tee_time_form = TeeTimeForm(request.POST, prefix='tee')
        if tee_time_form.is_valid():
            tee_time = tee_time_form.save(commit=False)
            tee_time.save()
            tee_time.tee_time_users.set([self.request.user.userprofile])
            tee_time.save()
            #group_obj = TeeTimeGroup.objects.filter(tee_group_date=cleaned_info[tee_time.tee_time_date])
            group_obj = TeeTimeGroup.objects.filter(tee_group_date=tee_time.tee_time_date)
            if group_obj.count() == 0:
                gg = TeeTimeGroup(tee_group_date=tee_time.tee_time_date)
                gg.save()
                gg.tee_group_members.set([tee_time])
            else:
                group_obj = TeeTimeGroup.objects.get(tee_group_date=tee_time.tee_time_date)
                group_obj.tee_group_members.add(tee_time)
            return HttpResponse("Made the tee!<br><a href='/my_tee_times'>Go to home</a>")
        else:
            return HttpResponse("Error with tee : <a href='/signup'>Try again</a>!")



class FindRidesView(TemplateView):
    template_name = 'find_rides.html'

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['loggedIn'] = False
        if self.request.user.is_authenticated:
            ctx['loggedIn'] = True
            ctx['tee_times'] = TeeTimeGroup.objects.all().order_by('tee_group_date').reverse()
        return ctx

class MyTeeTimesView(TemplateView):
    template_name = 'my_tee_times.html'

    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['loggedIn'] = False
        if self.request.user.is_authenticated:
            ctx['loggedIn'] = True
            UserP = self.request.user.userprofile
            #the tee_time_potential_users refers to the related name in the model, so don't have to use _set.all()
            ctx['tee_times'] = UserP.tee_time_users.all()
            ctx['user'] = self.request.user
        return ctx



### GENERAL VIEWS ###

class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('/')

def sent_success(request):
	return render(request, "friend_request_success.html")

# class Display(ListView):
#     template_name = 'display.html'
#     model = User

#     def get_queryset(self):
#         # original qs
#         qs = super().get_queryset() 
#         return qs#.filter(name__startswith=self.kwargs['name'])

# class ProfileView(TemplateView):
#     template_name = 'myprofile.html'

#     def get_context_data(self, **kwargs):
#         ctx = {}
#         ctx['loggedIn'] = False
#         if self.request.user.is_authenticated:
#             ctx['loggedIn'] = True
#         return ctx

# class FriendsView(TemplateView):
#     template_name = 'friends.html'

#     def get_context_data(self, **kwargs):
#         ctx = {}
#         ctx['loggedIn'] = False
#         if self.request.user.is_authenticated:
#             ctx['loggedIn'] = True
#             ctx['friends'] = Friend.objects.friends(user=self.request.user)
#         return ctx

# class FriendRequestView(TemplateView):
#     template_name = 'friendrequest.html'

#     def get_context_data(self, **kwargs):
#         ctx = {}
#         ctx['loggedIn'] = False
#         if self.request.user.is_authenticated:
#             ctx['loggedIn'] = True
#             ctx['friend_list'] = Friend.objects.unread_requests(user=self.request.user)
#         return ctx


# #TO DO: filter so that its only users that are not already friends with the person logged in
# class displayAll(ListView):
# 	template_name = "display_all.html"
# 	model = UserProfile

# 	def get_context_data(self, **kwargs):
# 		ctx = super().get_context_data(**kwargs)
# 		ctx['filter'] = UserFilter(self.request.GET, queryset=self.get_queryset())
# 		return ctx

#TO DO: Make sure login_required functionality is working
@login_required
def friendship_add_friend(
    request, to_username, to_teetime, template_name="add_friend.html"
):
    """ Create a FriendshipRequest """
    to_user = user_model.objects.get(username=to_username)
    relevant_teetime = to_teetime
    ctx = {"to_username": to_username, "target_person": to_user, "to_teetime": to_teetime}

    if request.method == "POST":
        #to_user = user_model.objects.get(username=to_username)
        from_user = request.user
        try:
            Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            #return redirect("friendship_request_list")
            return redirect('/sent/success/')

    return render(request, template_name, ctx)

@login_required
def add_friendteetime(
    request, to_username, to_teetime, template_name="add_teetime.html"
):
    """ Create a FriendshipRequest """
    to_user = user_model.objects.get(username=to_username)
    to_teetime = TeeTime.objects.get(id=to_teetime)
    #relevant_teetime = to_teetime
    ctx = {"to_username": to_username, "target_person": to_user, "to_teetime": to_teetime}

    if request.method == "POST":
        from_user = request.user
        try:
            to_teetime.tee_time_potential_users.set([from_user.userprofile])
            to_teetime.save()
            ctx["to_teetime"] = to_teetime
            #Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect('/sent/success/')

    return render(request, template_name, ctx)


@login_required
def accept_teetime_request(
    request, to_username, to_teetime, template_name="accept_teetime.html"
):
    """ Create a FriendshipRequest """
    to_user = user_model.objects.get(username=to_username)
    to_teetime = TeeTime.objects.get(id=to_teetime)
    #relevant_teetime = to_teetime
    ctx = {"to_username": to_username, "target_person": to_user}

    if request.method == "POST":
        from_user = request.user
        try:
            to_teetime.tee_time_users.add(to_user.userprofile)
            to_teetime.tee_time_potential_users.remove(to_user.userprofile)
            to_teetime.save()
            ctx["to_teetime"] = to_teetime
            #Friend.objects.add_friend(from_user, to_user)
        except AlreadyExistsError as e:
            ctx["errors"] = ["%s" % e]
        else:
            return redirect('/sent/success/')

    return render(request, template_name, ctx)


# '''class addFriend(TemplateView)
#     template_name = 'login.html'
#     def post(self, request, *args, **kwargs):'''

# @login_required
# def friendship_request_list(
#     request, template_name="friendship/friend/requests_list.html"
# ):
#     """ View unread and read friendship requests """
#     friendship_requests = Friend.objects.requests(request.user)
#     # This shows all friendship requests in the database
#     # friendship_requests = FriendshipRequest.objects.filter(rejected__isnull=True)

#     return render(request, template_name, {"requests": friendship_requests})