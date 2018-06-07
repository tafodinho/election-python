from django.conf.urls import url, include
from election import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register('students', views.StudentViewSet)
router.register('votes', views.VoteViewSet)
router.register('faculties', views.FacultyViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('election_types', views.ElectionTypeViewSet)
router.register('election_session', views.ElectionSessionViewSet)

schema_view = get_schema_view(title='Pastebin API')
urlpatterns = [
        url(r'^', include(router.urls)),
        url(r'^schema/$', schema_view)
    ]
