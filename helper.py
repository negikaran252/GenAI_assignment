import os, base64, requests, json, io, uuid
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

'''
Function to extract text from image
'''
def image_ocr(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()

    # Construct the JSON request
    data = {
    "requests": [
        {
        "image": {
            "content": encoded_string
        },
        "features": [
            {
            "type": "TEXT_DETECTION"
            }
        ]
        }
    ]
    }

    # Convert it to a JSON string
    data = json.dumps(data)

    # Specify the URL of the API endpoint
    key=os.getenv('GCP_OCR')
    url = 'https://vision.googleapis.com/v1/images:annotate?key='+key

    # Make the request
    response = requests.post(url, data=data)

    # Return the response
    return response.json()['responses'][0]['textAnnotations'][0]['description']


'''
function to translate text to another text
'''
def text_translation(target_text,target_language_code):
    subscription_key=os.getenv('AZURE_TEXT_KEY')
    endpoint="https://api.cognitive.microsofttranslator.com/"

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'eastus',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }   

    body = [{
        'text': target_text
        }]
    params = {
        'api-version': '3.0',
        'to': target_language_code
    }
    request_url = endpoint + "/translate"
    response = requests.post(request_url, params=params, headers=headers, json=body)
    return response.json()[0]['translations'][0]['text']


'''
function to convert to audio
'''
def text_to_speech(text, lang):
    subscription_key=os.getenv('AZURE_SPEECH_KEY')
    region = 'eastus'
    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    speech_config.speech_synthesis_language = lang
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config,audio_config=None)
    audio_filename = "static/output.wav"
    audio_output = speechsdk.AudioDataStream(speech_synthesizer.speak_text_async(text).get())
    audio_output.save_to_wav_file(audio_filename)
    # Read the file into an io.BytesIO object
    with open(audio_filename, 'rb') as f:
        audio_file = io.BytesIO(f.read())
    return audio_file