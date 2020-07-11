
from django.http import HttpResponse
from django.shortcuts import render


def about_us(request):
    aboutus={'name':'aboutus'}
    return render(request,'aboutus.html',aboutus)

def contact_us(request):
    contactus={'name':'contactus'}
    return render(request,'contactus.html',contactus)

def templates_new(request):
    temporary_var={'name':'rebel','place':'unknown'}
    return render(request,'index.html',temporary_var)

def remove_punctuations(text):
    punctuations = '''<>’*\():,{}—“”''!.-?;/[]'''
    final_text = ""
    for char in text:
        if char not in punctuations:
            final_text += char
    return final_text

def capital_first_letter(text):
    final_text = ''
    i = 0
    for char in text:
        final_text += char.upper()
        break
    for char in text:
        if i == 0:
            i += 1
        else:
            final_text += char
            i += 1
    return final_text

def capital_all_letters(text):
    final_text=text.upper()
    return final_text

def remove_space(text):
    final_text=''
    for i in text:
        if i !=' ':
            final_text+=i
    return final_text

def call_func(number,text):
    check_func = [remove_punctuations(text), capital_first_letter(text), capital_all_letters(text),remove_space(text)]
    final_text=check_func[number]
    return final_text

def analyse(request):
    global djtext
    djtext= request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    capital_first = request.POST.get('capital_first', 'off')
    capital_all= request.POST.get('capital_all','off')
    removespace=request.POST.get('removespace','off')
    check_request=[removepunc,capital_first,capital_all,removespace]
    checkbox_check=0
    for j,k in enumerate(check_request):
        if k=='on':
            checkbox_check+=1
            djtext= call_func(j,djtext)

    analysed=djtext

    if checkbox_check == 0:
        params = {'purpose': '', 'analysed_text': analysed}
        return render(request, 'analyse.html', params)
    else:
        purposes=[' Remove Punctuation',' Capitalize First Letter',' Capitalize All Letters',' Remove Space']
        purpose_assign=''
        count=0
        for i,j in enumerate(check_request):
            if j=='on':
               count+=1
               if count>1:
                   purpose_assign+=','
               purpose_assign+=purposes[i]
        params = {'purpose': purpose_assign , 'analysed_text': analysed}
        return render(request, 'analyse.html', params)




