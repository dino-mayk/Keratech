from django.db import models


class ProductGalleryManager(models.Manager):
    def product_gallery(self, product_id):
        return (
            self.get_queryset()
                .filter(product__id=product_id)
                .select_related('product')
                .order_by('product')
        )
