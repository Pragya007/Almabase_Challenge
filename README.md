# Almabase Challenge
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/logo.jpg)

## Problem Statement
Find the n most popular repositories of a given organization on Github (Eg:https://github.com/google) based on the number of forks. For each such repo find the top m committees and their commit counts. 

## Application
This is a CLI serving the purpose of fetching most popular repositories on the basis of forks. Here GitHub API is used to fetch repository and sort them on the basis of forks then inside each of repository, committees are also fetched according to given committee count.



## Technology Stack

 1.  Python 3.7

### Dependencies

1. requests
2. re
3. json

## How to Use
1. Clone the Repository to a folder: ```git clone https://github.com/Pragya007/Almabase_Challenge.git```
2. Run following in the command prompt: ```cd Almabase/Code Files```
3. ```pip install re```
4. ```pip install requests```
5. ```pip install json```
6. ```python github_app.py google 20 8``` Here in place of "google 20 8" any arguments can be given to test any case.



# Screenshots

#### 1 Testcase
Org: google, n: 5, m: 3
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/1.png)
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/2.png)

#### 2 Testcase
Org: microsoft, n: 20, m: 8

![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/3.png)
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/4.png)

![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/5.png)
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/6.png)

![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/7.png)
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/8.png)

![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/9.png)

#### 3 Testcase
Org: microsoft, n: 101, m: 17

![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/10.png)
![](https://github.com/Pragya007/Almabase_Challenge/blob/main/Screenshots/11.png)

# Author
Pragya  
(pragyachaurasia24@gmail.com)
