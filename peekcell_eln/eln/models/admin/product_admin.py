from django.contrib import admin

@admin.action(description='Open selected products')
def open_products(modeladmin, request, queryset):
    for product in queryset:
        product.open()

@admin.action(description='Close selected products')
def close_products(modeladmin, request, queryset):
    for product in queryset:
        product.close()
