import io
import sys

from app import app

class TestApp:
    '''Flask application in flask_app.py'''

    def test_index_route(self):
        '''has a resource available at "/".'''
        response = app.test_client().get('/')
        assert(response.status_code == 200)

    def test_index_text(self):
        '''displays "Python Operations with Flask Routing and Views" in h1 in browser.'''
        response = app.test_client().get('/')
        assert(response.data.decode() == '<h1>Python Operations with Flask Routing and Views</h1>')

    def test_greet_route(self):
        '''has a resource available at "'/greet/<string:name>'".'''
        response = app.test_client().get('/greet/someone')
        assert(response.status_code == 200)

    def test_print_text(self):
        '''displays greeting in a paragraph.'''
        response = app.test_client().get('/greet/Jie')
        assert(response.data.decode() == '<p>Welcome Jie!</p>')

    def test_count_route(self):
        '''has a resource available at "/count/<int:num>".'''
        response = app.test_client().get('/count/5')
        assert(response.status_code == 200)

    def test_count_range_10(self):
        '''response is unordered list through range of parameter in "/count/<int:num>".'''
        response = app.test_client().get('/count/4')
        count = '<ul><li>0</li><li>1</li><li>2</li><li>3</li></ul>'
        assert(response.data.decode() == count)

    def test_math_route(self):
        '''has a resource available at "/math/<int:num1>/<string:op>/<int:num2>".'''
        response = app.test_client().get('/math/5/+/4')
        assert(response.status_code == 200)

    def test_math_add(self):
        '''adds parameters in "/math/" resource when operation is "+".'''
        response = app.test_client().get('/math/5/+/4')
        assert(response.data.decode() == '<h2>5+4=9</h2>')

    def test_math_subtract(self):
        '''subtracts parameters in "/math/" resource when operation is "-".'''
        response = app.test_client().get('/math/5/-/4')
        assert(response.data.decode() == '<h2>5-4=1</h2>')

    def test_math_multiply(self):
        '''multiplies parameters in "/math/" resource when operation is "*".'''
        response = app.test_client().get('/math/5/*/4')
        assert(response.data.decode() == '<h2>5*4=20</h2>')

    def test_math_divide(self):
        '''divides parameters in "/math/" resource when operation is "div".'''
        response = app.test_client().get('/math/8/div/4')
        assert(response.data.decode() == '<h2>8div4=2.0</h2>')
    
    def test_math_modulo(self):
        '''finds remainder of parameters in "/math/" resource when operation is "%".'''
        response = app.test_client().get('/math/17/%/5')
        assert(response.data.decode() == '<h2>17%5=2</h2>')
        
    def test_math_unknown_op(self):
        '''Returns error message for unknown operator'''
        response = app.test_client().get('/math/7/@/5')
        assert(response.data.decode() == '<p>Operation not recognized.</p>')