from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    """关于页面"""
    return '''
    <h1>关于我们</h1>
    <p>这是一个基础的 Flask 应用示例</p>
    <a href="/">返回首页</a>
    '''

@app.route('/user/<username>')
def show_user(username):
    """显示用户信息的动态路由"""
    return f'<h1>用户: {username}</h1><p>欢迎访问你的个人页面！</p>'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    """显示文章的动态路由，使用整数类型"""
    return f'<h1>文章 ID: {post_id}</h1><p>这是第 {post_id} 篇文章</p>'

@app.route('/api/data')
def get_data():
    """返回 JSON 数据的 API 端点"""
    data = {
        'status': 'success',
        'message': '数据获取成功',
        'data': {
            'items': ['项目1', '项目2', '项目3'],
            'count': 3
        }
    }
    return jsonify(data)

@app.route('/greet')
def greet():
    """从查询参数获取名字并问候"""
    name = request.args.get('name', '访客')
    return f'<h1>你好，{name}！</h1>'

@app.errorhandler(404)
def page_not_found(error):
    """404 错误处理"""
    return '<h1>404 - 页面未找到</h1><p>抱歉，您访问的页面不存在。</p><a href="/">返回首页</a>', 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=55000)
