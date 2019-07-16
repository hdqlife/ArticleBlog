from django.shortcuts import render,HttpResponse
from django.core.paginator import Paginator
from Article.models import *

def index(request):
    first_10 = Article.objects.order_by("-time")[:10] #取前10条
    tui_7 = Article.objects.filter(tui=1).order_by("-time")[:7]  # 取推荐的前7条
    click_12 = Article.objects.order_by("-click")[:12] #取点击最高的前12条
    return render(request, "index.html",locals())

def lists(request,id):
    id = int(id)
    page_number = request.GET.get("page",1) #request.GET django接收get请求参数，get是类字典方法
    types = Type.objects.get(id=id)
    articles = types.article_set.order_by("-time") #外键关系一查询多的查询方式
    p = Paginator(articles,6)
    page = p.page(int(page_number))
    return render(request,"lists.html",locals())

def article(request,id):
    id = int(id)
    article = Article.objects.get(id = id)
    return render(request,"article.html",locals())

def picture(request):
    return render(request,"pictures.html")

# from Article.models import Article,Type
# import datetime
# def addArticle(request):
#     for i in range(200):
#         a = Article()
#         if i%4 == 1:
#             a.title = "背影_%s"%i
#             a.types = Type.objects.get(id = 1)
#             a.desctiption = "这是一篇散文"
#             a.content = "这是一篇散文 这是一篇散文 这是一篇散文\n"*10
#         elif i % 4 == 2:
#             a.title = "诛仙_%s" % i
#             a.types = Type.objects.get(id=2)
#             a.desctiption = "这是一篇小说"
#             a.content = "这是一篇小说 这是一篇小说 这是一篇小说\n" * 10
#         elif i%4 == 3:
#             a.title = "python技术文章_%s" % i
#             a.types = Type.objects.get(id=3)
#             a.desctiption = "这是一篇技术文章"
#             a.content = "这是一篇技术文章 这是一篇技术文章 这是一篇技术文章\n" * 10
#         else:
#             a.title = "日记_%s" % i
#             a.types = Type.objects.get(id=4)
#             a.desctiption = "这是一篇日记"
#             a.content = "这是一篇日记 这是一篇日记 这是一篇日记\n" * 10
#         a.time = datetime.datetime.now()
#         a.picture = "images/QQ图片20190328211750.jpg"
#         a.tui = 0
#         a.click = 0
#         a.save()
#     return HttpResponse("保存成功")
# Create your views here.

from django.http import JsonResponse
def api(request):
    """
    request={
        "code": "formId",
        "msg": {
            "msgtype": "eapp",
            "eapp": {
                "img": "@mediaId",
                "title": "工单已回复",
                "content": "非常感谢",
                "link": "eapp://index/page?param1=1&param2=2"
            }
        }
    }
    response={
        "errcode": 0,
        "errmsg": "ok"
    }
    查询每种类型文章个数的接口
    以ge的形式提交文章的类型
    返回给类型文章的个数
    """
    respone={
        "errorcode":0,
        "errormessage":"",
        "data":""
    }
    if request.method=="GET" and request.GET.get("get_count"):
        id=int(request.GET.get("get_count"))
        types=Type.objects.get(id=int(id))
        obj=len(types.article_set.all())
        respone["errormessage"]="ok"
        respone["data"]={
            "count":obj,
            "name":types.name
        }

    return JsonResponse(respone)