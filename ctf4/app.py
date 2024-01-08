from flask import Flask, make_response, request
from ua_parser import user_agent_parser

app = Flask(__name__)


@app.route("/")
def hello():
    site = '''<html>
<title>My Fav Browser</title>
<head>
<font size="7">
        '''

    end = '''this is not my fav browser</font><br>
</head>
</html>
'''
    end2 = '''yes but this is not my fav os</font><br>
    </head>
    </html>
    '''

    end_corr = '''yes this is my fav os also</font><br>
<p><font size="6">Since Firefox and Linux are FOSS(Fully Open Source) They Respect ur privacy hence they are my favourite </font></p>
</head>
</html>
    '''

    response = make_response(site + end)
    usragent = request.headers.get('User-Agent')
    usr_brow = user_agent_parser.ParseUserAgent(usragent)
    usr_os = user_agent_parser.ParseOS(usragent)

    print(usr_brow)
    print(usr_os)
    if usr_brow['family'] == "Firefox":
        if usr_os['family'] == "Linux" or usr_os['family'] == "Ubuntu":
            f = open("flag.txt", "r")
            flag = f.read()
            f.close()
            return site + flag + " " + end_corr
        else:
            return site + end2
    else:
        return response


if __name__ == '__main__':
    app.run(host="0.0.0.0")
