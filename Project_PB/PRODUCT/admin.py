from django.contrib import admin
from django.contrib.admin.sites import site
from PRODUCT.models import Cat,SubCat,P_Details,Offer
import csv
from django.http import HttpResponse

def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['product_id', 'subcat_id', 'offer_id', 'p_name', 'p_price', 'p_label','p_qty','p_type','p_fabric','p_size','p_img','p_desc','p_color'])
    books = queryset.values_list('product_id', 'offer_id', 'p_name', 'p_price', 'p_label', 'p_qty','p_type','p_fabric','p_img','p_desc','p_color')
    for book in books:
        writer.writerow(book)
    return response
export_books.short_description = 'Export to csv'

class BookAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'offer_id', 'p_name', 'p_price', 'p_label', 'p_qty','p_type','p_fabric','p_img','p_desc','p_color']
    actions = [export_books]


admin.site.register(Cat)
admin.site.register(SubCat)
admin.site.register(P_Details,BookAdmin)
admin.site.register(Offer)