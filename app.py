from flask import Flask,render_template,request,redirect

app=Flask(__name__)

#route() decorators
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')
 
@app.route('/send_guess/',methods=['POST'])
def send():
#     #Getting form data from the web form
    guess=request.form['guess']
#     email=request.form['email']
#     subject=request.form['subject']
#     message=request.form['message']


#     BODY = '\r\n'.join(['To: %s' % TO,
#                         'From: %s' % gmail_sender,
#                         'Subject: %s' % SUBJECT,
#                         '', TEXT])
#     try:
#         server.sendmail(gmail_sender, [TO], BODY)
#     except:
#         print('error sending mail')
    
#     server.quit()
#     #Notification of email sending
    return redirect('/index.html')

if __name__=='__main__':
    app.run(debug=True)