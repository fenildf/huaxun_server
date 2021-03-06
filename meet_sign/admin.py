#coding:utf-8
from django.contrib import admin

# Register your models here.
from meet_sign.models import *


##class ImageLibraryAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(ImageLibrary,ImageLibraryAdmin)
##
####2
##class ArticleLibraryAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(ArticleLibrary,ArticleLibraryAdmin)
##
####3
##class PageAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(Page,PageAdmin)
##
####4
##class MeetAdmin(admin.ModelAdmin):
##    pass
##admin.site.register(Meet,MeetAdmin)

##5
class CostAdmin(admin.ModelAdmin):
    list_display = ('id','name_admin','name',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "meet":
            kwargs["queryset"] = Meet.objects.filter(father = None)
        return super(CostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Cost,CostAdmin)

##6
class DiscountTemplateAdmin(admin.ModelAdmin):
    pass
admin.site.register(DiscountTemplate,DiscountTemplateAdmin)


##6.2
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)
admin.site.register(Attendee,AttendeeAdmin)

##6.2
class SignAdmin(admin.ModelAdmin):
    list_display = ('id','attendee','cost','is_alive',)
    # list_editable = ('is_alive',)
    pass
admin.site.register(Sign,SignAdmin)


##7
class DiscountAdmin(admin.ModelAdmin):
    pass
admin.site.register(Discount,DiscountAdmin)

##8
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','sign','wx_out_trade_no','sign','origin_price','pay_price','is_pay','is_alive',)
admin.site.register(Order,OrderAdmin)

##9
##class CoverAdmin(admin.ModelAdmin):
##    list_display = ('id','page','meet','article',)
##    raw_id_fields = ('cover_image','logo_image',)  #选择封面图片
##admin.site.register(Cover,CoverAdmin)

