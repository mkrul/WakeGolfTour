from django.urls import path, include
from django.contrib import admin

from . views import homepage
from golf_course import urls as golf_course_urls
from golfer import urls as golfer_urls
from tournament import urls as tournament_urls
from golfer_polls import urls as golfer_polls_urls

urlpatterns = [
    path(r'^', homepage),
    path('admin/', admin.site.urls),
    path('golf_course/', include(golf_course_urls)),
    path('golfer/', include(golfer_urls)),
    path('tournament/', include (tournament_urls)),
    path('golfer_polls/', include(golfer_polls_urls)),
]

admin.site.site_header = 'Wake Golf Tour'
admin.site.index_title = 'WGT Site Administration'

