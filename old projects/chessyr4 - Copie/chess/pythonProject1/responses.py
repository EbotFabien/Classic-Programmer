from datetime import datetime
from datetime import date
import  Film as fi 

def sample_responses(input_text,token,name):
    print('ok')
    user_message = str(input_text).lower()
    bot=fi.Bot.query.filter_by(token=token).first()
    bot_responses=list(fi.Bot_data.query.filter_by(bot=bot.id).all())
   
    for i in bot_responses:
        if i.question.lower() in user_message:
            res=fi.Bot_responses(bot=bot.id,botresponse=i.response,user_name=name)
            fi.db.session.add(res)
            fi.db.session.commit()
            return i.response
    res=fi.Bot_responses(bot=bot.id,user_message=user_message,botresponse="Im sorry. I dont understand",user_name=name)
    fi.db.session.add(res)
    fi.db.session.commit()
    return "I'm sorry. I don't understand"


    ''' 
  if "hi" in user_message or "hey" in user_message or "hello" in user_message:
        return "Hey how are you?"

    if "and you" in user_message or "nd u" in user_message:
        return "I'm okay thanks"

    if "good morning" in user_message:
        return "Good morning"

    if "date" in user_message or "date?" in user_message:
        today = date.today()
        return "Today is " + str(today)

    if "time?" in user_message:
        now = datetime.now()
        date_time = now.strftime("%H:%M")
        return "The time is "+str(date_time)

    else:
        return "I'm sorry. I don't understand"

     myresponses = {
        'hi': greeting,
        'hey': greeting,
        'and you': "I'm okay thanks",
        'good morning': 'Good morning',
        'Good Evening': 'Good evening',
        'date': str(date.today()),
        'time': str(datetime.now().strftime("%H:%M"))
    }
    '''

