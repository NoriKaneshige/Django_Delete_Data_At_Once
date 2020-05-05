# Django_Delete_Files_At_Once

[referred blog](https://narito.ninja/blog/detail/90/)

![delete-selected-data-at-once](delete-selected-data-at-once.gif)

> ## models.py
``` python
from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)

	# def __str__(self):
	#     return self.file.url

	def __str__(self):
		return self.title
```

> ## admin.py
``` python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

> ## views.py
``` python
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

```

> ## urls.py
``` python
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    # path('', views.PostIndex.as_view(), name='post_list'), # as_view() is necessary because PostIndex view uses ListView
    path('', views.postindex, name='post_list'), # as_view() is NOT necessary because postindex view is a nomal view
   
]
```

> ## post_list.html
``` python
<!-- In case that delete() by using filter() -->
<!-- <form action="" method="POST">
		{% for post in post_list %}
			<p>post title:{{ post.title }} - delete: <input type="checkbox" name="delete" value="{{ post.pk }}"></p>
		{% endfor %}
		{% csrf_token %}
		<button type="submit">delete</button>
</form> -->



<form action="" method="POST">
        {{ formset.management_form }}
        {% for form in formset %}
            {% for field in form.hidden_fields %}{{ field }}{% endfor %}
            <!-- {{ form.title.as_hidden }} hides input area of post title -->
            {{ form.title.as_hidden }}
            <p>the title of post:{{ form.instance.title }} - {{ form.DELETE }}</p>
            <!-- {{ form.DELETE }} is a checkbox that modelformset has -->
        {% endfor %}
        {% csrf_token %}
        <button type="submit">delete</button>
</form>
```
