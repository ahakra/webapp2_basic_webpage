# webapp2_basic_webpag
This is basically a webapp2 python google app engine application to deploy a webpage

python version :2.7
python libraries used :webapp2


#app.yaml
service: webapp  //you can remove this line ine app.yaml if you want to deploy app as default app engine service


#To deploy app using cloud shell or google cloud sdk
#set your project id first
gcloud config set project [PROJECT_ID]

#deploy command
gcloud app deploy

#to view app in browser after deploying
gcloud app browse -s webapp 
#the "-s webapp" as declared in app.yaml file ,or if left as a default service,
#you can remove "-s webapp"
