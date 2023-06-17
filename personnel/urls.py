from django.urls import path
from .views import (
    DepartmentView, 
    PersonnelListCreate,
    PersonalGetUpdateDelete,
    DepartmentPersonnelView,
    CustomDepartmentPersonnelView,
)

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelListCreate.as_view()),
    path("personnel/<int:pk>/", PersonalGetUpdateDelete.as_view()),
    # path("department/<str:department>/", DepartmentPersonnelView.as_view()),
    path("department/<str:name>/", CustomDepartmentPersonnelView.as_view()),

]
