from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user, user_logged_in
from .models import renting, rentingadmin
from . import db
import base64, uuid
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)

@views.route('/')
def welcome():
    if user_logged_in == "logged-in":
        return redirect(url_for('views.home'))
    else:
        return render_template('welcome.html', user=current_user)
    
@views.route('/home')
@login_required
def home():
    
    return render_template('home.html', user=current_user)

@views.route('/categories')
@login_required
def categories():
    images=rentingadmin.image1()
    
    return render_template('categories.html', user=current_user, images=images)

@views.route('/list', methods=['GET', 'POST'])
@login_required
def list():
    if request.method == 'POST':
        renter = request.form.get('renter')
        phone = request.form.get('phone')
        address = request.form.get('address')
        category = request.form.get('category')
        item_name = request.form.get('item_name')
        item_desc = request.form.get('item_desc')
        price = request.form.get('price')
        security_depo = request.form.get('security_depo')

        item_image1 = request.files['item-image1']
        item_image2 = request.files['item-image2']
        item_image3 = request.files['item-image3']
        item_image4 = request.files['item-image4']

        image1_name = secure_filename(item_image1.filename)
        image1_uuid = str(uuid.uuid1()) + '_' + image1_name
        image2_name = secure_filename(item_image2.filename)
        image2_uuid = str(uuid.uuid1()) + '_' + image2_name
        image3_name = secure_filename(item_image3.filename)
        image3_uuid = str(uuid.uuid1()) + '_' + image3_name
        image4_name = secure_filename(item_image4.filename)
        image4_uuid = str(uuid.uuid1()) + '_' + image4_name

        image1_type = item_image1.mimetype
        image2_type = item_image2.mimetype
        image3_type = item_image3.mimetype
        image4_type = item_image4.mimetype

            

        if len(phone) > 10:
            flash('phone number incorrect, please try again', category='error')
        else:
            
            new_item = renting(renter=renter, 
                               phone=phone, 
                               address=address, 
                               category=category, 
                               item_name=item_name, 
                               item_desc=item_desc, 
                               item_price=price, 
                               image1=item_image1.read(),
                               image1_name=image1_uuid,
                               image1_type=image1_type,
                               image2=item_image2.read(),
                               image2_name=image2_uuid,
                               image2_type=image2_type,
                               image3=item_image3.read(),
                               image3_name=image3_uuid,
                               image3_type=image3_type,
                               image4=item_image4.read(),
                               image4_name=image4_uuid,
                               image4_type=image4_type,
                               security_depo = security_depo
                               )
            db.session.add(new_item)
            db.session.commit()
            flash('item added successfully!')
            return redirect(url_for('views.itemadded'))

    return render_template('list.html', user=current_user)

@views.route('/item-added')
@login_required
def itemadded():
    return render_template('item-added.html', user=current_user)




