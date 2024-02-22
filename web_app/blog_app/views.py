from django.shortcuts import render

# some data 
posts = [
    {
        'title':'Spatial data',
        'author':'collins kech',
        'content':'spatial data can nolonger be ignored',
        'date':'2020-07-29',
    },
    {
        'title':'adopt gis',
        'author':'mike eplips',
        'content':'Each business shal use gis in the future',
        'date':'2022-01-15',
    },
    {
        'title':'migrate to Arc GIS Pro',
        'author':'Joyce mandi',
        'content':'Arc Pro has more features and capabilities',
        'date':'2022-12-31',
    }
]


def home(request):
    # grab data into a dictionary
    context = {
        'posts':posts
    }
    return render(request, 'blog_app/home.html', context)


def about(request):
    return render(request, 'blog_app/about.html', {'title':'About Page'})
