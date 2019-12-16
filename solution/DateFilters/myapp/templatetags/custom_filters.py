from django.template import Library, Template
from datetime import date, datetime
from random import randint


register = Library()

@register.filter
def format_dates(value):
    delta = date.today()-value
    print(delta)
    if(delta.days==0):
        result = 'Today'
    elif(delta.days==-1):
        result = 'Tomorrow'
    elif(delta.days<-1):
        result = f"{abs(delta.days)} days later"
    elif(delta.days==1):
        result = 'Yesterday'
    elif(delta.days>1):
        result = f"{abs(delta.days)} days ago"

    return result

@register.filter
def truncate(string,length):
    new_string = f"{string[:length]}..."
    return new_string
@register.simple_tag
def random():
    number = randint(0,1000)
    return number

@register.simple_tag(takes_context = True)
def shape(context, shape_type):
    if(shape_type == "rectangle"):
        return Template("""<div style='height: 100px; 
                    width:150px; 
                    background-color: green'></div>""").render(context)
    elif(shape_type == "circle"):
        return Template("""<div style='height: 100px; 
                    width: 100px; 
                    background-color: green;
                    border-radius: 50%;'></div>""").render(context)
    elif(shape_type == "triangle"):
        return Template("""<div style='height 0px; width:0px; 
                    border-left: 50px solid transparent; 
                    border-right: 50px solid transparent;
                    border-bottom: 100px solid green;
                    '></div>""").render(context)
