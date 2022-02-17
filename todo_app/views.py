from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo_app.forms import AddTodoForm, UpdatePictureProfile, CommentForm  # ,UpdatePictureProfile
from todo_app.models import TodoModel, Profile, Comment
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import TodoSerializer


class ListTodoViews(ListView):
    model = TodoModel
    template_name = 'todo_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class DeleteTodoViews(DeleteView):
    model = TodoModel
    template_name = 'todo_app/delete_todo.html'
    success_url = reverse_lazy('list_todos')


class CreateTodoViews(CreateView):
    model = TodoModel
    form_class = AddTodoForm
    template_name = 'todo_app/create_todo.html'


class EditTodoView(UpdateView):
    model = TodoModel
    form_class = AddTodoForm
    template_name = 'todo_app/update_todo.html'


class DetailTodoView(DetailView):
    model = TodoModel
    template_name = 'todo_app/detail_todo.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailTodoView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(TodoModel, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        # context['now'] = timezone.now()
        # context['total_likes'] = total_likes
        context['liked'] = liked
        return context


"""
Starting with serialization
"""


@csrf_exempt
def todo_list_serializer(request):
    if request.method == "GET":
        todos = TodoModel.objects.all()
        serializer = TodoSerializer(todos, many=True)

        return JsonResponse(serializer.data, safe=False, json_dumps_params={'indent': 2})

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, status=201, json_dumps_params={'indent': 2})

        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def todo_detail_serializer(request, pk):
    try:
        todo = TodoModel.objects.get(pk=pk)
    except TodoModel.DoesNotExist:
        # return redirect('list_todos')
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = TodoSerializer(todo)
        return JsonResponse(serializer.data, json_dumps_params={'indent': 2})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TodoSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, json_dumps_params={'indent': 2})
        return JsonResponse(serializer.errors, status=404)

    elif request.method == "DELETE":
        todo.delete()
        return HttpResponse(status=204)


class TodoListApi(APIView):

    def get(self, request, format=None):
        if request.method == "GET":
            todos = TodoModel.objects.all()
            serializer = TodoSerializer(todos, many=True)

            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailApi(APIView):

    def get_object(self, pk):
        try:
            return TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk)
        serial = TodoSerializer(todo, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def like_todo(request, pk):
    todo = get_object_or_404(TodoModel, id=request.POST.get('todo_id'))
    liked = False
    if todo.likes.filter(id=request.user.id).exists():
        todo.likes.remove(request.user)
        liked = False
    else:
        todo.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('detail_todo', args=[str(pk)]))


class EditProfilePictureView(UpdateView):
    model = Profile
    form_class = UpdatePictureProfile
    template_name = 'todo_app/profile_pic.html'


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'todo_app/add_comment.html'

    def form_valid(self, form, *args, **kwargs):
        form.instance.todo_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('list_todos')




