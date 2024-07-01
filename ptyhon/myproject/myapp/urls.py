# INI ADALAH MODUL DJANGO YG DIGUNAKAN UNTUK KONFIG URL
from django.urls import path
# Mengimpor Ke Views
from . import views 

# INI ADALAH DAFTAR YANG BERISI SEMUA POLA URL MENGHUBUNGKAN POLA YG DI MINTA DENGAN FUNGSI VIEWS YANG AKAN MENANGANI
urlpatterns = [
    #URL KE HOME.HTML
    path('', views.start, name='start'),
    #URL KE SEQUENTIAL.HTML
    path('sequentialsearch/', views.sequentialsearch, name='sequentialsearch'),
    #URL KE BINARY.HTML
    path('binarysearch/', views.binarysearch, name='binarysearch'),
    #URL KE GROUP.HTML
    path('group/', views.group, name='group'),
    #URL UNTUK MENYIMPAN DATA TERSIMPAN
    path('save_data/', views.save_data, name='save_data'),
    #URL UNTUK MENGHAPUS DATA YG SUDAH DI SIMPAN
    path('delete_data/', views.delete_data, name='delete_data'),
]
