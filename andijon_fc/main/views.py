from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializer import *



@ api_view(['GET'])
def get_Banner (request):
     a = Banner.objects.all()
     ser =BannerSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Navbar (request):
     a =Navbar.objects.all()
     ser =NavbarSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_News (request):
     a = News.objects.all()
     ser =NewsSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Game_schedule (request):
      a = Game_schedule.objects.all()
      ser =Game_scheduleSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Calendar (request):
      a = Calendar.objects.all()
      ser =CalendarSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Schedule (request):
      a = Schedule.objects.all()
      ser =ScheduleSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Player_statistics (request):
     a = Player_statistics.objects.all()
     ser = Player_statisticsSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Shop_1 (request):
     a = Shop_1.objects.all()
     ser =Serializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Shop_2(request):
      a=Shop_2.objects.all()
      ser =Serializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Shop_3 (request):
      a = Shop_3.objects.all()
      ser =Serializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_About_shop (request):
      a=About_shop.objects.all()
      ser =About_shopSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Stadium_photo (request):
      a = Stadium_photo.objects.all()
      ser =Stadium_photoSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Stadium (request):
      a =Stadium.objects.all()
      ser =StadiumSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Arena_history (request):
      a=Arena_history.objects.all()
      ser = Arena_historySerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Arena_history2 (request):
      a = Arena_history2.objects.all()
      ser =Arena_history2Serializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Arena_history3 (request):
     a = Arena_history3.objects.all()
     ser =Arena_history3Serializer(a)
     return Response(ser)


@ api_view(['GET'])
def get_Partners (request):
     a = Partners.objects.all()
     ser =PartnersSerializer(a)
     return Response(ser)


@ api_view(['GET'])
def get_Team_members (request):
      a = Team_members.objects.all()
      ser =Team_membersSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Management (request):
       a = Management.objects.all()
       ser =ManagementSerializer(a, many=True).data
       return Response(ser)


@ api_view(['GET'])
def get_Coach (request):
     a = Coach.objects.all()
     ser =CoachSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Club_info(request):
      a=Club_info.objects.all()
      ser =Club_infoSerializer(a, many=True).data
      return Response(ser)


@ api_view(['GET'])
def get_Club_history (request):
    a = Club_history.objects.all()
    ser =Club_historySerializer(a, many=True).data
    return Response(ser) 


@ api_view(['GET'])
def get_Recommendations(request):
     a = Recommendations.objects.all()
     ser =RecommendationsSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Youtube(request):
     a = Youtube.objects.all()
     ser =YoutubeSerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Academy(request):
     a = Academy.objects.all()
     ser =AcademySerializer(a, many=True).data
     return Response(ser)


@ api_view(['GET'])
def get_Training(request):
     a = Training.objects.all()
     ser =TrainingSerializer(a, many=True).data
     return Response(ser)