from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



def credit(mo):
    if mo >= 90:
        return 10
    elif mo >= 80 and mo < 90:
        return 9
    elif mo >= 70 and mo < 80:
        return 8
    elif mo >= 60 and mo < 70:
        return 7
    elif mo >= 50 and mo < 60:
        return 6
    elif mo >= 40 and mo < 50:
        return 5
    elif mo >= 30 and mo < 40:
        return 4
    elif mo >= 20 and mo < 30:
        return 3
    elif mo >= 10 and mo < 20:
        return 2
    else:
        return 1

def calculate(request):
    math = int(request.POST['math'])
    m1 = credit(math) * 3
    dsa =  int(request.POST['math'])
    m2 = credit(dsa) * 4
    ade =  int(request.POST['math'])
    m3 = credit(ade) * 3
    co =  int(request.POST['math'])
    m4 = credit(co) * 3
    se =  int(request.POST['math'])
    m5 = credit(se) * 3
    dms =  int(request.POST['math'])
    m6 = credit(dms) * 3
    adel =  int(request.POST['math'])
    m7 = credit(adel) * 2
    dsal =  int(request.POST['math'])
    m8 = credit(dsal) * 2
    cip =  int(request.POST['math'])
    m9 = credit(cip) * 1

    summ = math + dsa + ade + co + se + dms + adel + dsal + cip

    credit_score = 24
    sub_t_c = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9

    cgpa = (sub_t_c / credit_score)

    params = {'s1': math, 's2': dsa, 's3': ade, 's4': co, 's5': se, 's6': dms, 's7': adel, 's8': dsal, 's9': cip, 'res': 'TOTAL: {}'.format(summ), 'cg': 'CGPA: {}'.format(cgpa)}


    return render(request, 'result.html', params)

