from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/robots.txt")
def hint():
    return "Use the user-agent of the linux mascot"

@app.route("/")
def hello():
    site = '''<html>
<title>Why Linux is the best OS</title>
<head>
<font size="7"><u>So Linux is considered the best OS by many. Lets see 5 reasons why</u></font>
</head>
<body>
<p><img src="/static/penguin.png" alt="Penguin pic"></p>
<p><font size="6">1. Open Source Nature<p>
<p>What is it like when you buy a car, but you cannot see what’s under the hood? Similar is the case with when you use a Windows-powered system. However, in contrast, Linux is completely an open source project. You can have a look at the source code of a Linux OS, which is a plus.</p>
<p>2. Secure</p>
<p>Let’s face it; Windows OS is vulnerable to different types of attacks (or hacks). However, Linux is not as vulnerable as Windows. It sure isn’t invulnerable, but it is a lot more secure. Although, there’s no rocket science in it. It is just the way Linux works that makes it a secure operating system. Overall, the process of package management, the concept of repositories, and a couple more features makes it possible for Linux to be more secure than Windows.</p>
<p>3. Customization</p>
<p>One major advantage of using Linux instead of Windows is customization. If you like tweaking your system’s looks, Linux is just perfect for you. Apart from installing themes, you have tons of beautiful icon themes. In addition to that, you can use Conky to display system information on the desktop in the coolest way possible. Needless to say that you can do a lot around Wallpapers in Linux.</p>
<p>4. Free to Use</p>
<p>Linux is accessible to the public for free! However, that is not the case with Windows! You will not have to pay 100-250 USD to get your hands on a genuine copy of a Linux distro (such as Ubuntu, Fedora). So, it is entirely free.</p>
<p>5. Reliability</p>
<p>Windows, as we know it, becomes sluggish day after day. You will want to re-install Windows after a while when you encounter crashes or slowdowns on your system. If you are using Linux, you will not have to worry about re-installing it just to experience a faster and a smoother system. Linux helps your system run smooth for a longer period (in fact, much longer!).</font></p>
<body>
</html>
        '''

    response = make_response(site)
    usragent = str(request.headers.get('User-Agent'))

    print(usragent)

    if usragent == "tux":
        f=open("flag.txt","r")
        flag=f.read()
        f.close()
        return flag
    else:
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")
