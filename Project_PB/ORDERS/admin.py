from django.contrib import admin
from django.contrib.admin.sites import site
from ORDERS.models import details
from DASHBOARD.models import Customer_details
from PRODUCT.models import P_Details
import csv
from django.http import HttpResponse

def export_books(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reports.csv"'
    writer = csv.writer(response)
    writer.writerow(['order_id','customer_id','Product_id','Quantity','NetAmount','OrderDate','Deatils','Status'])
    Reports = queryset.values_list('o_id','cust_id','p_id','o_qty','o_netamount','o_date','o_details','o_status')
    for Report in Reports:
        writer.writerow(Report)
    return response 
export_books.short_description = 'Export to csv'

class HeroAdmin(admin.ModelAdmin):
    list_display = ['o_id','cust_id','p_id','o_qty','o_netamount','o_date','o_details','o_status']
    date_hierarchy = 'o_date'
    actions = [export_books]
    
admin.site.register(details,HeroAdmin)
