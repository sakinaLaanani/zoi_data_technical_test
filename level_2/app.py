from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from utils import parse_string_to_json

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://zoi_user:zoi_user_pswd@db:5432/zoi_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)

class Member(db.Model):
    __tablename__ = 'member'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    sex = db.Column(db.Integer)
    age = db.Column(db.Integer)
    default_language_en = db.Column(db.Boolean)
    waiting_list_time = db.Column(db.Float)
    black_and_white_design = db.Column(db.Boolean)
    follow_reco = db.Column(db.Float)
    follow_reco_above_50p = db.Column(db.Boolean)

@app.route('/')
def main_page():
    return '<h1>Hello Zoi</h1>'

@app.route('/member', methods=['POST'])
def create_member():
    new_member = request.get_json() 
    json_member = parse_string_to_json(new_member['member'])
    member_received = Member(member_id=json_member['id'], created_at=json_member['created_at'], sex=json_member['sex'], age=json_member['age'], default_language_en=json_member['default_language_en'], waiting_list_time=json_member['waiting_list_time'], black_and_white_design=json_member['black_and_white_design'], follow_reco=json_member['follow_reco'], follow_reco_above_50p=json_member['follow_reco_above_50p'])
    
    db.session.add(member_received)
    db.session.commit()
    return ''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')