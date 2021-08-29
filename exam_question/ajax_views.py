from django.http import JsonResponse
from django.views import View
from exams.models import Question, ExaminerExamRegistration, Subjects, Score, ExamRegistration
from geopy.geocoders import Nominatim
from users.models import Location


class CreateQuestion(View):
    def get(self, request):
        id = request.GET.get('id', None)
        question = request.GET.get('question', None)
        option_A = request.GET.get('optionA', None)
        option_B = request.GET.get('optionB', None)
        option_C = request.GET.get('optionC', None)
        option_D = request.GET.get('optionD', None)
        correct_answer = request.GET.get('answer', None)
        registered = ExaminerExamRegistration.objects.get(id=id, examiner=request.user)

        obj = Question.objects.create(
            registration=registered,
            question=question,
            option_A=option_A,
            option_B=option_B,
            option_C=option_C,
            option_D=option_D,
            answer=correct_answer
        )
        questions = {
            'id': obj.id,
            'question': obj.question,
            'option_A': obj.option_A,
            'option_B': obj.option_B,
            'option_C': obj.option_C,
            'option_D': obj.option_D,
            'answer': obj.answer,
        }

        data = {
            'questions': questions
        }
        return JsonResponse(data)


class GetQuestions(View):
    def get(self, request):
        #id = request.GET.get('id', None)
        subject = request.GET.get('subject', None)

        code = subject[-7:-1]
        get_question = Question.objects.filter(registration__examiner=request.user, registration__subject__subject_code=code)
        questions = []
        data = {}
        for i in range(len(get_question)):
            ques = {
                'id': get_question[i].id,
                'question': get_question[i].question,
                'option_A': get_question[i].option_A,
                'option_B': get_question[i].option_B,
                'option_C': get_question[i].option_C,
                'option_D': get_question[i].option_D,
                'correct_answer': get_question[i].answer,
            }
            questions.append(ques)
        data['questions'] = questions
        return JsonResponse(data)


class StudentQuestions(View):
    def get(self, request):
        # id = request.GET.get('id', None)
        subject = request.GET.get('subject', None)

        code = subject[-7:-1]
        get_question = Question.objects.filter(registration__subject__subject_code=code)
        questions = []
        data = {}
        for i in range(len(get_question)):
            ques = {
                'id': get_question[i].id,
                'question': get_question[i].question,
                'option_A': get_question[i].option_A,
                'option_B': get_question[i].option_B,
                'option_C': get_question[i].option_C,
                'option_D': get_question[i].option_D,
                'correct_answer': get_question[i].answer,
            }
            questions.append(ques)
        data['questions'] = questions
        return JsonResponse(data)


class SaveAnswer(View):
    def get(self, request):
        id = request.GET.get('id', None)
        score = request.GET.get('score', None),
        subject = request.GET.get('subject', None)

        obj = Score.objects.create(
                candidate=request.user.username,
                subject=subject,
                score=score
        )
        user_score = {
            'id': obj.id,
            'name': obj.candidate,
            'subject': obj.subject,
            'score': obj.score
        }

        data = {
            'user_score': user_score
        }
        return JsonResponse(data)


class SubectAnswered(View):
    def get(self, request):
        get_score = Score.objects.filter(candidate=request.user.username)
        student_score = []
        data = {}
        for score in get_score:
            x = {
                'id': score.id,
                'name': score.candidate,
                'sub': score.subject,
                'student_score': score.score,
                'date': score.date
            }
            student_score.append(x)
        data['score_details'] = student_score
        return JsonResponse(data)


class GetLocation(View):
    def get(self, request):
        latitude = request.GET.get('latitude')
        longitude = request.GET.get('longitude')

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.reverse(latitude+','+longitude)
        #print(location)
        address = location.raw['address']
        #print(address)

        obj = Location.objects.create(
            user=request.user.username,
            country=address.get('country', ''),
            state=address.get('state', ''),
            city_or_town=address.get('town', ''),
            local_govt=address.get('county', ''),
            zip_code=address.get('postcode', '')
        )
        location_details = {
            'user': obj.user,
            'country': obj.country,
            'state': obj.state,
            'city_or_town': obj.city_or_town,
            'local_govt': obj.local_govt,
            'zip_code': obj.zip_code
        }
        data = {
            'location_details': location_details
        }
        return JsonResponse(data)