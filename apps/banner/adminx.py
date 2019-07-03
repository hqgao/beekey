import xadmin
from xadmin import views


class BaseSetting(object):
    site_title = '后台管理系统'
    site_footer = '后台管理系统'

xadmin.site.register(views.CommAdminView, BaseSetting)



from .models import bannerModel


class bannerAdmin(object):
    list_display = ["id", "name", "update_time", "add_time"]
    ordering = ["-id"]


xadmin.site.register(bannerModel, bannerAdmin)
