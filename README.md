# Trafficontrol

#Inspiration

Ever happened to us that on red signal we are behind stop line but many people are on the stop or on pedestrian crossing making it difficult for people to cross road. Or on no-parking area people are parking their vehicles making it difficult for others to drive in that area. It makes me thinking can we this dump traffic cctv camera's, speakers smarter & with that born a smart near real time video analysis solution.

#What it does

This project (Trafficcontrol) is a near real time video analysis solution which analyzes camera feed using Artificial Intelligence. Now let's see what exactly it does :

 1.   On traffic signal when there is red light Trafficontrol will generate custom voice alerts if someone stop their vehicle on pedestrian crossing or on stop line. By this alert system people will get educated and people can start following rules in the future.
 2.  By using same solution we are generating custom voice alerts if someone tries to park their vehicle in no parking areas.
 3.  In future we are planning to make this solution more smart by teaching to detect more traffic rules so it can detect more such things and alert the police.

#How we built it

 1.   First collected video feeds from traffic signal for training our algorithms to make them differentiate between who is breaking law & who is not.
 2.  Break those video into images and then store them different folder for training, validation purpose.
 3.  Trained machine learning algorithm for making classification on traffic signal and no-parking area video feed.
 4.  Built solution to read live video feed and pass it to machine learning algorithms for classification purpose like are anyone breaking law?

#Accomplishments that we are proud of

This is first machine learning task we have perform for practical purpose. We happy with the result it is showing and making Bangalore more smarter by using existing hardware infrastructure it has like cctv, speakers.

#What we learned

How to think for any practical problems and come up with solutions. First think about solution which can use existing infrastructure so new solution can cost less. Many new think about machine learning like overfitting issues, training and validation data issue.

#What's next for Trafficoontrol

Now we want to build more smart solution like if someone is breaking traffic rules capture his number plate and generate challan with that automate complete challan system so people can get alert about challan on their mobile number. They have to pay the same online for more transparency.
