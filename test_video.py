from twittwer_api import Get_twitter

def test_tweetApi():
  hashtag = "Test"
  assert Get_twitter(hashtag) != ''