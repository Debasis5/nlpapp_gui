from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API

class NLPApp:
    def __init__(self):

        #cretae db object
        self.dbo = Database()
        self.apio = API()
        
        #login ka gui load
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.config(bg = '#34495E')

        self.login_gui()

        self.root.mainloop()

        

    def login_gui(self):

        self.clear()
        
        heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
        heading.pack(pady = (30,30))
        heading.configure(font = ('verdana', 24, 'bold'))

        label1 = Label(self.root, text = 'Email',bg = '#34495E', fg = 'white')
        label1.pack(pady = (10,10))

        self.email_input = Entry(self.root, width = 30)
        self.email_input.pack(pady = (5,10))

        label2 = Label(self.root, text = 'Password', bg = '#34495E', fg = 'white')
        label2.pack(pady = (10,10))

        self.password_input = Entry(self.root, width = 30, show = '*')
        self.password_input.pack(pady = (5,10))

        login_button = Button(self.root, text = 'Login', command=self.perform_login)
        login_button.pack(pady = (10,10))

        label3 = Label(self.root, text = 'Not a member?',bg = '#34495E', fg = 'white')
        label3.pack(pady = (30,10))

        redirect_button = Button(self.root, text = 'Register Now', command = self.register_gui)
        redirect_button.pack(pady = (10,10))

    def register_gui(self):
        # print("Register")
       self.clear()

       heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
       heading.pack(pady = (30,30))
       heading.configure(font = ('verdana', 24, 'bold'))

       label0 = Label(self.root, text = 'Enter Name',bg = '#34495E', fg = 'white')
       label0.pack(pady = (10,10))

       self.name_input = Entry(self.root, width = 30)
       self.name_input.pack(pady = (5,10))


       label1 = Label(self.root, text = 'Enter Email',bg = '#34495E', fg = 'white')
       label1.pack(pady = (10,10))

       self.email_input = Entry(self.root, width = 30)
       self.email_input.pack(pady = (5,10))

       label2 = Label(self.root, text = 'Enter Password', bg = '#34495E', fg = 'white')
       label2.pack(pady = (10,10))

       self.password_input = Entry(self.root, width = 30, show = '*')
       self.password_input.pack(pady = (5,10))

       register_button = Button(self.root, text = 'Register', command=self.perform_registration)
       register_button.pack(pady = (10,10))

       label3 = Label(self.root, text = 'Already a member?',bg = '#34495E', fg = 'white')
       label3.pack(pady = (30,10))

       redirect_button = Button(self.root, text = 'Login Now', command = self.login_gui)
       redirect_button.pack(pady = (10,10))

    def clear(self):
         
         #clear existing gui
         for i in self.root.pack_slaves():
            print(i.destroy())

    def perform_registration(self):
        # fetch data from GUI
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo('success', 'Registration successful' )
            # print('Registration successful')
        
        else:
            messagebox.showerror('error', 'Email already exists' )
            # print('User exists')

    def perform_login(self):

        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.serach(email,password)

        if response:
            messagebox.showinfo('success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('error', 'Incorrect credentials')

    def home_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
        heading.pack(pady = (30,30))
        heading.configure(font = ('verdana', 24, 'bold'))
        
        sentiment_button = Button(self.root, text = 'Sentiment Analysis', width=20, height=4, command=self.sentiment_gui)
        sentiment_button.pack(pady = (10,10))

        
        ner_button = Button(self.root, text = 'Named Entity Recognition', width=20, height=4,command=self.ner_gui)
        ner_button.pack(pady = (10,10))
        
        
        emotion_button = Button(self.root, text = 'Emotion Prediction',width=20, height=4, command=self.emotion_gui)
        emotion_button.pack(pady = (10,10))

        logout_button = Button(self.root, text = 'Logout', command = self.login_gui)
        logout_button.pack(pady = (50,10))

    def sentiment_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
        heading.pack(pady = (30,30))
        heading.configure(font = ('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis', bg = '#34495E', fg = 'white')
        heading2.pack(pady = (10,20))
        heading2.configure(font = ('verdana', 20))

        label1 = Label(self.root, text = 'Enter Text',bg = '#34495E', fg = 'white')
        label1.pack(pady = (10,10))

        self.sentiment_input = Entry(self.root, width = 50)
        self.sentiment_input.pack(pady = (5,10))

        sentiment_button = Button(self.root, text = 'Analyse Sentiment', command = self.do_sentiment_analysis)
        sentiment_button.pack(pady = (50,10))

        self.sentiment_result = Label(self.root, text = '',bg = '#34495E', fg = 'white')
        self.sentiment_result.pack(pady = (5,5))
        self.sentiment_result.configure(font = ('verdana', 20))

        goback_button = Button(self.root, text = 'GO BACK', command = self.home_gui)
        goback_button.pack(pady = (20,10))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
                txt = txt + i + '>' + str(result['sentiment'][i]) + '\n'

        self.sentiment_result['text'] = txt

    def ner_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
        heading.pack(pady = (30,30))
        heading.configure(font = ('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Named Entity Recognition', bg = '#34495E', fg = 'white')
        heading2.pack(pady = (10,20))
        heading2.configure(font = ('verdana', 20))

        label1 = Label(self.root, text = 'Enter Text',bg = '#34495E', fg = 'white')
        label1.pack(pady = (10,10))

        self.ner_input = Entry(self.root, width = 50)
        self.ner_input.pack(pady = (5,10))

        ner_button = Button(self.root, text = 'NER', command = self.do_ner_analysis)
        ner_button.pack(pady = (50,10))

        self.ner_result = Label(self.root, text = '',bg = '#34495E', fg = 'white')
        self.ner_result.pack(pady = (5,5))
        self.ner_result.configure(font = ('verdana', 20))

        goback_button = Button(self.root, text = 'GO BACK', command = self.home_gui)
        goback_button.pack(pady = (20,10))

    def do_ner_analysis(self):

        text = self.ner_input.get()
        result = self.apio.ner_analysis(text)

        # txt = ''
        print(result)
        # for i in result['entities']:
        #         txt = txt + i + '>' + str(result['entities'][i]) + '\n'

        self.ner_result['text'] = result

    def emotion_gui(self):

        self.clear()

        heading = Label(self.root, text='NLPApp', bg = '#34495E', fg = 'white')
        heading.pack(pady = (30,30))
        heading.configure(font = ('verdana', 24, 'bold'))

        heading2 = Label(self.root, text='Emotion Prediction', bg = '#34495E', fg = 'white')
        heading2.pack(pady = (10,20))
        heading2.configure(font = ('verdana', 20))

        label1 = Label(self.root, text = 'Enter Text',bg = '#34495E', fg = 'white')
        label1.pack(pady = (10,10))

        self.emotion_input = Entry(self.root, width = 50)
        self.emotion_input.pack(pady = (5,10))

        emotion_button = Button(self.root, text = 'Predict Emotion', command = self.do_emotion_prediction)
        emotion_button.pack(pady = (50,10))

        self.emotion_result = Label(self.root, text = '',bg = '#34495E', fg = 'white')
        self.emotion_result.pack(pady = (5,5))
        self.emotion_result.configure(font = ('verdana', 20))

        goback_button = Button(self.root, text = 'GO BACK', command = self.home_gui)
        goback_button.pack(pady = (20,10))

    def do_emotion_prediction(self):

        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)

        
        print(result)
        txt = ''
        for i in result['emotion']:
                txt = txt + i + '>' + str(result['emotion'][i]) + '\n'

        self.emotion_result['text'] = txt



nlp = NLPApp()
