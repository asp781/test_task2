from django.http import Http404
from django.views.generic.base import TemplateView

from .models import Participant
from .forms import ParticipantForm


class ContestView(TemplateView):
    """Страница конкурса"""

    template_name = 'contest/contest.html'
    form_class = ParticipantForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return self.render_to_response({'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            participants = Participant.objects.all().order_by('-id')
            return self.render_to_response({
                'form': form,
                'participants': participants,
                'message':'Спасибо за участие!'})
        # else:
        #     return self.render_to_response({'form': form})
