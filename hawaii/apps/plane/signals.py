# -*- coding: utf-8 -*-
# __author__ = chenchiyuan

from __future__ import division, unicode_literals, print_function
from django.db.models.signals import m2m_changed


def flight_inventory_changed(sender, instance, *args, **kwargs):
    from libs.datetimes import dates_during
    from hawaii.apps.plane.models import FlightProduct, FlightInventory

    inventory = FlightInventory.objects.select_related().get(pk=instance.pk)
    weekdays = inventory.days.values_list("number", flat=True)

    dates = dates_during(from_date=inventory.begin, to_date=inventory.end, weekdays=weekdays)
    copy_dates = dates[:]
    products = list(inventory.products.all())
    products_will_delete = []
    for product in products:
        if not product.departure.date in copy_dates:
            products_will_delete.append(product.id)
        else:
            dates.remove(product.date)

    # delete products
    FlightProduct.objects.filter(id__in=products_will_delete).delete()

    # create products
    FlightProduct.bulk_create_products(inventory, dates)


def register_flight_inventory_changed():
    from hawaii.apps.plane.models import FlightInventory
    m2m_changed.connect(flight_inventory_changed, sender=FlightInventory.days.through, dispatch_uid='flight_inventory_changed')


def register_flight_signals():
    register_flight_inventory_changed()
    print("plane signal register")