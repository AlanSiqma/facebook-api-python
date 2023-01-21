import facebook
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('TOKEN')

api = facebook.GraphAPI(token)


def send_feed(message):
    api.put_object("me", "feed", message=message)


def seen_image_with_text(image, message):
    api.put_photo(image=open(image, 'rb'),
                  message=message)


# send_feed("Happy Coding!" + " #LearnPython4")
seen_image_with_text('tweet-post.png', "Happy Coding!" + " #LearnPython5")
