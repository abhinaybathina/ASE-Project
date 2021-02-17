from django.shortcuts import render
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import redirect_loggeduser, unauthenticated_user
from django.contrib.auth.models import Group
from farm.models import Farm
from .forms import VillageQueryForm, StateQueryForm, CropQueryForm
from django.shortcuts import redirect
from django.db.models import Sum
from announcements.models import Announcement
from rest_framework.views import APIView
from rest_framework.response import Response

crops_list = (
    'Rice', 'Wheat', 'Dal', 'Maize', 'Pulses', 'Millets', 'Sugarcane',
    'Tobacco', 'Cotton', 'Coffee', 'Coconut', 'Tea'
)


@redirect_loggeduser
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username, name, role = form.cleaned_data.get('username'), form.cleaned_data.get('first_name'), \
                                   form.cleaned_data.get('role')
            farmer = Group.objects.get(name='Farmers')
            staff = Group.objects.get(name='Staff')
            if role == 'Farmers':
                user.groups.add(farmer)
            else:
                user.groups.add(staff)

            messages.success(request,
                             f'Account created for {name} with Username : {username} . You can now login here!')
            return redirect('userLogin')
    else:
        form = RegistrationForm()
    return render(request, 'users/user_registration.html', {'form': form, 'title': 'User Register'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,
                             f'Your Account has been successfully updated')

            return redirect('Profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'User Profile'
    }
    return render(request, 'users/user_profile.html', context)


@login_required
def user_homepage(request):
    user = request.user
    user_group = user.groups.all().first()
    if user_group.name == 'Farmers':
        return render(request, 'users/farmer_homepage.html', {'title': 'Home'})
    else:
        return render(request, 'users/staff_homepage.html', {'title': 'Staff-Home'})


# Class based views template lookup : <app>/<model>_<viewtype>.html

@unauthenticated_user
@login_required
def query_farm_data(request):
    if request.method == 'POST':
        if 'query_village' in request.POST:
            # All the three forms that will be sent as context to the page
            village_form = VillageQueryForm(request.POST)
            state_form = StateQueryForm()
            crop_form = CropQueryForm()

            if village_form.is_valid():
                village = village_form.cleaned_data['village']
                farm_objects = Farm.objects.filter(village=village)
                if farm_objects.exists():
                    village_data = get_village_data(farm_objects)
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': village_data,
                        'state_data': None,
                        'crop_data': None
                    }
                else:
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': None,
                        'state_data': None,
                        'crop_data': None
                    }
                return render(request, 'users/farm_lookup.html', context)
        elif 'query_state' in request.POST:
            state_form = StateQueryForm(request.POST)
            village_form = VillageQueryForm()
            crop_form = CropQueryForm()

            if state_form.is_valid():
                state = state_form.cleaned_data['state']
                farm_objects = Farm.objects.filter(state=state)
                if farm_objects.exists():
                    print(farm_objects, state)
                    state_data = get_state_data(farm_objects)
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': None,
                        'state_data': state_data,
                        'crop_data': None
                    }
                else:
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': None,
                        'state_data': None,
                        'crop_data': None
                    }
                return render(request, 'users/farm_lookup.html', context)

        elif 'query_crop' in request.POST:
            crop_form = CropQueryForm(request.POST)
            village_form = VillageQueryForm()
            state_form = StateQueryForm()

            if crop_form.is_valid():
                crop = crop_form.cleaned_data['crop']
                farm_objects = Farm.objects.filter(crop=crop)
                if farm_objects.exists():
                    crop_data = get_crop_data(farm_objects, crop)
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': None,
                        'state_data': None,
                        'crop_data': crop_data
                    }

                else:
                    context = {
                        'village_form': village_form,
                        'state_form': state_form,
                        'crop_form': crop_form,
                        'village_data': None,
                        'state_data': None,
                        'crop_data': None
                    }
                return render(request, 'users/farm_lookup.html', context)

    else:
        village_form = VillageQueryForm()
        state_form = StateQueryForm()
        crop_form = CropQueryForm()
        context = {
            'village_form': village_form,
            'state_form': state_form,
            'crop_form': crop_form
        }

    return render(request, 'users/farm_lookup.html', context)


def get_village_data(farm_objects):
    crops = farm_objects.values('crop').order_by('crop').annotate(total=Sum('expecting_yield'))
    village_data = {
        'Total_farmers': len(farm_objects.values_list('owner').distinct().order_by('owner')),
        'Crop_list': crops.order_by('-total'),
        'Major_crop': crops.order_by('-total').values_list('crop', flat=True)[0],
        'Total_land': farm_objects.aggregate(Sum('total_land_available')),
        'Land_cultivating': farm_objects.aggregate(Sum('land_cultivating'))
    }
    return village_data


def get_state_data(farm_objects):
    crops = farm_objects.values('crop').order_by('crop').annotate(total=Sum('expecting_yield'))
    state_data = {
        'Villages_list': farm_objects.values_list('village', flat=True).distinct().order_by('village'),
        'Villages_count': farm_objects.values('village').distinct().count(),
        'Total_farmers': len(farm_objects.values_list('owner').distinct().order_by('owner')),
        'Crop_list': crops.order_by('-total'),
        'Major_crop': crops.order_by('-total').values_list('crop', flat=True)[0],
        'Total_land': farm_objects.aggregate(Sum('total_land_available')),
        'Land_cultivating': farm_objects.aggregate(Sum('land_cultivating'))
    }
    return state_data


def get_crop_data(farm_objects, crop):
    expected_yield = farm_objects.aggregate(total=Sum('expecting_yield'))['total']
    total_crops_yield = Farm.objects.exclude(crop=crop).aggregate(total=Sum('expecting_yield'))['total']
    share = round(expected_yield / (expected_yield + total_crops_yield), 2)
    crop_data = {
        'Expected_yield': expected_yield,
        'Share': share * 100,
        'Total_states_contributing': len(farm_objects.values_list('state', flat=True).distinct().order_by('state')),
        'States_contributing': list(farm_objects.values_list('state', flat=True).distinct().order_by('state')),
        'Land_cultivating': sum(list(farm_objects.values_list('land_cultivating', flat=True)))
    }
    return crop_data


@login_required
def announcements_list(request):
    announcements = Announcement.objects.all()
    crop_yield = crop_wise_yield()
    avg_yield = sum(crop_yield.values()) / len(crop_yield.values())
    context = {
        'announcements': announcements,
        'crop_yield': crop_yield,
        'avg_yield': avg_yield
    }
    return render(request, 'users/list_of_announcements.html', context)


def crop_wise_yield():
    crops = Farm.objects.filter(crop__in=crops_list).values('crop').annotate(total=Sum('expecting_yield')).order_by(
        '-total')
    crop_yield = {crop: 0 for crop in crops_list}
    for entry in crops:
        crop_yield[entry['crop']] = float(entry['total'])
    return crop_yield


def crop_wise_land():
    crops = Farm.objects.filter(crop__in=crops_list).values('crop').annotate(total=Sum('land_cultivating')).order_by(
        '-total')
    crop_land = {crop: 0 for crop in crops_list}
    for entry in crops:
        crop_land[entry['crop']] = float(entry['total'])
    return crop_land


def yield_estimates_staff(request):
    crop_yield = crop_wise_yield()
    avg_yield = sum(crop_yield.values()) / len(crop_yield.values())
    crop_land = crop_wise_land()
    context = {
        'crop_yield': crop_yield,
        'avg_yield': avg_yield,
        'crop_land': crop_land
    }
    return render(request, 'users/staff_crops_wise_yield.html', context)


class CropData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        crop_data = Farm.objects.all().values('crop').order_by('-total').annotate(total=Sum('expecting_yield'))
        state_data = Farm.objects.all().values('state').order_by('-total').annotate(total=Sum('land_cultivating'))

        serialized_data = {
            'crops': [data['crop'] for data in crop_data[:5]],
            'yields': [data['total'] for data in crop_data][:5],
            'states': [data['state'] for data in state_data[:5]],
            'land_area': [data['total'] for data in state_data[:5]],
        }
        return Response(serialized_data)