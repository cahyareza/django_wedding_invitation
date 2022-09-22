from allauth.account.forms import SignupForm
from allauth.account.forms import LoginForm

class MyCustomSignupForm(SignupForm):


    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

    def __init__(self, *args, **kwargs):
        super(MyCustomSignupForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'input'
            })

class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super(MyCustomLoginForm, self).__init__(*args, **kwargs)

        self.fields['login'].widget.attrs.update({
            'class': 'input'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input'
        })
        self.fields['remember'].widget.attrs.update({
            'class': 'checkbox'
        })