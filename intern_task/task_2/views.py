from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Heirarchy
from anytree import Node, RenderTree


# Create your views here.

@login_required()
def hierarchy(request):
    root = Node("root")
    d = {}
    obj = Heirarchy.objects.all().order_by('sid')
    lst = []

    def findNode(parentId):
        return d[parentId]

    def findSpacefromKey(id):
        s = Heirarchy.objects.get(sid=id)
        for i in lst:
            if i['name'] == s.title:
                return range(0,list(i['spaces'])[len(i['spaces']) - 1] + 2)

    def findKey(node):
        for i in d:
            if d[i] == node:
                s =  Heirarchy.objects.get(sid = i)
                if s.parentId is None:
                    return range(1)
                else:
                    return findSpacefromKey(s.parentId)

    print(obj)
    for i in obj:
        if i.parentId is None:
            d[i.sid] = Node(i.title, parent=root)
        else:
            d[i.sid] = Node(i.title, parent=findNode(i.parentId))
    for pre, fill, node in RenderTree(root):
        data ={}
        print("%s%s" % (pre, node.name))
        if(node.name != 'root'):

            data["name"] = node.name
            data['spaces'] = findKey(node)
            lst.append(data)
    print(lst)
    return render(request, 'task_2/hierarchy.html', {'lst' : lst})
