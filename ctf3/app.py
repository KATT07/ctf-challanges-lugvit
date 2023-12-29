from flask import Flask, make_response, request

app = Flask(__name__)

@app.route("/")
def hello():
    site = '''
<html>
<title>My Blog Website</title>
<head>
<font size="7">Here are some different types of cookies:</font><br>
</head>
<body>
<p><font size="6">1. Chocolate Chip Cookies</font></p>
<p><img src="/static/Chocolate-Chip-Cookies-min-300x239.jpg"></p>
<p><font size="5">Chocolate chip cookies are the perennial classic and longtime fan favorite. They can be soft and chewy or crispy and crunchy depending on how you make them and the ingredients you use. Either way, they’re completely delicious.</font> </p> <br>
<p><font size="6">2. Shortbread Cookies</font></p>
<p><img src="/static/Shortbread-Cookies-min-300x200.jpg"></p>
<p><font size="5">Shortbread cookies are made with a large amount of butter or shortening, which lends them the name “short.” Due to their low amount of flour and sugar, they have a classic crumbly and tender texture.</font></p> <br>
<p><font size="6">3. Macaron Cookies</font></p>
<p><img src="/static/Macaron-Cookies-min-300x180.jpg"></p>
<p><font size="5">Macarons are meringue-based cookies made with almond meal, egg whites, and powdered sugar with a creme ganache in the middle. The cookie shell features a delicate outer crust that houses a chewy meringue texture inside.</font></p> <br>
<p><font size="6">4. Macaroon Cookies</font></p>
<p><img src="/static/Macaroon-Cookies-min-467x420.jpg"></p>
<p><font size="5">Quite different from macarons, macaroons are coconut based with a dense, lumpy texture that’s sweet and chewy. Some macaroons are even dipped in chocolate for extra indulgence.</font></p> <br>
<p><font size="6">5. Biscotti Cookies</font></p>
<p><img src="/static/Biscotti-Cookies-min-300x200.jpg"></p>
<p><font size="5">Biscotti actually means “twice baked” and the cookie is indeed baked twice, resulting in its hard and crunchy texture. Biscotti come in a wide array of flavors and toppings, from plain almond to double chocolate and so much more.</font></p> <br>
<p><font size="6">6. Sugar Cookies</font></p>
<p><img src="/static/Sugar-Cookies-min-300x200.jpg"></p>
<p><font size="5">Made with basic ingredients, such as sugar, flour, butter, and vanilla, sugar cookies are easy to make and insanely popular. They’re typically made by rolling out the dough and cutting into shapes before decorating with icing, sprinkles, or colored sugar.</font></p> <br>
<p><font size="6">7. Oatmeal Raisin Cookies</font></p>
<p><img src="/static/Oatmeal-Raisin-Cookies-min-300x200.jpg"></p>
<p><font size="5">Oatmeal raisin is a type of drop cookie. as its name suggests, it’s made with oats, and contains raisins and brown sugar. They can be crispy and crunchy or chewy, depending on the ingredients you use and how long you bake them.</font></p> <br>
<p><font size="6">8. Gingerbread Cookies</font></p>
<p><img src="/static/Gingerbread-Cookies-min-300x200.jpg"></p>
<p><font size="5">Gingerbread cookies are the ultimate holiday cookie. They’re made with spices galore, including cinnamon, ginger, nutmeg, and molasses, and are made by rolling out the dough and cutting into shapes.</font></p> <br>
<p><font size="6">9. Snickerdoodle Cookies</font></p>
<p><img src="/static/Snickerdoodle-Cookies-min-300x200.jpg"></p>
<p><font size="5">Snickerdoodles are made with butter, sugar, and flour with cream of tartar and baking soda added into the dough to make it rise slightly. They’re known by their cracked surface that’s coated in cinnamon and sugar.</font></p> <br>
<p><font size="6">10. Fortune Cookies</font></p>
<p><img src="/static/Fortune-Cookies-min-300x203.jpg"></p>
<p><font size="5">Fortune cookies are mostly known as the type of cookie that comes with Chinese takeout. They’re made with flour, sugar, vanilla, and just a hint of sesame oil and are shaped into their classic crescent shape while the dough is still hot from the oven.</font></p> <br>
</body>
</html>
        '''
    response = make_response(site)
    cookie = request.cookies.get("howmany")
    response.set_cookie("howmany", "0")
    print("cookie is set to " + str(cookie))
    if cookie == "10":
        f=open("flag.txt","r")
        flag=f.read()
        f.close()
        return flag
    else:
        return response

if __name__ == '__main__':
    app.run(host="0.0.0.0")
