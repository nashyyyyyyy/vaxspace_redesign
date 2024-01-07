from django.shortcuts import render, redirect, get_object_or_404
from contextlib import redirect_stderr
from http.client import HTTPResponse
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from vaxapp import views
from django.contrib.auth.models import Group
from datetime import datetime, date, timedelta, time
from django.utils.timezone import localdate
from django.utils import timezone
import pytz
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.db.models import Count
import matplotlib.pyplot as plt
import base64
import io
import urllib
import plotly.graph_objs as go
import json
from django.db.models import Q
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.groups.filter(name='admin').exists():
                login(request, user)
                return redirect('index/')

            elif user.groups.filter(name='healthworker').exists():
                login(request, user)
                return redirect('healthworker/')

            elif user.groups.filter(name='guardian').exists():
                login(request, user)
                return redirect('guardian/')

        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('/')
                

    return render(request, 'vaxapp/login.html')

@login_required
def update_healthworker(request):
    user = request.user

    if request.method == 'POST':
        # Update user profile if form is submitted
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.email = request.POST.get('email')
        # Update other user fields similarly
        
        user.save()
        messages.success(request, 'Updated successfully')
        return redirect('/healthworker/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/healthworker/') 
    return render(request, 'healthworker.html', {'user': user})

@login_required
def update_admin(request):
    user = request.user

    if request.method == 'POST':
        # Update user profile if form is submitted
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.email = request.POST.get('email')
        # Update other user fields similarly
        
        user.save()
        messages.success(request, 'Admin updated successfully')
        return redirect('/index/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/index/') 
    return render(request, 'index.html', {'user': user})

def edit_guardian(request, id):
    guardian = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        guardian.first_name = request.POST.get('first_name')
        guardian.last_name = request.POST.get('last_name')
        guardian.username = request.POST.get('username')
        guardian.email = request.POST.get('email')
        guardian.is_active = request.POST.get('is_active')
        # Update other guardian fields similarly
        
        guardian.save()
        messages.success(request, 'User updated successfully')
        return redirect('/admin_tables/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/admin_tables/') 

def edit_healthworker(request, id):
    healthworker = get_object_or_404(User, id=id)
    
    if request.method == 'POST':
        healthworker.first_name = request.POST.get('first_name')
        healthworker.last_name = request.POST.get('last_name')
        healthworker.username = request.POST.get('username')
        healthworker.email = request.POST.get('email')
        healthworker.is_active = request.POST.get('is_active')
        # Update other guardian fields similarly
        
        healthworker.save()
        messages.success(request, 'Healthworker updated successfully')
        return redirect('/admin_tables/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/admin_tables/') 

def edit_vaccine(request, id):
    vaccine = get_object_or_404(Vaccine, id=id)
    
    if request.method == 'POST':
        vaccine.name = request.POST.get('name')
        vaccine.description = request.POST.get('description')
        vaccine.dose1 = request.POST.get('chk1')
        vaccine.dose2 = request.POST.get('chk2')
        vaccine.dose3 = request.POST.get('chk3')
        vaccine.recommended_age1 = request.POST.get('recommended_age1')
        vaccine.recommended_age2 = request.POST.get('recommended_age2')
        vaccine.recommended_age3 = request.POST.get('recommended_age3')
        if not vaccine.recommended_age1:
            vaccine.recommended_age1 = None
        if not vaccine.recommended_age2:
            vaccine.recommended_age2 = None
        if not vaccine.recommended_age3:
            vaccine.recommended_age3 = None

            vaccine.save()
            messages.success(request, 'Vaccine updated successfully')
            return redirect('/admin_tables/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/admin_tables/') 

def edit_barangay(request, id):
    if id:
        barangay = get_object_or_404(Barangay, id=id)
        
        if request.method == 'POST':
            healthworker_username = request.POST.get('healthworker')
            if healthworker_username:
                try:
                    assign_healthworker = User.objects.get(username=healthworker_username)
                    barangay.healthworker = assign_healthworker
                    barangay.save()
                    messages.success(request, 'Updated successfully')
                except User.DoesNotExist:
                    messages.error(request, 'User does not exist')
            else:
                # Set healthworker_id to NULL
                barangay.healthworker = None
                barangay.save()
                messages.success(request, 'Healthworker cleared successfully')
        else:
            messages.error(request, 'Invalid request method')

    else:
        messages.error(request, 'Empty ID received.')
    
    return redirect('/admin_tables/')

@login_required
def update_guardian(request):
    user = request.user

    if request.method == 'POST':
        # Update user profile if form is submitted
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.email = request.POST.get('email')
        # Update other user fields similarly
        
        user.save()
        messages.success(request, 'Updated successfully')
        return redirect('/guardian/')  # Replace with your success URL
    else:
        messages.error(request, 'Error updating.')
        return redirect('/guardian/') 
    return render(request, 'guardian.html', {'user': user})

@allowed_users(allowed_roles=['admin', 'healthworker'])
@admin_only
def index(request):
    vaccine = Vaccine.objects.all()
    vax_count = vaccine.count()
    regs = Admin_record.objects.all()
    regs_count = regs.count()
    guardian = User.objects.filter(groups=3)
    user_count = guardian.count()
    healthworker = User.objects.filter(groups=2)
    worker_count = healthworker.count()
    barangay = Barangay.objects.all()
    bar_count = barangay.count()
    
    vaccine_types = [vaccine.name for vaccine in vaccine]
    
    vaccinated_records = Vaccine_record.objects.filter(remarks__icontains='Vaccinated')
    non_vaccinated_records = Vaccine_record.objects.exclude(remarks__icontains='Vaccinated')
    vaccinated_counts = [0] * len(vaccine_types)
    non_vaccinated_counts = [0] * len(vaccine_types)

    for record in vaccinated_records:
        # Get vaccine IDs from the record (assuming 'vax1', 'vax2', 'vax3' are fields in Vaccine_record)
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):  # Check if the ID exists and is an integer
                # Fetch corresponding Vaccine record and get the vaccine name
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    vaccinated_counts[index] += 1

    for record in non_vaccinated_records:
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):  # Check if the ID exists and is an integer
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    non_vaccinated_counts[index] += 1

    context = {
        'vax_count':vax_count,
        'vaccine':vaccine,
        'regs': regs,
        'regs_count': regs_count,
        'user_count': user_count,
        'worker_count': worker_count,
        'bar_count': bar_count,
        'brgy': barangay,
        'vaccine_types': vaccine_types,
        'vaccinated_counts': vaccinated_counts,
        'non_vaccinated_counts': non_vaccinated_counts,
    }
    if request.method == 'POST':
        
                child_name = request.POST.get('child_name')
                date_of_birth = request.POST.get('date_of_birth')
                place_of_birth = request.POST.get('place_of_birth')
                address = request.POST.get('address')
                contact = request.POST.get('contact')
                mother_name = request.POST.get('mother_name')
                father_name = request.POST.get('father_name')
                birth_height = request.POST.get('birth_height')
                birth_weight = request.POST.get('birth_weight')
                sex = request.POST.get('sex')
                added_by = request.user

                if Register.objects.filter(child_name = child_name).exists():
                    messages.error(request, 'Already registered.')
                    return redirect('index/..')
                else:
                    address_instance = Barangay.objects.get(name=address)
                    registered = Register(child_name=child_name,date_of_birth=date_of_birth, place_of_birth=place_of_birth, mother_name=mother_name,father_name=father_name,address=address_instance,contact=contact,birth_height=birth_height, birth_weight=birth_weight, sex=sex, added_by=added_by)
                    registered.save()
                    messages.success(request, "Registered successfully.")
                    return redirect('index/..')

    return render(request, 'vaxapp/index.html', context)


def add_vaccine(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        created = datetime.now()
        dose1 = request.POST.get('chk1')
        dose2 = request.POST.get('chk2')
        dose3 = request.POST.get('chk3')
        recommended_age1 = request.POST.get('recommended_age1')
        recommended_age2 = request.POST.get('recommended_age2')
        recommended_age3 = request.POST.get('recommended_age3')


        if Vaccine.objects.filter(name = name).exists():
            messages.error(request, 'Already registered.')
            return redirect('index/..')
        else:
            added = Vaccine(name=name, description=description, created=created, dose1= dose1, dose2= dose2, dose3= dose3,recommended_age1=recommended_age1,recommended_age2=recommended_age2,recommended_age3=recommended_age3)
            added.save()
            messages.success(request, "Registered successfully.")
            return redirect('index/..')
    return render(request, 'vaxapp/add_vaccine.html')


@allowed_users(allowed_roles=['healthworker'])
def healthworker(request):
    assign = Barangay.objects.get(healthworker=request.user)
    records = Register.objects.filter(address=assign)
    vax_sched = Schedule.objects.filter(brgy=assign)
    vaccine = Vaccine.objects.all()
    vax_count = vaccine.count()
    records_count = records.count()
    guardian = User.objects.filter(groups=3)
    user_address = User_info.objects.filter(address=assign.name)
    user_count = user_address.count()
    sched_count = vax_sched.count()
    
    vaccine_types = [vaccine.name for vaccine in vaccine]
    
    # Filtering vaccinated records
    vaccinated_records = Vaccine_record.objects.filter(
        remarks__icontains='Vaccinated',
        brgy=assign
    )

    # Filtering non-vaccinated records
    non_vaccinated_records = Vaccine_record.objects.filter(
        ~Q(remarks__icontains='Vaccinated'),
        brgy=assign
    )

    # Filtering records by specific address separately
    
    
    vaccinated_counts = [0] * len(vaccine_types)
    non_vaccinated_counts = [0] * len(vaccine_types)

    for record in vaccinated_records:
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    vaccinated_counts[index] += 1

    for record in non_vaccinated_records:
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    non_vaccinated_counts[index] += 1
    context = {
        'assign': assign,
        'records': records,
        'vax_sched': vax_sched,
        'guardian':guardian,
        'vax_count':vax_count,
        'vaccine':vaccine,
        'records_count': records_count,
        'user_count': user_count,
        'sched_count': sched_count,
        'vaccine_types': vaccine_types,
        'vaccinated_counts': vaccinated_counts,
        'non_vaccinated_counts': non_vaccinated_counts,
    }
    if request.method == 'POST':
        
                child_name = request.POST.get('child_name')
                date_of_birth = request.POST.get('date_of_birth')
                place_of_birth = request.POST.get('place_of_birth')
                address = request.POST.get('address')
                contact = request.POST.get('contact')
                mother_name = request.POST.get('mother_name')
                father_name = request.POST.get('father_name')
                birth_height = request.POST.get('birth_height')
                birth_weight = request.POST.get('birth_weight')
                sex = request.POST.get('sex')
                added_by = request.POST.get('added_by')

                if Register.objects.filter(child_name = child_name).exists():
                    messages.error(request, 'Already registered.')
                    return redirect('index/..')
                else:
                    assign_instance = User.objects.get(id=added_by)
                    address_instance = Barangay.objects.get(name=address)
                    registered = Register(child_name=child_name,date_of_birth=date_of_birth, place_of_birth=place_of_birth, mother_name=mother_name,father_name=father_name,address=address_instance,contact=contact,birth_height=birth_height, birth_weight=birth_weight, sex=sex, added_by=assign_instance)
                    registered.save()
                    messages.success(request, "Registered successfully.")
                    return redirect('healthworker/..')

    return render(request, 'vaxapp/healthworker.html', context)



def add_healthworker(request):
    form = CreateUserForm()
    brgy = Barangay.objects.all()
    context = {
        'form':form,
        'brgy':brgy
        }

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():

            user = form.save()
            
            group = Group.objects.get(name='healthworker')
            user.groups.add(group)
            messages.success(request, "Account created successfully.")
            return redirect('index/..')
        else:
             return render(request, 'vaxapp/register.html', {'form': form, 'brgy': brgy})
    
    
    return render(request, 'vaxapp/add_healthworker.html', context)

def user_register(request):
    form = CreateUserForm()
    user_infos = User_info.objects.all()
    brgy = Barangay.objects.all()
    context = {
        'form': form,
        'brgy':brgy,
        'user_infos': user_infos
    }

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            # Save User model data
            user = form.save()
            
            # Save User_info model data
            role = request.POST.get('role')  # Get the role from the form
            address = request.POST.get('address')  # Get the address from the form
            contact = request.POST.get('contact')  # Get the contact from the form

            user_info = User_info.objects.create(
                user=user,
                role=role,
                address=address,
                contact=contact
                # Add other fields as required
            )

            # Adding user to group 'guardian'
            group = Group.objects.get(name='guardian')
            user.groups.add(group)

            messages.success(request, "Account created successfully.")
            return redirect('/')
        else:
            # Form is not valid, render form with errors
            return render(request, 'vaxapp/register.html', {'form': form})
    
    return render(request, 'vaxapp/register.html', context)

@login_required(login_url='/')
def guardian(request):
        brgy = Barangay.objects.all()
        profile = request.user
        user_info = User_info.objects.get(user=profile)
        children = Register.objects.filter(added_by=profile)
        children_count = children.count()
        specific_group = Group.objects.filter(user=profile, name='guardian').first()
        ph_tz = pytz.timezone('Asia/Manila')
        due_today = timezone.now().astimezone(ph_tz).date()
        try:
            child_sched = Schedule.objects.filter(guardian=profile)
            child_count = child_sched.count()

        except Schedule.DoesNotExist:
            child_sched = None

           
        context = {
            'brgy':brgy,
            'profile':profile,
            'user_info':user_info,
            'children':children,
            'children_count':children_count,
            'specific_group':specific_group,
            'child_sched':child_sched,
            'child_count': child_count,
            'due_today': due_today
        }
        if request.method == 'POST':
        
                child_name = request.POST.get('child_name')
                date_of_birth = request.POST.get('date_of_birth')
                place_of_birth = request.POST.get('place_of_birth')
                address = request.POST.get('address')
                contact = request.POST.get('contact')
                mother_name = request.POST.get('mother_name')
                father_name = request.POST.get('father_name')
                birth_height = request.POST.get('birth_height')
                birth_weight = request.POST.get('birth_weight')
                sex = request.POST.get('sex')
                added_by = request.user

                if Register.objects.filter(child_name = child_name).exists():
                    messages.error(request, 'Already registered.')
                    return redirect('guardian/..')
                else:
                    address_instance = Barangay.objects.get(name=address)
                    registered = Register(child_name=child_name,date_of_birth=date_of_birth, place_of_birth=place_of_birth, mother_name=mother_name,father_name=father_name,address=address_instance,contact=contact,birth_height=birth_height, birth_weight=birth_weight, sex=sex, added_by=added_by)
                    registered.save()
                    messages.success(request, "Registered successfully.")
                    return redirect('guardian/..')

        return render(request, 'vaxapp/guardian.html', context)



def barangay(request):
    assign_brgy = User.objects.filter(groups=2)
    brgy_data = Barangay.objects.all()
    context = {
        'assign_brgy': assign_brgy,
        'brgy_data': brgy_data,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        healthworker = request.POST.get('healthworker')

        if Barangay.objects.filter(name=name).exists():
            messages.error(request, 'Already added.')
            return redirect('barangay/..')
        else:
            healthworker_instance = User.objects.get(first_name=healthworker)
            added_brgy = Barangay(name=name, healthworker = healthworker_instance)
            added_brgy.save()
            messages.success(request, "Added successfully.")
            return redirect('barangay/..')

    return render(request, 'vaxapp/barangay.html', context)

def charts(request):

    return render(request, 'vaxapp/charts.html')

def admin_tables(request):
    admin_records = Admin_record.objects.all()
    child_record = Vaccine_record.objects.all()
    admin_true = User.objects.filter(is_superuser=True)
    healthworker_list = User.objects.filter(groups=2)
    guardian = User.objects.filter(groups=3)
    barangay_list = Barangay.objects.all()
    vaccine_list = Vaccine.objects.all()

    
    context = {
        'child_record':child_record,
        'admin_records': admin_records,
        'admin_true': admin_true,
        'healthworker_list':healthworker_list,
        'guardian': guardian,
        'barangay_list':barangay_list,
        'vaccine_list': vaccine_list
    }
    return render (request,'vaxapp/admin_tables.html', context)

def tables(request):
    assign = Barangay.objects.get(healthworker=request.user)
    records = Register.objects.filter(address=assign)
    vax_sched = Schedule.objects.filter(brgy=assign)
    
    ph_tz = pytz.timezone('Asia/Manila')
    due_today = timezone.now().astimezone(ph_tz).date()

    def calculate_days_old(birth_date):
        today = date.today()
        delta = today - birth_date
        days_old = delta.days

        if days_old < 1:
            return "Less than a day old"
        elif days_old == 1:
            return f"{days_old} day old"
        else:
            return f"{days_old} days old"

    for record in records:
        record.days_old = calculate_days_old(record.date_of_birth)
        if record.days_old != "Less than a day old":
            days_old = int(record.days_old.split()[0])  # Extract the integer value
            age_range = range(days_old - 4, days_old + 2)  # Creating a range around the days_old value
            
            vaccine_doses = (
                Vaccine.objects.filter(recommended_age1__in=age_range) |
                Vaccine.objects.filter(recommended_age2__in=age_range) |
                Vaccine.objects.filter(recommended_age3__in=age_range)
            )
            
            # Use vaccine_doses as needed for each record
            record.vaccine_doses = vaccine_doses
        else:
            record.vaccine_doses = "Less than a day old"
    context = {
        'records': records,
        'assign': assign,
        'vax_sched': vax_sched,
        'due_today': due_today,

    }
    return render(request, 'vaxapp/tables.html', context)
def edit_schedule(request, id):
    schedule = get_object_or_404(Schedule, id=id)
    if request.method == 'POST':
        vax_date = request.POST.get('update_sched')
        schedule.vax_date = vax_date
        schedule.save()
        messages.success(request, "Updated successfully.")
    return redirect('/tables/')

#### MAIN FEATURE
def vax_recommendation(age_in_days):
    age_range = range(age_in_days - 4, age_in_days + 2)
    vaccine_doses = (
        Vaccine.objects.filter(recommended_age1__in=age_range) |
        Vaccine.objects.filter(recommended_age2__in=age_range) |
        Vaccine.objects.filter(recommended_age3__in=age_range)
    )

    return vaccine_doses


def add_record(request, id):
    added = Register.objects.get(id=id)

    

    try:
        register_instance = Register.objects.get(id=id)
    except Register.DoesNotExist:
        register_instance = None

    age_category = None
    vaccine_doses = None

    if register_instance and register_instance.date_of_birth:
        today = datetime.now().date()
        dob = register_instance.date_of_birth
        age = today - dob

        # Calculate age in days
        age_in_days = age.days

        if age_in_days < 1:
            age_category = "Less than a day old"
        elif age_in_days < 30:
            age_category = f"{age_in_days} days old"
        else:
            age_category = f"{int(age_in_days / 30.4)} month(s) old / {(age_in_days)} days old"

        vaccine_doses = vax_recommendation(age_in_days)
        
    context = {
        'added': added,
        'age_category': age_category,
        'vaccine_doses': vaccine_doses,
        'age':age,
        
    }
    
    if request.method == 'POST':
        
        child_id = request.POST.get('child_id')
        vax_ids = request.POST.getlist('vax_ids[]')
        brgy_id = request.POST.get('brgy_id')
        guardian_id =request.POST.get('guardian_id')
        date_of_birth =request.POST.get('dob')
        created = datetime.now()
        dose1 = request.POST.get('dose1')
        dose2 = request.POST.get('dose2')
        dose3 = request.POST.get('dose3')
        
        vax1, vax2, vax3 = [None] * 3
        for i, vax_id in enumerate(vax_ids):
            if i == 0:
                vax1 = vax_id
            elif i == 1:
                vax2 = vax_id
            elif i == 2:
                vax3 = vax_id
        if Schedule.objects.filter(child = id).exists():
            messages.error(request, 'Already added.')
            return redirect('tables/..')

        else:
            register_id = Register.objects.get(id=child_id)
            barangay_id = Barangay.objects.get(name=brgy_id)
            guardian_id = User.objects.get(pk = guardian_id)
            
            vax1_info = ""
            vax2_info = ""
            vax3_info = ""

            for vaccine in vaccine_doses:
                vax_info = f"{vaccine.name} : "
                
                if age.days <= int(vaccine.recommended_age1) + 5:
                    if vaccine.dose1:
                        vax_info += "First dose"
                elif age.days <= int(vaccine.recommended_age2) + 5:
                    if vaccine.dose2:
                        vax_info += "Second dose"
                    elif not vaccine.dose2 and vaccine.dose1:
                        vax_info += "First dose"
                elif age.days <= int(vaccine.recommended_age3) + 5:
                    if vaccine.dose3:
                        vax_info += "Third dose"
                    elif not vaccine.dose3 and vaccine.dose1:
                        vax_info += "First dose"
                
                if vax_info.endswith(': '):  # Check if no doses were added
                    continue  # Skip if no doses were added
                
                # Assign to respective vax_info fields
                if not vax1_info:
                    vax1_info = f" •[{vax_info}] \n "
                elif not vax2_info:
                    vax2_info = f" •[{vax_info}] \n "
                elif not vax3_info:
                    vax3_info = f" •[{vax_info}] \n "
                else:
                    break  # Exit loop if all three vax_info fields are filled

# Remaining code to set up the date and save to the database...





            # Get the current date
            today = datetime.now().date()
            
            # Find the next Wednesday
            days_until_wednesday = (2 - today.weekday() + 7) % 7
            next_wednesday = today + timedelta(days=days_until_wednesday)
            
            # Set the vaccination date to the next Wednesday morning
            vaccination_date = datetime.combine(next_wednesday, time(hour=8, minute=0))
            vaccination_date_with_timezone = timezone.make_aware(vaccination_date)
            save_date = Schedule(child=register_id,vax2=vax2,vax2_info=vax2_info,vax1=vax1,vax1_info=vax1_info,vax3=vax3,vax3_info=vax3_info,vax_date=vaccination_date_with_timezone,date_of_birth=date_of_birth, brgy=barangay_id, guardian=guardian_id, created=created)
            save_date.save()
            messages.success(request, "Added successfully.")
            return redirect('/../../tables/')

    return render(request, 'vaxapp/add_to_schedule.html', context)
    
####END MAIN FEATURE
def view_record_staff(request, id):
    if request.user.is_superuser:
        try:
            view_id = Admin_record.objects.get(id=id)
            vax_info = Vaccine_record.objects.filter(child=view_id.child_id)
        except Vaccine_record.DoesNotExist:
            vax_info = None
    else:
        try:
            view_id = Register.objects.get(id=id)
            vax_info = Vaccine_record.objects.filter(child=id)
        except Vaccine_record.DoesNotExist:
            vax_info = None
    context = {
        'view_id':view_id,
        'vax_info':vax_info
    }
    return render(request, 'vaxapp/view_record_staff.html',context)

def view_record(request, id):
    try:
        view_id = Register.objects.get(id=id)
        vax_info = Vaccine_record.objects.filter(child=id)
    except Vaccine_record.DoesNotExist:
        vax_info = None
    
    context = {
        'view_id':view_id,
        'vax_info':vax_info
    }
    return render(request, 'vaxapp/view_record.html',context)


def confirmation(request,id):
    confirm = Schedule.objects.get(id=id)
    
    
    context = {
        'confirm':confirm,
    
    }

    if request.method == 'POST':
        child_id = request.POST.get('child_id')
        brgy = request.POST.get('brgy')
        birthheight = request.POST.get('birthheight')
        birthweight = request.POST.get('birthweight')
        vax1 = request.POST.get('vax1')
        vax1_info = request.POST.get('vax1_info')
        vax2 = request.POST.get('vax2')
        vax2_info = request.POST.get('vax2_info')
        vax3 = request.POST.get('vax3')
        vax3_info = request.POST.get('vax3_info')
        vaxdate = datetime.now()
        date_of_birth = request.POST.get('dob')
        b_height = request.POST.get('b_height')
        b_weight = request.POST.get('b_weight')
        vaccinator = request.POST.get('vaccinator')
        remarks = request.POST.get('remarks')
        
        vax1 = int(vax1) if vax1 and vax1.isdigit() else 0
        vax2 = int(vax2) if vax2 and vax2.isdigit() else 0
        vax3 = int(vax3) if vax3 and vax3.isdigit() else 0
        # Retrieve the Register instance for the given child_id
        register_instance = Register.objects.get(id=child_id)
        brgy_instance = Barangay.objects.get(id=brgy)
        # Update birth height and weight for the register instance
        register_instance.birth_height = b_height
        register_instance.birth_weight = b_weight
        register_instance.save()

        # Create the combined vaccination info string
        
        
        # Create and save a new instance of Vaccine_record
        vax_record = Vaccine_record(child=register_instance,brgy=brgy_instance, vax1=vax1,vax1_info=vax1_info,vax2=vax2,vax2_info=vax2_info,vax3=vax3,vax3_info=vax3_info, vaccination_date=vaxdate,date_of_birth=date_of_birth,prev_birth_height=birthheight, prev_birth_weight=birthweight,vaccinator=vaccinator, remarks=remarks)
        vax_record.save()

        try:
            schedule_to_delete = Schedule.objects.get(id=id)
            schedule_to_delete.delete()
        except Schedule.DoesNotExist:
            pass  # Handle the case where the Schedule does not exist

        messages.success(request, "Confirmed")
        return redirect('tables/../../..')  # Replace 'confirmation/..' with your actual URL

    return render(request, 'vaxapp/confirmation.html', context)
from .models import Admin_record, Vaccine_record

def save_to_admin(request):
    if request.method == 'POST':
        # Retrieve data from POST request
        child_record_id = request.POST.get('child_record')  # Assuming this is the ID of Vaccine_record
        child_id = request.POST.get('child_id')
        child_name = request.POST.get('child_name')
        date_of_birth = request.POST.get('date_of_birth')
        place_of_birth = request.POST.get('place_of_birth')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        mother_name = request.POST.get('mother_name')
        father_name = request.POST.get('father_name')
        birth_height = request.POST.get('birth_height')
        birth_weight = request.POST.get('birth_weight')
        sex = request.POST.get('sex')
    
        try:
            # Retrieve the Vaccine_record instance using the provided ID
            vaccine_record = Vaccine_record.objects.get(id=child_record_id)
            if Admin_record.objects.filter(child_record=vaccine_record).exists():
                if request.user.is_superuser:
                    messages.error(request, "Already saved")
                    return redirect(f'/view_record_staff/{child_id}/')
                else:
                    messages.error(request, "Already submitted")
                    return redirect(f'/view_record_staff/{child_id}/')
            child_address = Barangay.objects.get(name=address)
            # Create an Admin_record instance and save it
            saved_to_admin = Admin_record(
                child_record=vaccine_record,
                child_id=child_id,
                child_name=child_name,
                date_of_birth=date_of_birth,
                place_of_birth=place_of_birth,
                address=address,
                contact=contact,
                mother_name=mother_name,
                father_name=father_name,
                birth_height=birth_height,
                birth_weight=birth_weight,
                sex=sex
            )
            saved_to_admin.save()
            
            messages.success(request, "Submitted successfully")
            return redirect(f'/view_record_staff/{child_id}/')
        
        except Vaccine_record.DoesNotExist:
            # Handle if the Vaccine_record with provided ID doesn't exist
            messages.error(request, "Vaccine record does not exist")
            return redirect(f'/view_record_staff/{child_id}/')

    return redirect('/view_record_staff/')


def blank(request):

    return render(request, 'vaxapp/blank.html')

def remove_child(request, id):
        if Register.objects.filter(id=id).exists():
                remove_model1 = get_object_or_404(Register, id=id)
                remove_model1.delete()
        else:
            pass

    # Redirect to a success URL or a specific page
        return redirect('/../../tables/')
def remove_sched(request, id):
        if Schedule.objects.filter(id=id).exists():
                remove_model2 = get_object_or_404(Schedule, id=id)
                remove_model2.delete()
        else:
            pass

    # Redirect to a success URL or a specific page
        return redirect('/../../tables/')

def delete_child(request, id):
        if Admin_record.objects.filter(id=id).exists():
                delete_model1 = get_object_or_404(Admin_record, id=id)
                delete_model1.delete()
        else:
            pass
        # Redirect to a success URL or a specific page
        return redirect('/../../admin_tables/')

def delete_user(request, id):
    if User.objects.filter(id=id).exists():
                remove_user = get_object_or_404(User, id=id)
                remove_user.delete()
    else:
        pass

    # Redirect to a success URL or a specific page
    return redirect('/../../tables/')

def delete_worker(request, id):
        if User.objects.filter(id=id).exists():
                remove_worker = get_object_or_404(User, id=id)
                remove_worker.delete()
        else:
            pass

    # Redirect to a success URL or a specific page
        return redirect('/../../tables/')

def delete_vaccine(request, id):
        if Vaccine.objects.filter(id=id).exists():
                delete_model3 = get_object_or_404(Vaccine, id=id)
                delete_model3.delete()
        else:
            pass
    # Redirect to a success URL or a specific page
        return redirect('/../../admin_tables/')
def delete_brgy(request, id):
        if Vaccine.objects.filter(id=id).exists():
                delete_model4 = get_object_or_404(Barangay, id=id)
                delete_model14.delete()
        else:
            pass
    # Redirect to a success URL or a specific page
        return redirect('/../../admin_tables/')

def buttons(request):

    return render(request, 'vaxapp/buttons.html')

def utilities(request):

    return render(request, 'vaxapp/utilities-color.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def overall_vaccination_graph(request):

    vaccines = Vaccine.objects.all()
    vaccine_types = [vaccine.name for vaccine in vaccines]
    
    vaccinated_records = Vaccine_record.objects.filter(remarks__icontains='Vaccinated')
    non_vaccinated_records = Vaccine_record.objects.exclude(remarks__icontains='Vaccinated')
    vaccinated_counts = [0] * len(vaccine_types)
    non_vaccinated_counts = [0] * len(vaccine_types)

    for record in vaccinated_records:
        # Get vaccine IDs from the record (assuming 'vax1', 'vax2', 'vax3' are fields in Vaccine_record)
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):  # Check if the ID exists and is an integer
                # Fetch corresponding Vaccine record and get the vaccine name
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    vaccinated_counts[index] += 1

    for record in non_vaccinated_records:
        vaccine_ids = [record.vax1, record.vax2, record.vax3]

        for vaccine_id in vaccine_ids:
            if isinstance(vaccine_id, int):  # Check if the ID exists and is an integer
                vaccine = Vaccine.objects.filter(id=vaccine_id).first()
                if vaccine and vaccine.name in vaccine_types:
                    index = vaccine_types.index(vaccine.name)
                    non_vaccinated_counts[index] += 1

    return render(request, 'vaxapp/overall_vaccination_graph_template.html', {
        'vaccine_types': vaccine_types,
        'vaccinated_counts': vaccinated_counts,
        'non_vaccinated_counts': non_vaccinated_counts,
        
    })