from django.db import models


class ProductGalleryManager(models.Manager):
    def product_gallery(self, item_id):
        return (
            self.get_queryset()
                .filter(item__id=item_id)
                .select_related('item')
                .order_by('item')
        )
