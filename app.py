from flask import Flask, render_template
from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from sqlalchemy import Table, MetaData


app = Flask(__name__)
ENGINE = create_engine("sqlite:///sample.sqlite3") #connect DB
Base = declarative_base() #DBテーブルをpythonオブジェクトにマップする

class DB(Base):
    __tablename__ = "todo"
    todo = Column(String(255))
    complete = Column(Integer)
    id = Column(Integer, primary_key=True)
    def toDict(self):
        return {
            'todo': str(self.todo),
            'complete':int(self.complete),
            'id':int(self.id)
        }
def getDataBase(clss, filter=False):
    Session = sessionmaker(bind=ENGINE)
    ses = Session()
    if filter != False:
        res = ses.query(clss).filter(clss.category_name==filter).all()
    else:
        res = ses.query(clss).all()
    ses.close()
    List = []
    for item in res:
        Dict = item.toDict() #DBオブジェクトを辞書型に変換
        #List.append([Dict["id"], Dict["todo"]])
        List.append(Dict)
    return List


@app.route('/')
def index():
    db = getDataBase(clss=DB)
    #complete==0のものだけのリストとcomplete==1のものだけのリスト
    print(db)
    return render_template('index.html', data=db)

@app.route('/change', methods=["POST"])
def ajax():
    print('ajax')
    todo = request.form.get('todo')
    comp = request.form.get('complete')
    id = request.form.get('id')
    if comp==str(0):
        comp = str(1)
    else:
        comp = str(0)
    print(f"{todo}, {comp}")
    #dbの更新(compの更新)
    Session = sessionmaker(bind=ENGINE)
    ses = Session()
    mydata = ses.query(DB).filter(DB.id==int(id)).one()
    mydata.complete = int(comp)
    ses.add(mydata)
    ses.commit()
    ses.close()

    db = getDataBase(clss=DB)
    print(db)
    return jsonify(db)

@app.route('/add', methods=["POST"])
def add():
    todo = request.form.get('todo')
    comp = request.form.get('complete')
    mydata = DB(todo=todo, complete=comp)
    Session = sessionmaker(bind=ENGINE)
    ses = Session()
    ses.add(mydata)
    ses.commit()
    ses.close()
    #更新後のdb
    db = getDataBase(clss=DB)
    print(db)
    return jsonify(db)

@app.route('/delete', methods=['POST'])
def delete():
    id = request.form.get('id')
    Session = sessionmaker(bind=ENGINE)
    ses = Session()
    data = ses.query(DB).filter(DB.id==str(id)).one()
    ses.delete(data)
    ses.commit()
    ses.close()

    db = getDataBase(clss=DB)
    return jsonify(db)

if __name__=='__main__':
    app.run(debug=True)