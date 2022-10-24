from multiprocessing import context
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages


from .forms import CreateUserForm 

@login_required(login_url='login:cadastro')
def loggedPage(request): 
    context = {}
    return render(request, 'login\login.html', context)

def logoutUser(request): 
    logout(request)
    return redirect('login:cadastro')

def cadastroPage(request): 
    #TODO 
    # Criar sequência de mensagens apontando erros durante o login
    if not request.user.is_authenticated: 
        form = CreateUserForm();  

        if request.method == 'POST':

            if request.POST.get('realSignUp'): 
                form = CreateUserForm(request.POST)
                #form.clean_email()
                if form.is_valid(): 
                    form.save()
                    messages.success(request, 'Clique no link enviado ao email cadastrado e verifique-o.', extra_tags='sucesso')
                # else: 
                #     messages.error(request, 'Erro na validação dos seus dados pessoais', extra_tags='errozin')
            elif request.POST.get('realSignIn'):
                username = request.POST.get('username')      
                password = request.POST.get('password')      
                user = authenticate(request, username=username, password=password)

                if user is not None: 
                    login(request, user)
                    return redirect('login:login_home')
                else:
                    messages.info(request, 'Senha ou usuário incorretos', extra_tags='inform')
    else: return redirect('login:login_home')

    context = {'form': form}
    return render(request, 'login\cadastro.html', context)