from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
# Create your views here.


def index(request):
    # 查询数据库， 获取目前储存的分类
    # 按点赞次数倒序排列分类
    # 获取前5个分类, 如果分类少于5个, 那就获取全部
    # 把分类列表放入 context_dict 字典
    # 稍后传给模板引擎

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    pages = Page.objects.order_by('views')[:5]
    context_dict['pages'] = pages
    print(pages)

    # 渲染响应, 发给客户端
    return render(request, 'rango/index.html', context_dict)


def show_category(request, category_name_slug):
    # 创建上下文字典 稍后传给模板渲染引擎
    context_dict = {}

    try:
        # 能通过传入的分类别名找到对应的分类吗？
        # 如果找不到 .get()方法抛出 DoseNotExist 异常
        # 因此 .get()方法返回一个模型的实例或抛出异常
        category = Category.objects.get(slug=category_name_slug)

        # 检索关联的所有网页
        # 注意, filter() 返回一个网页对象列表或空列表
        pages = Page.objects.filter(category=category)

        #把得到的列表赋值给模板上下文中名为 pages 的键
        context_dict['pages'] = pages
        #也把从数据库中获取的category对象添加到上下文字典中
        # 我们将在模板中通过这个变量确认分类是否存在
        context_dict['category'] = category
    except Category.DoesNotExist:
        # 没找到指定的分类时执行这里
        # 什么也不做
        # 模板会显示消息, 指明分类不存在
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context_dict)


def add(request):
    form = CategoryForm()
    # 是 HTTP POST 请求吗?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        #表单数据有效吗?
        if form.is_valid():
            # 把新分类存入数据库
            form.save(commit=True)
            # 保存新分类后可以显示一个确认消息
            # 不过既然最受欢迎的分类在首页
            # 那就把用户带到首页吧
            return index(request)
        else:
            # 表单数据有错误
            # 直接在终端打印出来
            print(form.errors)
    # 出来有效数据和无效数据之后
    # 渲染表单 并显示可能出现的错误消息
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form =PageForm()
    if request.method == "POST":
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    content_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', content_dict)