from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from patient_first.models import Patient, Encounter
from patient_first.forms import PatientForm, EncounterForm, UserForm, UserProfileForm
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    patient_list = Patient.objects.order_by('last_name')
    context_dict = {'Patients': patient_list}

    return render(request, 'patient_first/index.html', context=context_dict)


def show_patient(request, patient_name_slug):
    context_dict = {}
    try:
        patient = Patient.objects.get(slug=patient_name_slug)
        encounter = Encounter.objects.filter(patient=patient)
        context_dict['encounter'] = encounter
        context_dict['patient'] = patient
    except Patient.DoesNotExist:
        context_dict['encounter'] = None
        context_dict['patient'] = None

    return render(request, 'patient_first/patient.html', context_dict)


def add_patient(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            pat = form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'patient_first/add_patient.html', {'form': form})


def add_encounter(request, patient_name_slug):
    try:
        patient = Patient.objects.get(slug=patient_name_slug)
    except Patient.DoesNotExist:
        patient = None
    form = EncounterForm()
    if request.method == 'POST':
        form = EncounterForm(request.POST)
        if form.is_valid():
            if patient:
                encounter = form.save(commit=False)
                encounter.patient = patient
                encounter.save()
                return show_patient(request, patient_name_slug)
        else:
            print(form.errors)
    context_dict = {'form': form, 'patient': patient}
    return render(request, 'patient_first/add_encounter.html', context_dict)


def about(request):
    return render(request, 'patient_first/about.html', {})


def register(request):
    # A boolean value for telling the template
    # whether the registration was successful.
    # Set to False initially.  Code changes value to
    # True when registration succeeds.
    registered = False

    # if it's a HTTP POSE, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our forms using two ModelForm instances.
        # These forms will be blank, ready for user input.

        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
                  'patient_first/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull ou the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request POST.get('<variable>') as opposed
        # to request.POST('<variable>'), because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log in the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied")

    # The request is not a HTTP POST, so displayed the login form.
    # THe scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object.
        return render(request, 'patient_first/login.html', {})


@login_required()
def restricted(request):
    return render(request, 'patient_first/restricted.html', {})


# Use the login_required() decorator to ensure only those logged in can access
# the view
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect(reverse('index'))
