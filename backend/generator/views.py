from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import prepare_user_image
from . import designs
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
        
        design_map = {
            "1": designs.design_1, "2": designs.design_2, "3": designs.design_3,
            "4": designs.design_4, "5": designs.design_5, "6": designs.design_6,
            "7": designs.design_7, "8": designs.design_8, "9": designs.design_9,
            "10": designs.design_10, "11": designs.design_11, "12": designs.design_12,
            "13": designs.design_13, "14": designs.design_14, "15": designs.design_15,
            "16": designs.design_16, "17": designs.design_17, "18": designs.design_18,
            "19": designs.design_19, "20": designs.design_20,
        }
        
        selected_design = design_map.get(template_id, designs.design_1)
        final_card = selected_design(user_name, address, processed_user_img)
        
        output_name = f"eid_card_{uuid.uuid4()}.jpg"
        output_path = os.path.join(settings.MEDIA_ROOT, output_name)
        final_card.convert("RGB").save(output_path, "JPEG", quality=95)
        
        os.remove(temp_path)
        
        card_url = request.build_absolute_uri(settings.MEDIA_URL + output_name)
        return Response({"card_url": card_url})
