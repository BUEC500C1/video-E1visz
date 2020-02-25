from twittwer_api import Get_twitter
from textToImage import setAllImg
from imgToVideo import imgToVideo
import os

def test_tweetApi():
  hashtag = "Test"
  assert Get_twitter(Test) != ''

def test_mainFunction():
  hashtag = "Test"
  setAllImg(hashtag)
  imgToVideo(hashtag)
  assert os.path.exists('Test.avi') == True

