"""
Routes and views for the bottle application.
"""

from bottle import route, view, request, redirect, post
from datetime import datetime
from connection import coll
from bson.objectid import ObjectId



@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    result = coll.find()
    result = list(result);
    for b in result:
        if b["post_tags"] != None and len(b["post_tags"]) >0 :
            b["post_tags"] = ', '.join(b["post_tags"])
    return dict(
        blogs = list(result)
    )

@route('/add')
@view('add')
def add():
    """Renders the contact page."""
    return dict(
    )

@post('/add_blog')
def add_blog():
    title =request.forms.get('txtTitle')
    date = datetime.now()
    content = request.forms.get('txtContent')
    tags = request.forms.getall('txtTags')
    b = dict(
        post_date = date,
        post_title = title,
        post_text = content,
        post_tags = tags
        )
    coll.insert_one(b);
    redirect('/')


@route ('/delete/<bID>')
def delete_blog(bID):
    objID = ObjectId(bID)
    delete_result = coll.delete_one({"_id":objID})
    redirect('/')




@route('/find/<bID>')
@view('edit')
def show_blog(bID):
    b_doc = coll.find_one({"_id":ObjectId(bID)})
    return dict(
       blog = b_doc
    )

@post('/edit_blog')
def update_blog_doc():
    title = request.forms.get('txtTitle')
    date = datetime.now()
    text = request.forms.get('txtText')
    id = request.forms.get('txtID')
    tags = request.forms.getall('txtTags')

    update_result = coll.update_one(
                                        {"_id": ObjectId(id)},
                                        {"$set":{"post_title":title, "post_date":date,"post_tags":tags}}
                                    )
    redirect('/')

@route('/search')
@view('search')
def search():
    return dict(
        blogs = []
        )

@post('/search_blog')
@view('search')
def search_blog():
    title = request.forms.get("txtTitle")
    context = request.forms.get("txtContent")
    tag = request.forms.get("txtTag")

    result = list(coll.find({"post_title": {'$regex':".*" + title + ".*", "$options": "-i"},"post_text": {'$regex':".*" + context + ".*", "$options": "-i"},"post_tags": {'$regex':".*" + tag + ".*", "$options": "-i"}}))
    for b in result:
        if b["post_tags"] != None and len(b["post_tags"]) >0 :
            b["post_tags"] = ', '.join(b["post_tags"])
    return dict(
            blogs = result
    )
