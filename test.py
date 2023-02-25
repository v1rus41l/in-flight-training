from flask import Flask, url_for, request, render_template
import json

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Ученик Яндекс.Лицея"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)

@app.route('/queue')
def queue():
    return render_template('queue.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/training/<prof>', methods=['GET', 'POST'])
def training(prof):
    return render_template('index.html', prof=prof)

@app.route('/list_prof/<list>', methods=['GET', 'POST'])
def list_prof(list):
    professions = ['инженер-исследователь',
                   'пилот',
                   'строитель',
                   'экзобиолог',
                   'врач',
                   'инженер по терраформированию',
                   'климатолог',
                   'специалист по радиационной защите',
                   'астрогеолог',
                   'гляциолог',
                   'инженер',
                   'инженер жизнеобеспечения',
                   'метеоролог',
                   'оператор марсохода',
                   'киберинженер',
                   'штурман',
                   'пилот дронов']
    return render_template('professions.html', list=list, professions=professions)

@app.route('/answer')
@app.route('/auto_answer')
def auto_answer():
    profile = {}
    profile['surname'] = "Whatny"
    profile['name'] = "Pit"
    profile['education'] = "High School"
    profile['profession'] = "штурман"
    profile['sex'] = "Male"
    profile['motivation'] = "None"
    profile['ready'] = "True"
    return render_template('answer.html', title='Анкета', **profile)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')