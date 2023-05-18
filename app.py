# This is just test file.

from flask import *
import json, time
import random as rand # Yes, I knew what I was doing :)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data_set = {'Page': 'Home', 'Message': "Success on home", 'Time': current_time}
    json_dump = json.dumps(data_set)

    return json_dump


@app.route('/quote/', methods=['GET'])
def get_quote():

    quotes = ["I'm not superstitious, but I am a little stitious.",
    "I talk a lot, so I've learned to tune myself out.",
    "Sometimes I'll start a sentence and I don't even know where it's going. I just hope I find it along the way.",
    "I'm not offended by homosexuality. In the 60s, I made love to many, many women, often outdoors, in the mud and the rain. It's possible a man could've slipped in there. There'd be no way of knowing.",
    "I am Beyoncé always.",
    "I love inside jokes. I'd love to be a part of one someday.",
    "I'm not a hero. I'm a high-functioning sociopath.",
    "I wish there was a way to know you're in the good old days before you've actually left them.",
    "I'm an early bird and I'm a night owl. So I'm wise and I have worms.",
    "I'm not ashamed to say that I'm a proud owner of a Dundie award.",
    "Sometimes you have to take a break from being the kind of boss that's always trying to teach people things. Sometimes you just have to be the boss of dancing.",
    "I'm a deer hunter. I go all the time with my dad. One thing about deer, they have very good vision. One thing about me, I am better at hiding than they are...at vision.",
    "Well, well, well, how the turntables...",
    "I am running away from my responsibilities and it feels good.",
    "I am not a millionaire. But I would like to be one day. And if I had a million dollars, I would invest half of it in glorious mutual funds and take the other half over to my friend Asadulah who works in securities.",
    "I am not to be truffled with.",
    "I am running away from my responsibilities. And it feels good.",
    "I enjoy having breakfast in bed. I like waking up to the smell of bacon, sue me. And since I don't have a butler, I have to do it myself. So, most nights before I go to bed, I will lay six strips of bacon out on my George Foreman grill. Then I go to sleep. When I wake up, I plug in the grill. I go back to sleep again. Then I wake up to the smell of crackling bacon. It is delicious, it's good for me, it's the perfect way to start the day.",
    "There are a lot of beauty contests out there, but only one that counts. And that is the one that I am going to win.",
    "You know what they say. 'Fool me once, strike one, but fool me twice... strike three.'",
    "You know what they say about a car wreck, where it's so awful you can't look away? The Dundies are like a car wreck that you want to look away from but you have to stare at it because your boss is making you.",
    "Webster's Dictionary defines 'wedding' as 'the fusing of two metals with a hot torch.' Well, you know something? I think you guys are two medals. Gold medals.",
    "Would I rather be feared or loved? Easy. Both. I want people to be afraid of how much they love me.",
    "I'm not a hero. I put my bra on one boob at a time like everyone else.",
    "I would not miss it for the world"]

    index = rand.randint(0,30)

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    data_set = {'Page': 'Quote', 'Message': "Successfully landed on quotes page", 'quote': f'{quotes[index]}', 'Time': current_time}
    
    json_dump = json.dumps(data_set)
    return json_dump

@app.route('/user/', methods=['GET'])
def user_page():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    user_query = str(request.args.get('user'))
    data_set = {'Page': 'Request', 'Message': f"Success on User for {user_query}", 'Time': current_time}
    json_dump = json.dumps(data_set)

    return json_dump

if __name__ == '__main__':
    app.run(port=5600)
