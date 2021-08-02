"""Custom tags"""
from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Return total number of published posts."""
    return Post.published.count()
