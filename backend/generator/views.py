from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import prepare_user_image
from .designs import design_1, design_2
import uuid
import os
from django.conf import settings

class GenerateCardView(APIView):
    def post(self, request):
        user_name = request.data.get('name', 'আপনার নাম')
        address = request.data.get('address', 'আপনার ঠিকানা')
        template_id = request.data.get('template_id', '1')
        image_file = request.FILES.get('image')

        temp_name = f"temp_{uuid.uuid4()}.png"
        temp_path = os.path.join(settings.MEDIA_ROOT, temp_name)
        
        with open(temp_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)

        processed_user_img = prepare_user_image(temp_path)
        
        designs = {
            "1": design_1,
            "2": design_2,
        }
        
        selected_design = designs.get(template_id, design_1)
        final_card = selected_design(user_name, address, processed_user_img)
        
        output_name = f"eid_card_{uuid.uuid4()}.jpg"
        output_path = os.path.join(settings.MEDIA_ROOT, output_name)
        final_card.convert("RGB").save(output_path, "JPEG", quality=95)
        
        os.remove(temp_path)
        
        card_url = request.build_absolute_uri(settings.MEDIA_URL + output_name)
        return Response({"card_url": card_url})
