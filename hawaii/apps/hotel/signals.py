# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db.models.signals import m2m_changed


def hotel_inventory_changed(sender, instance, *args, **kwargs):
    from libs.datetimes import dates_during
    from hawaii.apps.hotel.models import HotelProduct, HotelInventory

    inventory = HotelInventory.objects.select_related().get(pk=instance.pk)
    weekdays = inventory.days.values_list("number", flat=True)

    dates = dates_during(from_date=inventory.begin, to_date=inventory.end, weekdays=weekdays)
    copy_dates = dates[:]
    products = list(inventory.products.all())
    products_will_delete = []
    for product in products:
        if not product.check_in_time.date in copy_dates:
            products_will_delete.append(product.id)
        else:
            dates.remove(product.date)

    # delete products
    HotelProduct.objects.filter(id__in=products_will_delete).delete()

    # create products
    HotelProduct.bulk_create_products(inventory, dates)


def register_hotel_inventory_changed():
    from hawaii.apps.hotel.models import HotelInventory
    m2m_changed.connect(hotel_inventory_changed, sender=HotelInventory.days.through, dispatch_uid='hotel_inventory_changed')


def register_hotel_signals():
    register_hotel_inventory_changed()
    print("hotel signal register")