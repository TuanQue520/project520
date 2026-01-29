from flask import Flask

app = Flask(__name__)

# 主页 HTML
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>123</title>
        <style>
            body { 
                text-align: center; 
                margin-top: 50px; 
                font-family: Arial; 
            }
            .content-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 30px auto;
                max-width: 800px;
                gap: 30px;
            }
            .image-box {
                text-align: right;
            }
            .text-box {
                text-align: left;
            }
            .main-text {
                font-size: 28px;
                color: #333;
                line-height: 1.4;
                margin-bottom: 15px;
            }
            .btn { 
                padding: 20px 40px; 
                margin: 15px; 
                font-size: 20px; 
                cursor: pointer;
                border-radius: 10px;
                border: none;
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                transition: all 0.3s;
            }
            .btn:hover {
                background-color: #45a049;
                transform: scale(1.05);
            }
        </style>
    </head> 
    <body>
        <h1>能做朋友吗?</h1>
        
        <!-- 图片和文字并排容器 -->
        <div class="content-container">
            <div class="image-box">
                <img src="<a href="https://ibb.co/vxgTQ8VC"><img src="https://i.ibb.co/KjRfLHbc/20260129144548-97-3.jpg" alt="20260129144548-97-3" border="0"></a>" alt="123" style="width: 300px;margin: 20px 0;">
            </div>
            <div class="text-box">
                <p class="main-text">这是沈星回</p>
            </div>
        </div>
        
        <!-- 按钮区域 -->
        <div style="margin-top: 20px;">
            <button class="btn" onclick="location.href='/forgive'">可以</button>
            <button class="btn" onclick="location.href='/think'">让我再想想 🤔</button>
            <button class="btn" onclick="location.href='/more'">解释📝</button>
        </div>
    </body>
    </html>
    '''

# 可以 HTML
@app.route('/forgive')
def forgive():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>可以</title>
        <style>
            body { text-align: center; margin-top: 50px; font-family: Arial; color: green; }
            .btn { 
                padding: 20px 40px; 
                margin: 15px; 
                font-size: 20px; 
                cursor: pointer;
                border-radius: 10px;
                border: none;
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                transition: all 0.3s;
            }
            .btn:hover {
                background-color: #45a049;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <h1>🎉🎉🎉<br>(✿^‿^)</h1>
        <p>可以给我发个1表示同意吗</p >
        <button class="btn" onclick="location.href='/'">返回主页</button>
    </body>
    </html>
    '''

# 让我再想想页面 HTML
@app.route('/think')
def think():
    return '''
    <!DOCTYPE html>
<html>
<head>
    <title>让我再想想🤔</title>
    <style>
        body { text-align: center; margin-top: 50px; font-family: Arial; color: orange; }
        .btn { 
            padding: 20px 40px; 
            margin: 15px; 
            font-size: 20px; 
            cursor: pointer;
            border-radius: 10px;
            border: none;
            background-color: #ff9800;
            color: white;
            font-weight: bold;
            transition: all 0.3s;
        }
        .btn:hover {
            background-color: #e68900;
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <h1>OK</h1>
    <p>不行也没关系<br>我尊重你的选择</p >
    <button class="btn" onclick="location.href='/'">返回主页</button>
</body>
</html>
    '''

# 理由 HTML
@app.route('/more')
def more():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>理由</title>
        <style>
            body { text-align: center; margin-top: 50px; font-family: Arial; }
            .btn { 
                padding: 20px 40px; 
                margin: 15px; 
                font-size: 20px; 
                cursor: pointer;
                border-radius: 10px;
                border: none;
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                transition: all 0.3s;
            }
            .btn:hover {
                background-color: #0b7dda;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <h1>解释</h1>
        <p>我不是故意这么直接说喜欢你的<br>你问我找你有什么事<br>我怕你觉得你对我有什么误会<br>这才直接说出来<br>希望不要给你带来压力<br>无论如何都尊重你的选择</p >
        <button class="btn" onclick="location.href='/'">返回主页</button>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)