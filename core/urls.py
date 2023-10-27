from django.urls import path
from core.views import lista_estudantes, criar_estudante, detalhar, editar, deletar_estudante

app_name = "core"

urlpatterns = [
    path('', lista_estudantes, name="lista_estudantes"),
    path('create-student', criar_estudante, name="create-student"),
    path('detail-student/<int:student_id>', detalhar, name="detail-student"),
    path('edit-student/<int:student_id>', editar, name="edit-student"),
    path('delete_student/<int:student_id>', deletar_estudante, name="delete-student"),
]
