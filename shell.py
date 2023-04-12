import datetime
from user.models import Student, Mentor, Language, Course

languages = [
    {
        'name': 'Python',
        'months_to_learn': 6
    },
    {
        'name': 'Java Script',
        'months_to_learn': 6
    },
    {
        'name': 'UX-UI',
        'months_to_learn': 2
    },
]
python_lang = Language.objects.create(name='Python', month_to_learn=6)
python_lang.save()
javascript_lang = Language.objects.create(name='JavaScript', month_to_learn=6)
javascript_lang.save()
uxui_design_lang = Language.objects.create(name='UX-UI design', month_to_learn=2)
uxui_design_lang.save()


students = [
    {
        'name': 'Amanov Aman',
        'email': 'aman@mail.ru',
        'phone_number': '+996700989898',
        'work_study_place': 'School №13',
        'has_own_notebook': True,
        'preferred_os': 'windows'
    },
    {
        'name': 'Apina Alena',
        'email': 'aapina@bk.ru',
        'phone_number': '0550888888',
        'work_study_place': 'TV',
        'has_own_notebook': True,
        'preferred_os': 'mac'
    },
    {
        'name': 'Phil Spencer',
        'email': 'spencer@microsoft.com',
        'phone_number': '0508312312',
        'work_study_place': 'Microsoft Gaming',
        'has_own_notebook': False,
        'preferred_os': 'linux'
    }
]
aman = Student.objects.create(
    name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
    work_study_place='School №13', has_own_notebook=True, preferred_os='Windows'
)
aman.save()
alena = Student.objects.create(
    name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
    work_study_place='TV', has_own_notebook=True, preferred_os='Mac'
)
alena.save()
phil = Student.objects.create(
    name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
    work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='Linux'
)
phil.save()


mentors = [
    {
        'name': 'Ilona Maskova',
        'email': 'imask@gmail.com',
        'phone_number': '0500545454',
        'main_work': None,
        'experience': datetime.date(year=2021, month=10, day=23)
    },
    {
        'name': 'Halil Nurmuhametov',
        'email': 'halil@gmail.com',
        'phone_number': '0709989876',
        'main_work': 'University of Fort Collins',
        'experience': datetime.date(year=2010, month=9, day=18)
    }
]
ilona = Mentor.objects.create(
    name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
    main_work=None, experience=(2021-10-23)
)
ilona.save()
halil = Mentor.objects.create(
    name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
    main_work='University of Fort Collins', experience=(2010-9-18)
)
halil.save()


python_course = Course.objects.create(
    name='Python – 21', language=python_lang, date_started=(2022-8-1),
    mentor=halil, student=aman,
)
python_course.student.add(alena)

uxui_design_course = Course.objects.create(
    name='UXUI design – 43', language=uxui_design_lang, date_started=(2022-8-22),
    mentor=ilona, student=phil,
)
