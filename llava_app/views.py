from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from PIL import Image
import io

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def process_input(request):
    try:
        # 입력값 가져오기
        user_input = request.data.get('input')
        image_file = request.FILES.get('image')

        if not user_input and not image_file:
            return Response({'output': 'No prompt or image provided.'}, status=400)

        # 테스트용 응답
        output = "Processed prompt and/or image successfully."
        if image_file:
            output += f" Image name: {image_file.name}"

        return Response({'output': output})
    except Exception as e:
        # 에러 처리
        print(f"Error: {e}")  # 서버 로그에 에러 출력
        return Response({'output': 'Error processing the input.'}, status=500)