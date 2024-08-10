from dao.feeds import Feeds
from dto.myexception import myException
import base64

#Get All Feeds
def all_feeds():
    data = Feeds.objects()
    return data

#Create New Feed
def new_feed(title, subdescription, description, image, status):
    poster = image.read()
    encoded_image = base64.b64encode(poster).decode("utf-8")
    data = Feeds(title=title, subDescription=subdescription, description=description, posterImg=encoded_image, status=status)
    data.save()
    return data

#Get Feed By Id
def get_feed(feedId):
    feed = Feeds.objects(id=feedId).first()
    if not feed:
        raise myException ("Feed not found !",400);
    return feed

#Update Feed By Id
def update_feed(feedId, title, subdescription, description, image, status):
    data = Feeds.objects(id=feedId).first()    
    if not data:
        raise myException('Feed not found !',400);
    poster = image.read()
    encoded_image = base64.b64encode(poster).decode("utf-8")
    data.update(title=title, subDescription=subdescription, description=description, posterImg=encoded_image, status=status)
    return get_feed(feedId)

#Delete Feed By Id
def delete_feed(feedId):
    data = Feeds.objects(id=feedId).first()    
    if not data :
        raise myException ("Feed not found !",400)
    data.delete()
    return data 