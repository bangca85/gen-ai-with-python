import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

#Load the pretrained processor and model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image
img_path = "google.png"
# convert it into an rgb format
image = Image.open(img_path).convert('RGB')

text = "the image of"
inputs = processor(images = image, text= text, return_tensors = "pt")

# Generate a caption for the image
outputs = model.generate(**inputs, max_length=50)

# Decode the generated tokens to text
caption = processor.decode(outputs[0], skip_special_tokens=True)
# Print the caption
print(caption)

