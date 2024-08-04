import requests
import streamlit as st
from datetime import date, timedelta

# Get yesterday's date
today = date.today()
yesterday = today - timedelta(days=1)

# Setup request parameters and inject api key
api_key = "xPGfXxiiGsDzseYawQu2pp4TSpfh8EPIQSysDf3E"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={yesterday}"
response = requests.get(url)
content = response.json()

# Set page configuration
st.set_page_config(layout="wide")

# Create header
st.title(content["title"])

# Check if link is image or video, return image or embed video
image_check = requests.head(content["url"], allow_redirects=True)
content_type = image_check.headers.get('Content-Type')
if content_type and ('image/jpeg' in content_type or 'image/png' in content_type or 'image/gif' in content_type):
    image = content["url"]
    st.image(image)
else:
    video = content["url"]
    st.video(video)

# Create content
st.write(content["explanation"])
