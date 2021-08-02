"""Custom tags"""
from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Return total number of published posts."""
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    """The most recently published posts."""
    latest_posts = Post.published.order_by('-publish')[:count]
    return dict(latest_posts=latest_posts)


@register.simple_tag
def get_most_commented_posts(count=5):
    """Get the published posts with the most comments."""
    return Post.published.annotate(total_comments=Count('comments')
                                   ).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    """Convert text to markdown format."""
    return mark_safe(markdown.markdown(text))
