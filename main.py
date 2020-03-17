import webapp2

class Hello(webapp2.RequestHandler):
    def get(self):
       self.response.write("""<!DOCTYPE html>
<html>
<body style="background-color:black">

<img src="/images/cloud2.jpg" style="width:100%" alt="GCP">
<p>&nbsp;</p><p>&nbsp;</p>
<h1 style="text-align: center;"><span style="color: #ffffff;"><strong>Welcome to the cloud</strong></span></h1>
<p>&nbsp;</p><p>&nbsp;</p><p>&nbsp;</p>
</body>
</html>
""")

application = webapp2.WSGIApplication([
    ('/', Hello),
], debug=True)
