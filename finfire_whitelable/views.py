from django.shortcuts import redirect

def activation_redirect(request, uid, token):
    # Change this URL to your frontend's activation page
    frontend_url = f"https://facebook.com"
    return redirect(frontend_url)