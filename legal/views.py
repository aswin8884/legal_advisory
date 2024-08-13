from django.shortcuts import render,redirect,get_object_or_404
from .models import*
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime

# Create your views here.

def index(request):

    return render(request,'index.html')

def login(request):

    if request.POST:
        email=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=email,password=password)

        if user:
            if user.is_active:
                if user.is_superuser:
                    return redirect('/admin_home')
                elif user.usertype=="advocate":
                    user = Advocate_registration.objects.get(email=email)
                    if user.approved:
                        request.session["email"] = email
                        request.session["id"] = user.id
                        return redirect('/advocate_home')
                    else:
                        messages.info(request,"Your account is not yet approved by an admin")
                        redirect('/login')
                elif user.usertype=="user":
                    user = User_registration.objects.get(email=email)
                    request.session["email"]=email
                    request.session["id"]=user.id
                    return redirect('/user_home')

    return render(request,'login.html')


def registration_user(request):
    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        gender=request.POST['gender']
        id_proof=request.FILES['id_proof']
        profile_picture=request.FILES['profile_picture']
        email=request.POST['email']
        password=request.POST['password']

        user_login=Login_table.objects.create_user(username=email,password=password,usertype='user')
        user_login.save()

        user=User_registration.objects.create(name=name,
        contact=contact,
        address=address,
        gender=gender,
        id_proof=id_proof,
        profile_picture=profile_picture,
        email=email,
        login_id=user_login)
        user.save()
        messages.info(request,"Registration successful, you can login now")

    return render(request,'registration_user.html')

def registration_advocate(request):

    if request.POST:
        name=request.POST['name']
        contact=request.POST['contact']
        address=request.POST['address']
        gender=request.POST['gender']
        email=request.POST['email']
        password=request.POST['password']
        advocate_type=request.POST['advocate_type']
        id_proof=request.FILES['id_proof']
        degree_cerificate=request.FILES['degree_cerificate']
        licence=request.FILES['licence']
        profile_picture=request.FILES['profile_picture']

        advocate_login=Login_table.objects.create_user(username=email,password=password,usertype='advocate')
        advocate_login.save()

        advocate=Advocate_registration.objects.create(
        name=name,
        contact=contact,
        address=address,
        gender=gender,
        profile_picture=profile_picture,
        id_proof=id_proof,
        advocate_type=advocate_type,
        degree_cerificate=degree_cerificate,
        licence=licence,
        email=email,
        login_id=advocate_login,
        approved=False)
        advocate.save()
        messages.info(request,"Registration successful, please wait for admin approval")


    return render(request,'registration_advocate.html')


#####################   ADMIN   ##################################

def admin_home(request):

    user_count=0
    advocate_count=0
    feedback_count=0
    cases_count=0
    users=User_registration.objects.all()
    feed=Feedbacks.objects.all()
    cases=Cases.objects.all()
    advocate=Advocate_registration.objects.filter(approved=True)

    for u in users:
        user_count+=1
        u.id

    for a in advocate:
        advocate_count+=1
        a.id
 
    for f in feed:
        feedback_count+=1
        f.id
     
    for c in cases:
        cases_count+=1
        c.id   


    return render(request,"admin/admin_home.html",
    {
       "user_count":user_count,
        "advocate_count":advocate_count,
        "feedback_count":feedback_count,
        "cases_count":cases_count
    })

def advocate_requests(request):

    advocates=Advocate_registration.objects.all()

    return render(request,"admin/advocate_requests.html",{"advocates":advocates})

def advocate_approval(request):

    aid=request.GET.get('id')
    advocate=Advocate_registration.objects.get(id=aid)
    advocate.approved=True
    advocate.save()
    messages.info(request,"Accepted advocate request")

    return redirect('/advocate_requests')

def advocate_reject(request):

    aid=request.GET.get('id')
    advocate=Advocate_registration.objects.get(id=aid)
    advocate.delete()
    log=Login_table.objects.get(username=advocate.login_id)
    log.delete()
    messages.info(request,"Rejected advocate request")

    return redirect('/advocate_requests')

def view_advocates_admin(request):

    advocates=Advocate_registration.objects.filter(approved=True)

    return render(request,'admin/view_advocates_admin.html',{"advocates":advocates})

def view_users_admin(request):

    users=User_registration.objects.all()

    return render(request,'admin/view_users_admin.html',{"users":users})

def remove_advocate(request):

    aid=request.GET.get('id')
    advocate=Advocate_registration.objects.get(id=aid)
    advocate.delete()
    messages.info(request,"Successfully removed ")

    return redirect('/view_advocates_admin')

def remove_user(request):

    uid=request.GET.get('id')
    user=User_registration.objects.get(id=uid)
    print(user.login_id)
    user.delete()
    log=Login_table.objects.get(username=user.login_id)
    log.delete()
    messages.info(request,"Successfully removed ")

    return redirect('/view_users_admin')

def add_ipc_section(request):

    if request.POST:
        section_name=request.POST['section_name']
        description=request.POST['description']
        punishment=request.POST['punishment']

        ipc=Ipc_section.objects.create(
        section_name=section_name,
        description=description,
        punishment=punishment)

        ipc.save()

        messages.info(request,'IPC section added successfully')
    return render(request,"admin/add_ipc_section.html")


def update_ipc_section(request):
    
    id=request.GET.get('id')
    ipc=Ipc_section.objects.get(id=id)

    if request.method == 'POST':
        section_name=request.POST["section_name"]
        ipc.section_name=section_name
        description=request.POST["description"]
        ipc.description=description
        punishment=request.POST["punishment"]
        ipc.punishment=punishment
        ipc.save()
        messages.info(request, "Updated Successfully")
        return redirect('/view_ipc_section_admin')

    return render(request,"admin/update_ipc_section.html",{"ipc":ipc})

def remove_ipc_section(request):
    id=request.GET.get('id')
    ipc=Ipc_section.objects.get(id=id)
    ipc.delete()
    messages.info(request,'Removed successfully')
    return redirect('/view_ipc_section_admin')

def view_ipc_section_admin(request):

    ipc=Ipc_section.objects.all()

    return render(request,"admin/view_ipc_section_admin.html",{"ipc":ipc})

def view_feedbacks_admin(request):

    feed=Feedbacks.objects.all()

    return render(request,"admin/view_feedback_admin.html",{"feed":feed})


##################   ADVOCATE   ##################################


def advocate_home(request):
    id=request.session['id']
    advocate=Advocate_registration.objects.get(id=id)

    return render(request,"advocate/advocate_home.html",{"advocate":advocate})

def view_cases_advocate(request):

    case=Cases.objects.filter(status=False)
    req=Request_work_admin.objects.all()

    return render(request,"advocate/view_cases_advocate.html",{"case":case,"req":req})

def request_work_advocate(request):

    cid=request.GET.get('id')
    case=Cases.objects.get(id=cid)
    id=request.session['id']
    advocate=Advocate_registration.objects.get(id=id)

    req=Request_work_admin.objects.create(
        case_id=case,
        advocate_id=advocate,
        status=True,
        accepted_date=datetime.now()
    )
    req.save()
    messages.info(request,"Request sent sucessfully,Wait for users approval")


    return redirect('/view_cases_advocate')

def view_request_from_user_advocate(request):

    id=request.session['id']
    message=Messages.objects.filter(advocate_id=id)

    return render(request,"advocate/view_request_from_user_advocate.html",{"message":message})

def accept_request_from_user_admin(request):
    mid=request.GET.get('id')
    message=Messages.objects.get(id=mid)
    message.status=True
    message.accepted_date=datetime.now()
    message.save()
    messages.info(request,"You accepted that request")
    return redirect('/view_request_from_user_advocate')

def reject_request_from_user_admin(request):
    
    mid=request.GET.get('id')
    message=Messages.objects.get(id=mid)
    message.status=False
    message.accepted_date=datetime.now()
    message.save()
    messages.info(request,"You rejected that request")


    return redirect('/view_request_from_user_advocate')

def view_feedbacks_advocate(request):

    feed=Feedbacks.objects.all()

    return render(request,"advocate/view_feedbacks_advocate.html",{"feed":feed})

def view_work_confirmation_advocate(request):
    id=request.session['id']
    advocate=Advocate_registration.objects.get(id=id)
    work=Cases.objects.filter(advocate_id=advocate)

    return render(request,'advocate/view_work_confirmation_advocate.html',{"work":work})

def edit_profile_advocates(request):

    id=request.session['id']
    advocate=Advocate_registration.objects.get(id=id)

    if request.POST:
        name=request.POST['name']
        advocate.name=name
        contact=request.POST['contact']
        advocate.contact=contact
        address=request.POST['address']
        advocate.address=address
        fees=request.POST['fees']
        advocate.fees=fees
        cases_won=request.POST['cases_won']
        advocate.cases_won=cases_won
        profile_picture=request.FILES['profile_picture']
        advocate.profile_picture=profile_picture
        advocate.save()
        messages.info(request,"Updated Successfully")
        return redirect('/advocate_home')

    return render(request,"advocate/edit_profile_advocate.html",{"advocate":advocate})


######################   USER   ##################################


def user_home(request):
    id=request.session['id']
    user=User_registration.objects.get(id=id)

    return render(request,"user/user_home.html",{"user":user})
def view_advocates_user(request):

    advocates=Advocate_registration.objects.filter(approved=True)

    return render(request,"user/view_advocates_user.html",{"advocates":advocates})

def message_advocate(request):
    aid=request.GET.get('id')
    advocate=Advocate_registration.objects.get(id=aid)
    id=request.session['id']
    user=User_registration.objects.get(id=id)

    if request.POST:
        case=request.POST['case']
        description=request.POST['description']
        current_date=datetime.now()

        message=Messages.objects.create(
            case=case,
            description=description,
            current_date=current_date,
            advocate_id=advocate,
            user_id=user)
        message.save()
        messages.info(request,"Request sent successfully")


    return render(request,"user/message_advocate.html")

def view_ipc_sections_user(request):

    ipc=Ipc_section.objects.all() 

    return render(request,"user/view_ipc_sections_user.html",{"ipc":ipc})

def post_case_user(request):
    id=request.session['id']
    user=User_registration.objects.get(id=id)
    if request.POST:
        case=request.POST['case']
        description=request.POST['description']
        image=request.FILES['image']
        current_date=datetime.now()

        case=Cases.objects.create(
            case=case,
            description=description,
            image=image,
            posted_date=current_date,
            user_id=user
        )
        case.save()
        messages.info(request,'Case posted sucessfully ')

    return render(request,'user/post_case_user.html')


def view_post_cases_user(request):
    id=request.session['id']
    case=Cases.objects.filter(user_id=id)

    return render(request,'user/view_post_cases_user.html',{"case":case})

def delete_post_cases_user(request):
    cid=request.GET.get('id')
    case=Cases.objects.get(id=cid)
    case.delete()
    messages.info(request,'Successfully deleted')

    return redirect('/view_post_cases_user')
def view_request_from_advocate(request):
    id = request.session.get('id')
    if not id:
        messages.error(request, "User not authenticated")
        return redirect('/login')  # Adjust the redirection as per your application

    # Fetch all cases for the user
    cases = Cases.objects.filter(user_id=id)

    # Initialize an empty queryset
    all_requests = Request_work_admin.objects.none()

    # Accumulate all related requests
    for case in cases:
        requests = Request_work_admin.objects.filter(case_id=case)
        all_requests = all_requests | requests

    return render(request, "user/view_request_from_advocate.html", {"requests": all_requests.distinct()})


def accept_request_from_advocate(request):
    rid = request.GET.get('id')
    if not rid:
        messages.error(request, "Request ID not provided")
        return redirect('/view_request_from_advocate')

    try:
        # Retrieve the request by ID
        requests = get_object_or_404(Request_work_admin, id=rid)
        
        # Fetch all cases related to the request
        cases = Cases.objects.filter(id=requests.case_id.id)
        
        if not cases.exists():
            messages.error(request, "No related cases found")
            return redirect('/view_request_from_advocate')
        
        # Update each case
        
        # Update the request
        requests.approval = True
        requests.accepted_date_user = datetime.now()
        requests.save()  # Save the changes to the request object

        for case in cases:
            case.status = True
            case.advocate_id=requests.advocate_id
            case.accepted_date_user=requests.accepted_date_user
            case.save()  # Save each case object
            
        messages.info(request, "Successfully accepted")
    except Request_work_admin.DoesNotExist:
        messages.error(request, "Request not found")
    except Exception as e:
        messages.error(request, f"An error occurred: {str(e)}")
        
    return redirect('/view_request_from_advocate')

def reject_request_from_advocate(request):

    rid=request.GET.get('id')
    requests=Request_work_admin.objects.get(id=rid)
    requests.delete()

    messages.info(request,"Rejected")
    return redirect('/view_request_from_advocate')


def view_replies_from_advocate(request):
    id=request.session['id']
    replies=Messages.objects.filter(user_id=id)

    return render(request,"user/view_replies_from_advocate.html",{"replies":replies})

def delete_posted_case_user(request):
    mid=request.GET.get('id')
    message=Messages.objects.get(id=mid)
    message.delete()
    messages.info(request,"Deleted sucessfully")

    return redirect('/view_replies_from_advocate')

def feedbacks_user(request):
    # Retrieve user ID from session
    id = request.session['id']
    # Ensure the user is retrieved from the correct model, e.g., User model
    try:
        user = User_registration.objects.get(id=id)
    except User_registration.DoesNotExist:
        messages.error(request, "User not found.")
        return render(request, "user/feedbacks_user.html", {"advocate": []})
    
    # Get approved advocates
    advocate = Advocate_registration.objects.filter(approved=True)
    
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        description = request.POST.get('description')
        rating = request.POST.get('rating')
        advocate_id = request.POST.get('advocate_id')
        
        try:
            advocate_instance = Advocate_registration.objects.get(id=advocate_id)
        except Advocate_registration.DoesNotExist:
            messages.error(request, "Advocate not found.")
            return render(request, "user/feedbacks_user.html", {"advocate": advocate})
        
        # Create the Feedback instance
        Feedbacks.objects.create(
            feedback=feedback,
            description=description,
            advocate_id=advocate_instance,
            user_id=user,
            rating=rating,
            posted_date=datetime.now()
        )
        
        messages.info(request, 'Feedback sent successfully')
    
    return render(request, "user/feedbacks_user.html", {"advocate": advocate})

def view_feedbacks_user(request):

    feed=Feedbacks.objects.all()

    return render(request,"user/view_feedbacks_user.html",{"feed":feed})