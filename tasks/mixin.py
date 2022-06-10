from django.urls import reverse_lazy
from django.views.generic import CreateView


class ObjectCreateMixin(CreateView):
    form_class = None
    template_name = None

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            'tasks:task_list',
            kwargs={'username': self.request.user.username}
        )
