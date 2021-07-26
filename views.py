from django.shortcuts import render, redirect
from django.contrib import messages
import pickle

with open('svmModel2.pkl', 'rb') as file:
    svmModel = pickle.load(file)

with open('tf2.pkl', 'rb') as file:
    tf = pickle.load(file)

def index(request):
    return render(request, 'index.html')

def giveMePredictionsBudyy(comment):

    review_vector = tf.transform([comment])
    pred =  svmModel.predict(review_vector)
    return pred
def predict(request):
    if(request.method == "POST"):
        comment = request.POST.get('myComment')

        pred = giveMePredictionsBudyy(comment)
        if pred==['pos'] :
            messages.success(request, "Positive")
        elif pred==['neg'] :
            messages.success(request, "Negative")
        else:
            messages.success(request, "Please phrase the message again!")

    return redirect('/')
