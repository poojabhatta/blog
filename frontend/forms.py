from dashboard.models import Comment


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment 
        fields = ['comment', 'time', 'user']