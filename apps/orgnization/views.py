from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from operation.models import UserAsk
from orgnization.forms import UserAskForm
from orgnization.models import CourceOrg, CityDict
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgView(View):
    def get(self,request):
        #获得所在地区和机构类别
        all_areas = CityDict.objects.all()

        all_category = CourceOrg.objects.all()
        city_id = request.GET.get('city', '')
        if city_id:  # 如果有city id
            all_category = all_category.filter(city_id=int(city_id))

        # 类别筛选
        category = request.GET.get('ct','')
        if category:
            all_category.filter(category=category)

        # 计算机构数量
        all_nums = all_category.count()
        # 排序功能
        hot_orgs = all_category.order_by('-click_nums')[:3]
        # 按学习人数 课程 排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_category.order_by('-students_order')
            elif sort=='cources':
                all_category.order_by('-cources_order')



        #　对课程机构进行分页　　具体在github上面抄
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1


        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_category,5, request=request)# 5是每页显示的数据条数

        orgs = p.page(page) #　这里就不会将所有的category传递进来
        context = {"all_areas": all_areas, 'all_category': orgs,
                   "all_nums": all_nums,
                   'city_id':city_id,
                   'category':category,
                   "hot_orgs":hot_orgs,
                   'sort':sort,
                   }
        return render(request,'org-list.html',context)

class UserAskView(View):
    # def get(self,request):
    #     return render(request,'org-list.html',{})

    def post(self,reqeust):
        ask_form = UserAskForm(reqeust.POST)

        if ask_form.is_valid():
            dict = reqeust.POST
            user = UserAsk()
            user.name = dict.get('name')
            user.mobile = dict.get('mobile')
            user.course_name = dict.get('course_name')

            user.save()

            return JsonResponse({"status":"success"})
        else:
            print('123')
            return JsonResponse({"status":"faild","msg":"添加出错"})

