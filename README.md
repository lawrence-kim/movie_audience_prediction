Movie Audience Prediction
=========
Hypothesis
----------
Many people in South Korea judge a movie by its cover. They usually consider two factors, the director and actors, when deciding whether to watch the film. Therefore we have developed a model with a machine learning algorithm that has the least root square error to estimate the audience prediction.


Method
----------
* Source: KOBIS (Korea Box-office Information System, 2003~2019)  
* ML model: KNN regressor  
* Label: Number of audience  
* Other columns: film name, film distributing company, film rating, film genre, film actor, film director  


Getting Started
-----------

After downloading movie_audience_prediction repository, please type below on command prompt or shell  
<pre>
<code>
$ [sudo] python3 project-main.py  
</code>
</pre>  



GUI samples
-------
### Main page  
<img width="251" alt="movie_main" src="https://user-images.githubusercontent.com/57359849/76737391-08544e00-67ac-11ea-9664-fab1d61eb203.PNG">  

### Introduction  
<img width="501" alt="movie_introduction" src="https://user-images.githubusercontent.com/57359849/76737949-0fc82700-67ad-11ea-8491-52eb366d8891.PNG">  
brief explanations in Korean  

### Ranking    
<img width="651" alt="movie_ranking" src="https://user-images.githubusercontent.com/57359849/76737971-1787cb80-67ad-11ea-84e2-34121c87ce56.PNG">  
first column = actor  
second column = accumulated number of audiences   

### Chart   
<img width="801" alt="movie_chart" src="https://user-images.githubusercontent.com/57359849/76737980-1e164300-67ad-11ea-8632-69a0ec30c699.PNG">  
above chart is sorted by genre types  

### Visualization  
<img width="661" alt="movie_visualization" src="https://user-images.githubusercontent.com/57359849/76738000-27071480-67ad-11ea-8813-4c777603ca09.PNG">  
above word cloud is sorted by film distributing companies  

### Prediction  
<img width="464" alt="movie_prediction" src="https://user-images.githubusercontent.com/57359849/76738008-2bcbc880-67ad-11ea-9028-6166fc0bddf8.PNG">  
Prediction of a movie released in November 2020, directed by 이병헌 with an actor 송강호, distributed by 씨제이, genre type drama, PG-13 rating gives an output of 11,826,567 audiences.  





