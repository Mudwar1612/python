#INI DIGUNAKAN UNTUK MERENDER HALAMAN HTML.
from django.shortcuts import render, redirect 
from .models import DataEntry #INI DIGUNAKAN UNTUK MENGIMPOR MODEL DataEntry YG BERADA DI BINARY, DIGUNAKAN UNTUK BERINTERAKSI DENGAN DATABASE, SEPERTI MENYIMPAN MENGAMBIL, ATAU MEMODIFIKASI.
import random #INI BERFUNGSI UNTUK MENGHASILKAN DATA YG DISIMPAN AWAL KALI PADA BINARY SEARCH SAMA SEPERTI YG TELAH DI INPUTKAN DARI AWAL(SECARA ACAK) 

# Create your views here.

#START 
def start(request):
    return render(request, 'start.html')

#GROUP
def group(request):
    return render(request, 'group.html')

# SEQUENTIAL SEARCH
# logika search sequential
def sequential_search_all_indices(data_list, target): 
    indices = [] 
    for index, item in enumerate(data_list):
        if item == target:
            indices.append(index)
    return indices if indices else -1

# Mengambil semua data dari database
def sequentialsearch(request):
    data_store = list(DataEntry.objects.all()) #Mengambil semua entri dari tabel DataEntry
    data_list = [entry.data for entry in data_store] #Menyimpan hanya bagian data dari setiap entri.
    search_result = None
    
    # Untuk Aksi Di Dalam Halamannya (FUNC TOMBOL)
    if request.method == 'POST':
        # Memproses Pencarian
        if 'search' in request.POST:
            target = request.POST.get('target')
            search_result = sequential_search_all_indices(data_list, target)  # Panggil fungsi sequential_search_all_indices
        # Penambahan Data Baru
        elif 'add' in request.POST:
            new_data = request.POST.get('new_data')
            if new_data:
                DataEntry.objects.create(data=new_data)
                data_list.append(new_data)
        # Penghapusan Data
        elif 'delete' in request.POST:
            del_data = request.POST.get('del_data')
            if del_data in data_list:
                DataEntry.objects.filter(data=del_data).delete()
                data_list.remove(del_data)
    
    return render(request, 'sequentialsearch.html', {'data_list': data_list, 'search_result': search_result})

#BINARY SEARCH
def binarysearch(request):
    data_store = list(DataEntry.objects.all()) #mengambil data
    result = None
    search_data = None
    data_found = None

    if request.method == 'POST':
        search_data = request.POST.get('search_data')
        if search_data:
            data_store.sort(key=lambda entry: entry.data)  # Urutkan berdasarkan data sebelum mencari
            data_list = [entry.data for entry in data_store]
            indices = binary_search_all_indices(data_list, search_data)
            data_found = len(indices) > 0
            result = {'search_data': search_data, 'indices': indices}
        else:
            random.shuffle(data_store)  # Acak urutan data

    return render(request, 'binarysearch.html', {
        'result': result,
        'data_store': data_store,
        'search_data': search_data,
        'data_found': data_found
    })

#Logika Binary Search
def binary_search_all_indices(arr, x):
    indices = []
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == x:
            indices.append(mid)
            left = mid - 1
            while left >= l and arr[left] == x:
                indices.append(left)
                left -= 1
            right = mid + 1
            while right <= r and arr[right] == x:
                indices.append(right)
                right += 1
            return indices
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return indices

def save_data(request):
    if request.method == 'POST':
        new_data = request.POST.get('new_data')
        if new_data:
            DataEntry.objects.create(data=new_data) #menyimpan data
    return redirect('binarysearch')

def delete_data(request):
    if request.method == 'POST':
        data_to_delete = request.POST.get('data_to_delete')
        if data_to_delete:
            DataEntry.objects.filter(data=data_to_delete).delete() #penghapusan data
    return redirect('binarysearch')