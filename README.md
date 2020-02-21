# video-E1visz
video-E1visz created by GitHub Classroom

#### Contents

* [Product Mission](#product-mission)
* [Recommendation](#Recommendation)
* [Architecture Needed](#architecture-needed)
* [Run Program](#run-program)
* [Results](#test-cases)
* [Question](#lessons-learned)

<a name="product-mission"/> 

## Project Mission
Develop a queue system that can collect the latest twitters of a given hashtage and convert the text to a short video summary in the same time.  

<a name="Recommendation"/>

## Recommendation
* Develop a queue system that can exercise your requirements with stub functions.  
* Develop the twitter functionality with an API.  
* Integrate them.  

<a name="architecture-needed"/>

## Architecture Needed

* Python code running on computer.    

* twitter API(Tweepy).  

* Pillow(PIL).  

* OpenCV(cv2).  

* Queue, Threading.  

<a name="run-program"/>

## Run Program

*Assumes __OpenCV, Pillow__ package already installed.*

*Assumes __twitter API Keys__ available.*

*Requires __Python 3.x__ to run!*

1. Clone the repo by using the command below.
   ```
   $ git clone https://github.com/BUEC500C1/video-E1visz.git
   ```

2. Ensure the following Python packages are installed: cv2, PIL, tweepy
   ```
   $ pip install opencv  
   $ pip install pillow
   $ pip install tweepy
   ```
3. Add API key to local "configr.py" file and save:  
   ```
   consumer_key = "your API key"
   consumer_secret = "your API secret key"
   access_token = "your access token key"
   access_token_secret = "your access token secret key"
   ```
4. Open terminal/command window and navigate to folder where code was downloaded

5. Open "SetQue.py", enter the hashtag in the code below.
   ```
   hashtag = ['James', 'Kobe', 'James Harden', 'Curry', 'Wade', 'Trump']
   ```
6. run the "SetQue.py", the images and videos will be saved automatically in the local file system.

<a name="test-cases"/>

## Results


1. The image stored in the file system.[Click](https://github.com/BUEC500C1/video-E1visz/tree/master/img)  
   <img src="img/Img result.png">
2. The video stored in the file system.[Click](https://github.com/BUEC500C1/video-E1visz/tree/master/Video)  
   <img src="img/Video result.png">
3. The UI for tracking the process.(Four threads)  
   <img src="img/Interface.png">

<a name="lessons-learned"/>

## Question

### 1. How many API calls you can handle simultaneously and why?  
      Now only one worker used in the process for one API. 
      However, I can apply four different workers simutaneously.
### 2. For example, run different API calls at the same time?  
      Yes.
### 3. Split the processing of an API into multiple threads?  
      I use 4 threads for the process. 



