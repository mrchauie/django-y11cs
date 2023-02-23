from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, View
from django.contrib.auth import login
from .forms import CreateNewUserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
        
class QuestionView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

class LoginView():
    template_name = 'registration/login.html'

class LogoutView():
    template_name = 'polls/index.html'


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return render(request, 'polls/results.html', {
#             'question': question,
#             'question_id': question.id,
#         })
        
class VoteView(View):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'polls/detail.html', {
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return render(request, 'polls/results.html', {
                'question': question,
                'question_id': question.id,
            })

# def register_request(request):
# 	if request.method == "POST":
# 		form = CreateNewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("polls:index")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = CreateNewUserForm()
# 	return render(request, "registration/register.html", {
#         "register_form" : form,
#     })
 
class RegisterUserFormView(FormView):
    template_name = 'registration/register.html'
    form_class = CreateNewUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('polls:index')
        
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterUserFormView, self).form_valid(form)