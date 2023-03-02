from django.shortcuts import render
from django.shortcuts import render
from user_auth.models import User


# def all_views_navbar_utils(request):
#     wish_op = digits.convert_to_fa(0)
#     login = False

#     same_context = {
#         'wish': wish_op,
#         'login': login,
#         'scategory': SupCategory.objects.all(),
#     }

#     if request.user.is_authenticated:
#         login = True
#         if wishlist.objects.filter(buyer=request.user).filter(paid=False).exists():
#             wish_op = wishlist.objects.filter(buyer=request.user).filter(paid=False).__len__()
#         else:
#             wish_op = 0
#         same_context['login'] = login
#         wish_op = digits.convert_to_fa(wish_op)
#         same_context['wish'] = wish_op

#         if request.user.owner:
#             owner = True
#             me = User.objects.get(mobile=request.user.mobile)
#             my_shop = me.shop
#             same_context['my_shop'] = my_shop
#             same_context['owner'] = owner

#     return same_context


def document_view(request):
    # context = all_views_navbar_utils(request)
    context = {}
    return render(request, 'document/docs.html', context)
