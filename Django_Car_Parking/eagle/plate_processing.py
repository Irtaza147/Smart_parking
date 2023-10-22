from landingai.predict import Predictor
from landingai import visualize
from landingai.postprocess import crop
from landingai.predict import OcrPredictor
from PIL import Image

def detect_license_plate(image, api_key, model_endpoint):
    predictor = Predictor(model_endpoint, api_key=api_key)
    prediction = predictor.predict(image)
    overlayed_frame = visualize.overlay_predictions(prediction, image)
    return prediction, overlayed_frame

def crop_license_plate(bounding_boxes, image):
    cropped_images = crop(bounding_boxes, image)
    return cropped_images

def perform_ocr(image, api_key):
    ocr_predictor = OcrPredictor(api_key=api_key)
    ocr_preds = ocr_predictor.predict(image)
    overlayed_ocr = visualize.overlay_predictions(ocr_preds, image)
    return ocr_preds, overlayed_ocr

def main():
    api_key_license_plate = "land_sk_aMemWbpd41yXnQ0tXvZMh59ISgRuKNRKjJEIUHnkiH32NBJAwf"
    model_endpoint_license_plate = "e001c156-5de0-43f3-9991-f19699b31202"
    
    # Prompt the user for the image file path
    image_path ="C:\\Users\\aliir\\Downloads\\Django Car Parking\\Django_Car_Parking\\media\\myimage\\1_aYa6JEi.jpeg"
    
    try:
        # Load the image
        image = Image.open(image_path)

        # Detect license plates in the single image
        bounding_boxes, overlayed_frame = detect_license_plate(image, api_key_license_plate, model_endpoint_license_plate)

        # print the overlayed frame
        if bounding_boxes:
            print(overlayed_frame)
        else:
            print("No license plates detected in the image.")

        # Crop the license plates in the single image
        cropped_images = crop_license_plate(bounding_boxes, image)

        # print the cropped license plates
        for cropped in cropped_images:
            print(cropped)

        # Perform OCR on the single image
        api_key_ocr = "land_sk_aMemWbpd41yXnQ0tXvZMh59ISgRuKNRKjJEIUHnkiH32NBJAwf"
        ocr_preds, overlayed_ocr = perform_ocr(image, api_key_ocr)

        # Storing OCR results in an 'output_text' variable
        output_text = []
        if ocr_preds:
            for text in ocr_preds:
                output_text.append(text.text)
                print(text.text)
        else:
            print("No text detected in the image.")

        # You can now access the extracted text from the 'output_text' variable
        print("OCR Results:")
        for text in output_text:
            print(text)
    
    except Exception as e:
        print ("An error occurred: {str(e}")

if __name__ == "__main__":
    main()
