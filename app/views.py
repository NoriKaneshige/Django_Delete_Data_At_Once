from django.shortcuts import redirect
from django.views import generic
from .models import Post


""" In case that delete() by using filter() """

# class PostIndex(generic.ListView):
# 	model = Post

# 	def post(self, request):
# 		post_pks = request.POST.getlist('delete')  # the name 'delete' was set in <input type="checkbox" name="delete" in template
# 		Post.objects.filter(pk__in=post_pks).delete()
# 		return redirect('app:post_list')  # redirecting the template, post_list.html

# request.POST.getlist('delete') gives a list such as ['1','2','3']
# on the other hand, request.POST['name'] gives one value, for example





""" In case that delete() with ModelFormSet """

from django import forms
from django.shortcuts import redirect, render
from .models import Post

PostFormSet = forms.modelformset_factory(Post, fields='__all__', can_delete=True, extra=0)

# can_delete=True enables checklist
# extra=0 disable a form for new post

def postindex(request):
    formset = PostFormSet(request.POST or None)
    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('app:post_list')

    context = {
        'formset': formset,
    }

    return render(request, 'app/post_list.html', context)