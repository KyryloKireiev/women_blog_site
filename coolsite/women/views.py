from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from women.models import Women, Category
from women.forms import AddNewArticle

MENU = [{"title": "About site", "url_name": "about"},
        {"title": "Add article", "url_name": "add_article"},
        {"title": "Feedback", "url_name": "feedback"},
        {"title": "Sign up", "url_name": "sign_up"},
        {"title": "Sign in", "url_name": "sign_in"}]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()

    context = {"title": "Title page",
               "cats": cats,
               "posts": posts,
               "menu": MENU,
               "cat_selected": 0}

    return render(request, "women/index.html", context=context)


def about(request):
    return render(request, "women/about.html", {"title": "About site",
                                                "menu": MENU})


def post_detail(request, post_id):
    model = Women.objects.get(id=post_id)
    category = Category.objects.get(id=model.cat_id)

    cats = Category.objects.all()

    post = {"category_name": category.name,
            "post_title": model.title,
            "post_detail": model.content,
            "menu": MENU,
            "date": model.time_update,
            "photo": model.photo,
            "cats": cats,
            "cat_selected": category.id}

    return render(request, "women/detail.html", context=post)


def show_category(request, cat_id):
    # return HttpResponse(f"Category id = {cat_id}")
    women = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    context = {"title": "Category",
               "cats": cats,
               "posts": women,
               "menu": MENU,
               "cat_selected": cat_id}

    return render(request, "women/index.html", context=context)


def add_article(request):
    if request.method == 'POST':
        form = AddNewArticle(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNewArticle()

    context = {"menu": MENU,
               "title": "Add new article",
               "form": form}

    return render(request, "women/add_article.html", context=context)


def feedback(request):
    return HttpResponse(f"<h2>Feedback</h2>")


def sign_in(request):
    return HttpResponse(f"<h3>Sign in page</h3>")


def sign_up(request):
    return HttpResponse("<h3>Sign up page</h3>")


def categories(request, cat_id):
    return HttpResponse(f"<h1>Categories page</h1>"
                        f"<p>This is page number {cat_id} </p>")


def archive(request, year):
    if request.GET:
        print(request.GET)
    else:
        print("no get parameters!")

    if int(year) > 2020:
        return redirect("home")
    return HttpResponse(f"<h3>This is archive from {year} year</h3>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h2>NOT exist!</h2>")
