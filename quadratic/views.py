from django.shortcuts import render
from utils import input_parameter, type_parametrs, get_discr
from quadratic.models import Parametr, Solution, TypeParametr

def quadratic_results(request):
    p = Parametr.objects.all()
    p = Parametr(param_a = request.GET['a'], param_b = request.GET['b'], param_c = request.GET['c'])
    p.save()

    a = input_parameter(p.param_a)
    b = input_parameter(p.param_b)
    c = input_parameter(p.param_c)

    t = TypeParametr.objects.all()

    t = TypeParametr(char_a = type_parametrs(a), char_b = type_parametrs(b), char_c = type_parametrs(c))
    t.save()


    d = get_discr(a, b, c)
    s = Solution.objects.all()
    s = Solution(discr = d)



    if type(d) is int:
        if d > 0:
            x1 = (-b + d ** (1/2.0)) / (2*a)
            x2 = (-b - d ** (1/2.0)) / (2*a)
            s = Solution(discr = d, root1 = x1, root2 = x2)
        elif d < 0:
            x = ''
            s = Solution(discr = d)
        elif d==0:
            x = -b / 2.0*a
            s = Solution(discr = d, root1 = x)
    s.save()
    

    return render (request, 'results.html', {'parametr':p, 'solution':s, 'charact':t})
