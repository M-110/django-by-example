"""Blogs views"""
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .forms import EmailPostForm
from .models import Post


def post_detail(request, year, month, day, post):
    """Page for an individual blog post."""
    post = get_object_or_404(Post,
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

def post_share(request, post_id):
    """Form for sharing a post."""
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} as {post_url}\n\n {cd['name']}'s " \
                      f"comments: {cd['comments']}"
            send_mail(subject, message, 'admin@mysite.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html',
                  dict(post=post,
                       form=form,
                       sent=sent))


class PostListView(ListView):
    """A class based view of the list of blog posts."""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
