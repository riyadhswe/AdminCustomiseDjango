from import_export import resources

from App.models import Blog


class BlogResource(resources.ModelResource):
    class Meta:
        model = Blog
