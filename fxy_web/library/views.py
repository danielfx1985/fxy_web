from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import Book
from django.shortcuts import render,redirect,reverse
from .forms import BookForm
from django.shortcuts import get_object_or_404

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library/book_list.html', context)

def book_search(request):
    query = request.GET.get('q')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

'''def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/library')'''

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'GET':
        book.delete()
        return redirect('/library')
    return render(request, 'library/book_delete_confirm.html', {'book': book})

def generate_thumbnail(image):
    print('------------Generating thumbnail for:', image.name)
    img = Image.open(image)
    img.thumbnail((200, 200))
    thumb_io = BytesIO()
    img.save(thumb_io, img.format, quality=85)
    thumb_file = InMemoryUploadedFile(thumb_io, None, image.name, 'image/jpeg', thumb_io.getbuffer().nbytes, None)
    return thumb_file

def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            if 'file' in request.FILES:
                book.file = request.FILES['file']
            if 'thumbnail' in request.FILES:
                book.thumbnail = generate_thumbnail(request.FILES['thumbnail'])
            book.save()
            return redirect(reverse('book_list'))
    else:
        form = BookForm()
    context = {'form': form}
    return render(request, 'library/book_upload.html', context)