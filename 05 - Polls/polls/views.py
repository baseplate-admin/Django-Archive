from django.shortcuts import render
from django.shortcuts import redirect
from .models import Poll
from django.db.models import F
from .models import IpTable
from django.http import HttpResponse
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    import socket
    try:
        socket.inet_aton(ip)
        ip_valid = True
    except socket.error:
        ip_valid = False
    if bool(ip_valid):
        return ip


def index(request):
    return redirect("all_poll/")


def poll_vote(request, pk):
    # option_one = Poll.objects.get(pk=1)
    # option_one.option_1_count = F('option_1_count') + 1
    # print(option_one)
    # option_one.save()
    poll = Poll.objects.get(pk=pk)
    if request.method == "POST":
        # Add IP to IpTables
        try:
            ip = get_ip(request)
            does_entry_exist = IpTable.objects.get(entry_id=pk)
            does_ip_exist = does_entry_exist.ip
            if does_ip_exist == ip:
                return redirect(f"/thank_you_poll/{pk}/")
        except ObjectDoesNotExist:
            pass
        question = request.POST['question']
        if question == "option1":
            poll.option_1_count = F('option_2_count') + 1
            poll.save()
        elif question == "option2":
            poll.option_2_count = F('option_1_count') + 1
            poll.save()
        elif question == 'option3':
            poll.option_3_count = F('option_3_count') + 1
            poll.save()
        elif question == 'option4':
            poll.option_4_count = F('option_4_count') + 1
            poll.save()

        ip_table = IpTable.objects.create(ip=ip, entry_id=pk)
        ip_table.save()

        return redirect(f"/thank_you_poll/{pk}")

    question = poll.question
    option_one = poll.option_1
    option_two = poll.option_2
    option_three = poll.option_3
    option_four = poll.option_4
    return render(
        request,
        "front/poll_vote.html",
        {
            "pk": pk,
            "question": question,
            "option_one": option_one,
            "option_two": option_two,
            "option_three": option_three,
            "option_four": option_four,
        },
    )


def create_poll(request):
    if request.method == "POST":
        # question = form.cleaned_data["question"]
        # option1 = form.cleaned_data["option_1"]
        # option2 = form.cleaned_data["option_2"]
        # option3 = form.cleaned_data["option_3"]
        # option4 = form.cleaned_data["option_4"]

        question = (request.POST.get("question"))
        option1 = (request.POST.get("option1"))
        option2 = (request.POST.get('option2'))
        option3 = (request.POST.get("option3"))
        option4 = (request.POST.get('option4'))
        import datetime

        time = datetime.datetime.now()
        database = Poll.objects.create(
            question=question,
            option_1=option1,
            option_2=option2,
            option_3=option3,
            option_4=option4,
            time=time,
        )
        database.save()
        query = Poll.objects.get(time=time).pk
        return redirect(f"/polls/{query}/")
    return render(
        request,
        "front/create_poll.html",
    )


def all_polls(request):
    polls = Poll.objects.order_by('-id')[:5]
    return render(request, "front/show_all_polls.html", {
        "polls": polls,
    })


def poll_result(request, pk):
    does_ip_exist = IpTable.objects.filter(entry_id=pk).exists()

    if not bool(does_ip_exist):
        return HttpResponse("You're not allowed to be here.")

    poll = Poll.objects.get(pk=pk)

    question = poll.question
    option_one = poll.option_1
    option_two = poll.option_2
    option_three = poll.option_3
    option_four = poll.option_4
    option_one_count = poll.option_1_count
    option_two_count = poll.option_2_count
    option_three_count = poll.option_3_count
    option_four_count = poll.option_4_count

    all_vote = option_one_count + option_two_count + option_three_count + option_four_count

    context = {
        "all": all_vote,
        "question": question,
        "option_one": option_one,
        "option_two": option_two,
        "option_three": option_three,
        "option_four": option_four,
        "option_one_count": option_one_count,
        "option_two_count": option_two_count,
        "option_three_count": option_three_count,
        "option_four_count": option_four_count,
        }
    # print(context)
    return render(request, "front/poll_result.html", context=context,)


def thank_you_poll(request, pk):

    does_ip_exist = IpTable.objects.filter(entry_id=pk).exists()

    if not bool(does_ip_exist):
        return HttpResponse("You're not allowed to be here.")
    primary_key = Poll.objects.get(pk=pk).pk
    context = {"pk": primary_key}
    return render(request, 'front/thank_you_poll.html', context=context)


