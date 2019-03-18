from django.conf.urls import url, include
from django.contrib import admin

from . views import homepage
from golf_course import urls as golf_course_urls
from golfer import urls as golfer_urls
from tournament import urls as tournament_urls

urlpatterns = [
    url(r'^$', homepage),
    url(r'^admin/', admin.site.urls),
    url('golf_course/', include(golf_course_urls)),
    url('golfer/', include(golfer_urls)),
    url('tournament/', include (tournament_urls)),
]

admin.site.site_header = 'Wake Golf Tour'
admin.site.index_title = 'WGT Site Administration'

