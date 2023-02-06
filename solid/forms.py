from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile, Blogs, Message, HomeWatch

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm, CreateView):
    class Meta:
        model = Profile
        fields = ("profile_pic",)
        template_name = 'profile-picpage.html'

    def clean_avatar(self, request):
        user = request.user
        avatar = self.cleaned_data['avatar']

        try:
            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                    '%s x %s pixels or smaller.' % (max_width, max_height))

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                                            'GIF or PNG image.')

            # validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs
        template_name = 'create-blog.html'
        fields = ['quote', 'quote_giver', 'title', 'blog_paragraph_main1', 'blog_paragraph_sub1',
                  'blog_paragraph_main2', 'blog_paragraph_sub2', 'blog_paragraph_sub2II', 'blog_paragraph_main3',
                  'quote_mid_page', 'quote_last_page', 'thumbnail']

    thumbnail = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),
        help_text="Please make sure the width of image is higher than height."
    )


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message

        fields = ['content']
        labels = {
            'content': 'Comment'
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'label-comment'})
        }


class HomeWatchForm(forms.ModelForm):
    class Meta:
        model = HomeWatch
        fields = ['display', 'name', 'description']
