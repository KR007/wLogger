# coding=UTF-8
from flask.blueprints import Blueprint
from flask_pymongo import PyMongo
from flask import render_template,request,flash,session,current_app
from webServer.customer import ApiCorsResponse
import time,re



home = Blueprint('home',__name__)

@home.route('/',methods=['GET','POST'])
def index():
    # flash('You were successfully logged in asdasd')
    if(request.method == 'GET'):
        print(request.args.get('var1'))
        return render_template('home/index.html')

    if(request.method == 'POST'):
        var1 = request.form['username']
        var2 = request.form['password']

        return {
            'username':var1,
            'password':var2,
            'asd':'asd',
            'sdfsdf':'asdfsdfsdsd'

        }

@home.route('/get_total_ip' , methods=['GET'])
def get_total_ip():
    return current_app.driver.get_total_ip()

@home.route('/get_total_pv' , methods=['GET'])
def get_total_pv():
    return current_app.driver.get_total_pv()

@home.route('/get_request_num_by_url' , methods=['GET'])
def get_request_num_by_url():
    return current_app.driver.get_request_num_by_url()

@home.route('/get_request_urls_by_ip' , methods=['GET'])
def get_request_urls_by_ip():
    return current_app.driver.get_request_urls_by_ip()

@home.route('/get_request_num_by_ip' , methods=['GET'])
def get_request_num_by_ip():
    return current_app.driver.get_request_num_by_ip()

@home.route('/get_request_num_by_secends' , methods=['GET'])
def get_request_num_by_secends():
    return current_app.driver.get_request_num_by_secends()

@home.route('/get_pv_num_by_minute' , methods=['GET'])
def get_pv_num_by_minute():
    return current_app.driver.get_pv_num_by_minute()

@home.route('/get_ip_num_by_minute' , methods=['GET'])
def get_ip_num_by_minute():
    return current_app.driver.get_ip_num_by_minute()

@home.route('/get_request_num_by_province' , methods=['GET'])
def get_request_num_by_province():
    return current_app.driver.get_request_num_by_province()

@home.route('/get_request_num_by_status' , methods=['GET'])
def get_request_num_by_status():
    return current_app.driver.get_request_num_by_status()


@home.route('/get_request_num_by_status_code' , methods=['GET'])
def get_request_num_by_status_code():
    return current_app.driver.get_request_num_by_status_code()

@home.route('/get_spider_by_ua' , methods=['GET'])
def get_spider_by_ua():
    return current_app.driver.get_spider_by_ua()


@home.route('/get_device_type_by_ua' , methods=['GET'])
def get_device_type_by_ua():
    return current_app.driver.get_device_type_by_ua()




if __name__ == "__main__":
    pass