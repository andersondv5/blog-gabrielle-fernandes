from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    outros_posts = Post.objects.exclude(id=post.id).order_by('-data')[:3]  # Exclui o post atual e pega 3 últimos
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'outros_posts': outros_posts,
    })


def post_list(request):
    posts = Post.objects.order_by('-data')
    return render(request, 'posts/post_list.html', {'posts': posts})



def admin_panel(request):
    posts = Post.objects.order_by('-data')
    
    # Se for editar, traz o post específico
    post_id = request.GET.get('edit')
    post_to_edit = None
    if post_id:
        post_to_edit = get_object_or_404(Post, id=post_id)
    
    if request.method == 'POST':
        # Ação delete
        if 'delete' in request.POST:
            delete_id = request.POST.get('delete')
            post_del = get_object_or_404(Post, id=delete_id)
            post_del.delete()
            return redirect('admin_panel')
        
        # Criar ou editar
        if post_to_edit:
            form = PostForm(request.POST, instance=post_to_edit)
        else:
            form = PostForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = PostForm(instance=post_to_edit)
    
    return render(request, 'posts/admin_panel.html', {
        'posts': posts,
        'form': form,
        'edit_post': post_to_edit,
    })
