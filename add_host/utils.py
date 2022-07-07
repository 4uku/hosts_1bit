from .forms import HostForm, HostFormAdmin


def form_for_user(user):
    if user.is_staff:
        return HostFormAdmin
    return HostForm
