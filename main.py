from flask import Flask,render_template,request,redirect,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from forms import item_form

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///marketitems.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']='e1aa50307cda2a3ca8a976a4'

db=SQLAlchemy(app)

class Market(db.Model):
    id=db.Column(db.Integer(), primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    supplier=db.Column(db.String(30),nullable=False)
    description=db.Column(db.String(1024),nullable=False)
    price=db.Column(db.Integer(),nullable=False)
    url=db.Column(db.String(4000),nullable=False)
    def __repr__(self)-> str:
        return f'{self.name} : {self.price}'

@app.route('/') #decorator
def home_page():
    items=Market.query.all()
    return render_template('index.html',items=items)

@app.route('/additems',methods=['GET','POST'])
def add_item():
    form = item_form(request.form)
    if form.validate_on_submit():
        item1=Market(name=form.name.data,supplier=form.supplier.data,description=form.description.data,price=form.price.data,url=form.url.data)
        db.session.add(item1)
        db.session.commit()
        flash('the data was successfully entered',category='success')
        return redirect("/")
    if form.errors != {}:
        for errors in form.errors.values():
            flash(errors,category='danger')
        return redirect('/')
    return render_template('additems.html',form=form)


@app.route('/delete/<int:num>')
def delete(num):
    item=Market.query.filter_by(id=num).first()
    db.session.delete(item)
    db.session.commit()
    flash('item was successfully deleted','danger')
    return redirect(url_for('home_page'))
    
@app.route('/update/<int:num>', methods=['GET','POST'])
def update(num):

    if request.method=='POST':
        u_name=request.form['name']
        u_supplier=request.form['supplier']
        u_des=request.form['description']
        u_price=request.form['price']
        u_url=request.form['url']
        item=Market.query.filter_by(id=num).first()
        item.name=u_name
        item.supplier=u_supplier
        item.description=u_des
        item.price=u_price
        item.url=u_url
        db.session.add(item)
        db.session.commit()
        flash(f'Item with number {item.id} has been updated',category='info')
        return redirect('/')

    item=Market.query.filter_by(id=num).first()
    return render_template('update.html',item=item)

@app.route('/about')
def about():
    items=Market.query.all()
    return render_template('about.html',items=items)

if __name__=="__main__":
    app.run(debug=True , port=8000)