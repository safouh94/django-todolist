# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .forms import TodoForm, UserForm

from django.views import generic
from django.views.generic import View

from .models import Todo


# class IndexView(generic.ListView):
#     template_name = 'todos/index.html'
#     context_object_name = 'todos'
#
#     def get_queryset(self):
#         return Toodo.objects.all()
def index(request):
    if not request.user.is_authenticated:
        context = {
            'error_message': "You're not a user!" 
                             "  Login or Signup by clicking Above!"
        }
        return render(request, 'todos/index.html', context)


    else:
        todos = Todo.objects.all()

        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():

                owner = form.save(commit=False)
                owner.user = request.user
                owner.save()

                form = TodoForm()
        else:
            form = TodoForm()
        context = {
            'todos': todos,
            'form': form,
        }

        return render(request, 'todos/index.html', context)
    # else:
    #     # render(request, 'todos/index.html', {'error_message': "You're NOT AUTHORIZED to be HERE!"})
    #     HttpResponse("You're NOT AUTHORIZED to be HERE!")


class DetailView(generic.DetailView):
    model = Todo
    template_name = 'todos/detail.html'


class TodoDelete(generic.DeleteView):
    model = Todo
    success_url = reverse_lazy('todo:index')


def achieved(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    # try:
    #     selected_todo = toodo.objects.get(pk=request.POST['toodo'])
    # except (KeyError, Toodo.DoesNotExist):
    #     return render(request, 'todos/detail.html', {
    #         'toodo':toodo,
    #         'error_message': "You did not select a valid toodo",
    #     })
    # else:
    if todo.is_achieved:
        todo.is_achieved = False
        todo.save()
    else:
        todo.is_achieved = True
        todo.save()
    return render(request, 'todos/detail.html', {'todo': todo})


# class UserFormView(View):
#     form_class = UserForm
#     template_name = 'todos/registration_form.html'
#
#     # display blank form
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#
#         if form.is_valid():
#
#             user = form.save(commit=False)
#
#             # cleaned (normalized) data
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user.set_password(password)
#             user.save()
#
#             # returns User objects if credentials are correct
#             user = authenticate(username=username, password=password)
#
#             if user is not None:
#
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('todo:index')
#         return render(request, self.template_name, {'form': form})


# def logout_user(request):
#     logout(request)
#     form = UserForm(request.POST or None)
#     context = {
#         "form": form,
#     }
#     # return render(request, 'todos/index.html', context)
#     return HttpResponseRedirect('../')
#
#
# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 todos = Todo.objects.all()
#                 # return render(request, 'todos/index.html', {'todos': todos})
#                 return HttpResponseRedirect('../')
#             else:
#                 return render(request, 'todos/login.html', {'error_message': 'Your account has been disabled'})
#         else:
#             return render(request, 'todos/login.html', {'error_message': 'Invalid login'})
#     return render(request, 'todos/login.html')


# ------------------------------------------


# class TodoCreate(CreateView):
#     model = Todo
#     fields = ['title', 'text', 'created_at', 'to_be_completed', 'is_achieved']


# def index(request):
#     todos = Toodo.objects.all()
#
#     if request.method == 'POST':
#         form = TodoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             form = TodoForm()
#
#     else:
#         form = TodoForm()
#
#     context = {
#         'todos': todos,
#         'form': form,
#     }
#
#     return render(request, 'todos/index.html', context)
#
#
# def detail(request, todo_id):
#     toodo = get_object_or_404(Toodo, pk=todo_id)
#     context = {
#         'toodo': toodo,
#     }
#     return render(request, 'todos/detail.html', context)


# def delete_todo(request, todo_id):
#     # +some code to check if New belongs to logged in user
#     dele = Toodo.objects.get(pk=id)
#     delete = dele.delete()
#
#     template = loader.get_template('todos/delete_todo.html')
#
#     context = {
#         'delete': delete
#     }
#
#     return HttpResponse(template.render(context, request))
