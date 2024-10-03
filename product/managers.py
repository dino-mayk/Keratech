from django.db import models


class PostsManager(models.Manager):
    def homepage(self):
        return (
            self.get_queryset()
                .filter(status=True)
                .select_related('user')
                .order_by('title')
        )

    def dogfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=2,
            **kwargs)

    def catfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=1,
            **kwargs)

    def otherfilter(self, *args, **kwargs):
        return self.homepage().filter(
            animal_type=3,
            **kwargs)


class PostsGalleryManager(models.Manager):
    def post_gallery(self, item_id):
        return (
            self.get_queryset()
                .filter(item__id=item_id)
                .select_related('item')
                .order_by('item')
        )