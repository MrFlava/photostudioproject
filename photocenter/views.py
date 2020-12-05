from django.shortcuts import render

from .models import PhotoOffice, PhotoCenter, PhotoStand, Order, ItemOrder, Item, ItemProvider

# Create your views here.


def HomePage(request):
    return render(request, "homepage/index.html")


def PhotoCentres(request):

    photo_centres = PhotoCenter.objects.all()
    context = {"photo_centres": photo_centres}

    return render(request=request, template_name="dashboard/index.html", context=context)


def PhotoCentresOffice(request, center_id):

    photo_offices = PhotoOffice.objects.filter(center=center_id)
    offices_quantity = photo_offices.count()

    context = {'center': center_id, 'photo_offices': photo_offices, 'offices_quantity': offices_quantity}

    return render(request=request, template_name="dashboard/offices.html", context=context)


def PhotoCentresStands(request, center_id):

    photo_stands = PhotoStand.objects.filter(office__center=center_id)
    stands_quantity = photo_stands.count()
    context = {'center': center_id, 'photo_stands': photo_stands, 'stands_quantity': stands_quantity}

    return render(request=request, template_name="dashboard/stands.html", context=context)


def PhotoOfficeOrders(request, office_id, date_from, date_to):

    orders = Order.objects.filter(photo_office=office_id, creation_date__range=[date_from, date_to])

    context = {
        "office": office_id,
        "orders_quantity": orders.count(),
        "orders": orders,
    }

    return render(request=request, template_name="office/orders.html", context=context)


def PhotoOfficeItemOrders(request, office_id, date_to, date_from):

    orders = ItemOrder.objects.filter(item__photo_office=office_id, creation_date__range=[date_from, date_to])

    earnings = 0

    for order in orders:
        earnings += order.item.price

    context = {
        "office": office_id,
        "earnings": earnings,
        "orders": orders,
    }

    return render(request=request, template_name="office/item_orders.html", context=context)


def PhotoOfficePopularItems(request, office_id):

    # print(date_to)
    # print(date_from)

    items = Item.objects.filter(photo_office=office_id)
    most_popular_items = []
    earnings = 0

    for item in items:
        item_orders = ItemOrder.objects.filter(item=item, item__photo_office=office_id)

        if item_orders.count() > 1:
            most_popular_items.append(item)

    context = {
        "office": office_id,
        "most_popular_items": most_popular_items
    }

    return render(request=request, template_name="homepage/index.html", context=context)


def PhotoOfficeStatusOrders(request, office_id, priority, date_to, date_from):

    earnings = 0

    orders = Order.objects.filter(photo_office=office_id, priority=priority, creation_date__range=[date_from, date_to])

    for order in orders:
            earnings += order.price

    context = {
            "office": office_id,
            "orders_quantity": orders.count(),
            "earnings": earnings,
            "orders": orders,
        }

    return render(request=request, template_name="office/orders.html", context=context)


def PhotoOfficeFilmDevelopmentOrders(request, office_id, priority, date_to, date_from):

    film_developed = 0

    orders = Order.objects.filter(photo_office=office_id, priority=priority, creation_date__range=[date_from, date_to], order_type='FILM_DEVELOPMENT')

    for order in orders:
            film_developed += 1

    context = {
            "office": office_id,
            "orders_quantity": orders.count(),
            "film_developed": film_developed,
            "orders": orders,
        }

    return render(request=request, template_name="office/orders.html", context=context)


def PhotoOfficeOrderCustomer(request, office_id, photos_quantity):


    customers = []

    orders = Order.objects.filter(photo_office=office_id, photos_quantity__lte=photos_quantity)

    for order in orders:
        customers.append(order.customer)

    context = {
        "office": office_id,
        "orders": orders
    }

    return render(request=request, template_name="office/customers.html", context=context)


def PhotoOfficeItemProviders(request, office_id, item_quantity):

    items = Item.objects.filter(photo_office=office_id, quantity=item_quantity)

    providers = []

    for item in items:
        provider_items = ItemProvider.objects.filter(item=item)

        for provider_item in provider_items:
            providers.append(provider_item.provider)

    context = {
        "office": office_id,
        "providers": providers
    }

    return render(request=request, template_name="office/providers.html", context=context)


def PhotoOfficePrintingDevelopmentOrders(request, office_id, priority, date_to, date_from):

    printing_and_development = 0

    orders = Order.objects.filter(photo_office=office_id, priority=priority, creation_date__range=[date_from, date_to])

    for order in orders:
            printing_and_development += 1

    context = {
            "office": office_id,
            "orders_quantity": orders.count(),
            "printing_and_development": printing_and_development,
            "orders": orders,
        }

    return render(request=request, template_name="office/orders.html", context=context)


def PhotoStandOrders(request, stand_id, date_to, date_from):

    orders = Order.objects.filter(photo_stand=stand_id, creation_date__range=[date_from, date_to])

    context = {
        "stand": stand_id,
        "orders_quantity": orders.count(),
        "orders": orders,
    }

    return render(request=request, template_name="homepage/index.html", context=context)


def PhotoStandItemOrders(request, stand_id):

    orders = ItemOrder.objects.filter(item__photo_stand=stand_id)
    earnings = 0

    for order in orders:
        earnings += order.item.price

    context = {
        "stand": stand_id,
        "earnings": earnings,
        "orders": orders,
    }

    return render(request=request, template_name="stand/item_orders.html", context=context)


def PhotoStandStatusOrders(request, stand_id, date_from, date_to):

    earnings = 0

    orders = Order.objects.filter(photo_stand=stand_id,  priority='ORDINARY_PRIORITY',
                                  creation_date__range=[date_from, date_to])

    for order in orders:
        earnings += order.price

    context = {
            "stand": stand_id,
            "orders_quantity": orders.count(),
            "earnings": earnings,
            "orders": orders,
        }

    return render(request=request, template_name="stand/orders.html", context=context)


def PhotoStandFilmDevelopmentOrders(request, stand_id, date_from, date_to):

    film_developed = 0
    stand_orders = Order.objects.filter(photo_stand=stand_id)

    orders = stand_orders.filter(photo_stand=stand_id,  priority='ORDINARY_PRIORITY',  creation_date__range=[date_from, date_to], order_type='FILM_DEVELOPMENT')

    for order in orders:
        film_developed += 1

    context = {
            "stand": stand_id,
            "film_developed": film_developed,
            "orders": orders,
        }

    return render(request=request, template_name="stand/orders.html", context=context)


def PhotoStandPrintingDevelopmenttOrders(request, stand_id, date_from, date_to):

    printing_and_development = 0
    stand_orders = Order.objects.filter(photo_stand=stand_id)

    orders = stand_orders.filter(photo_stand=stand_id,  priority='ORDINARY_PRIORITY',  creation_date__range=[date_from, date_to], order_type='PHOTO_PRINTING_AND_DEVELOPMENT')

    for order in orders:
        printing_and_development += 1

    context = {
            "stand": stand_id,
            "printing_and_development": printing_and_development,
            "orders": orders,
        }

    return render(request=request, template_name="stand/orders.html", context=context)


def PhotoStandItemProviders(request, stand_id, item_quantity):

    items = Item.objects.filter(photo_stand=stand_id, quantity=item_quantity)

    providers = []

    for item in items:
        provider_items = ItemProvider.objects.filter(item=item)

        for provider_item in provider_items:
            providers.append(provider_item.provider)

    context = {
        "stand": stand_id,
        "providers": providers
    }

    return render(request=request, template_name="stand/providers.html", context=context)
