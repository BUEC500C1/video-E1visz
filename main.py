from twittwer_api import Get_twitter
from textToImage import setAllImg
from imgToVideo import imgToVideo



def main():
  hashtag = "Harden"
  setAllImg(hashtag)
  imgToVideo(hashtag)


if __name__=="__main__":
    main()
