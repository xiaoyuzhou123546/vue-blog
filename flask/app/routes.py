from app import app
from flask import Flask, jsonify, abort, request
from flask_pymongo import PyMongo
from flask_restful import Api, Resource
import bson,time,os
from flask_uploads import UploadSet, configure_uploads, IMAGES,patch_request_class
app.config['MONGO_DBNAME'] = 'blog'
app.config['MONGO_URI']='mongodb://139.199.23.12/blog'
mongo = PyMongo(app).db
api = Api(app)


app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()+"/app/templates/images"  # 文件储存地址
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # 文件大小限制，默认为16MB


import random
import string
def generate_random_str():    
    '''    
    string.digits = 0123456789    
    string.ascii_letters = 26个小写,26个大写    
    '''    
    str_list = random.sample(string.digits + string.ascii_letters,20)    				
    random_str = ''.join(str_list)    
    return random_str


# 用户处理
class UserList(Resource):
	def get(self):
		start = mongo.login.find()
		output = []
		for s in start:
			s.pop('_id')
			output.append(s)
		return dict(result=output)

	# def post(self):
 #        user_id = int(max(USER_LIST.keys())) + 1
 #        user_id = '%i' % user_id
 #        USER_LIST[user_id] = {'name': request.form['name']}
 #        return USER_LIST[user_id]


# 博客列表处理
class BlogList(Resource):
	def get(self):
		blogs = mongo.blogContent.find()
		output = []
		for blog in blogs:
			blog.pop('_id')
			output.append(blog)
		return dict(result=output)
	def post(self):
		blogdata = request.get_json()
		blog_count = mongo.blogContent.count()
		defaultdata = {
			'addtime':time.time(),
			'exittime':time.time(),
			'see':0,
			'assist':0,
			'blog_id':blog_count
		}
		mongo.blogContent.insert_one(dict(blogdata,**defaultdata))
		return dict(result=dict(blogdata,**defaultdata))
# 博客内容
class BlogDetail(Resource):
	def get(self):
		id = int(request.args.get("id"))
		blog = mongo.blogContent.find_one({'blog_id':id})
		blog.pop("_id")
		return dict(result=blog)
#上传文件
class UploadFile(Resource):
	def post(self):
		suffix = os.path.splitext(request.files['photo'].filename)[1]
		filename = generate_random_str() + suffix
		photos.save(request.files['photo'], name=filename)
		file_url = photos.url(filename)
		return dict(result=file_url)

api.add_resource(UserList,'/')
api.add_resource(BlogList,'/blog')
api.add_resource(BlogDetail,'/blogdetail')
api.add_resource(UploadFile,'/uploadfile')