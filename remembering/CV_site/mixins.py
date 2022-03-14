from django.views.generic import View
from .models import Visitor


class ViewMixin(View):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            visitor = Visitor.objects.filter(user=request.user).first()
            # if not customer:
            #     customer = Visitor.objects.create(
            #         user=request.user
            #     )
        return super().dispatch(request, *args, **kwargs)
