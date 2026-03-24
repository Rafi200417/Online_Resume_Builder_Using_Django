import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.http import JsonResponse
from .models import Resume, Education, Experience, Project, Skill, Language, Achievement

def register_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        if not User.objects.filter(username=u).exists():
            user = User.objects.create_user(username=u, password=p)
            login(request, user)
            return redirect('home')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login_view')

@login_required(login_url='login_view')
def home(request):
    resume, _ = Resume.objects.get_or_create(user=request.user, title="My Resume")
    return render(request, 'index.html', {'resume': resume})

@login_required(login_url='login_view')
def save_resume(request):
    if request.method == 'POST':
        resume_id = request.POST.get('resume_id')
        resume = get_object_or_404(Resume, id=resume_id, user=request.user)
        
        resume.name = request.POST.get('name', '')
        resume.email = request.POST.get('email', '')
        resume.phone = request.POST.get('phone', '')
        resume.linkedin = request.POST.get('linkedin', '')
        resume.github = request.POST.get('github', '')
        
        template_choice = request.POST.get('template')
        if template_choice:
            resume.template = template_choice
            
        resume.save()

        resume.educations.all().delete()
        for i, (d, c, y) in enumerate(zip(request.POST.getlist('degree'), request.POST.getlist('college'), request.POST.getlist('edu_year'))):
            if d or c: Education.objects.create(resume=resume, degree=d, college=c, year=y, order=i)

        resume.projects.all().delete()
        for i, (p, dr, ds) in enumerate(zip(request.POST.getlist('project'), request.POST.getlist('proj_duration'), request.POST.getlist('proj_desc'))):
            if p: Project.objects.create(resume=resume, title=p, duration=dr, desc=ds, order=i)

        resume.experiences.all().delete()
        for i, (c, p, dr, ds) in enumerate(zip(request.POST.getlist('company'), request.POST.getlist('post'), request.POST.getlist('exp_duration'), request.POST.getlist('exp_desc'))):
            if c: Experience.objects.create(resume=resume, company=c, post=p, duration=dr, desc=ds, order=i)

        resume.skills.all().delete()
        for i, s in enumerate(request.POST.getlist('skills')):
            if s.strip(): Skill.objects.create(resume=resume, name=s, order=i)

        resume.languages.all().delete()
        for i, l in enumerate(request.POST.getlist('languages')):
            if l.strip(): Language.objects.create(resume=resume, name=l, order=i)

        resume.achievements.all().delete()
        for i, a in enumerate(request.POST.getlist('achievement')):
            if a.strip(): Achievement.objects.create(resume=resume, name=a, order=i)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})

@login_required(login_url='login_view')
@xframe_options_sameorigin
def resume_preview(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id, user=request.user)
    context = {
        'name': resume.name,
        'email': resume.email,
        'phone': resume.phone,
        'linkedin': resume.linkedin,
        'github': resume.github,
        'educations': resume.educations.all().order_by('order'),
        'experiences': resume.experiences.all().order_by('order'),
        'projects': resume.projects.all().order_by('order'),
        'skills': [s.name for s in resume.skills.all().order_by('order')],
        'languages': [l.name for l in resume.languages.all().order_by('order')],
        'achievements': [a.name for a in resume.achievements.all().order_by('order')],
    }
    template_name = 'resume.html' if resume.template in ['', 'classic', 'overleaf'] else f'resume_{resume.template}.html'
    return render(request, template_name, context)
