# webapp2_basic_webpag
This is basically a webapp2 python google app engine application <br/>
to deploy a webpage <br/>

python version :2.7 <br/>
python libraries used :webapp2 <br/>


#app.yaml <br/>
service: webapp  //you can remove this line ine app.yaml if you want to deploy app as default app engine service <br/>


#To deploy app using cloud shell or google cloud sdk <br/>
#set your project id first <br/>
gcloud config set project [PROJECT_ID] <br/>

#deploy command <br/>
gcloud app deploy <br/>

#to view app in browser after deploying <br/>
gcloud app browse -s webapp  <br/>
#the "-s webapp" as declared in app.yaml file ,or if left as a default service, <br/>
#you can remove "-s webapp" <br/>
