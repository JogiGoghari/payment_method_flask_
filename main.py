import os
from flask import Flask, jsonify, request ,render_template, redirect
# Import datetime class from datetime module
from datetime import datetime

app = Flask(__name__,
            static_url_path='',
            static_folder='.')
YOUR_DOMAIN = 'http://localhost:4242'

@app.route("/payment", methods=["GET", "POST"])
def payment():

    if request.method == "POST":
        req = request.form
        print(req)
        print(req["amount"])
        x = int(req["amount"])

        if x < 20 :
            print("Chep payment")
            return redirect(YOUR_DOMAIN + "/checkout1")
        elif 21 < x < 500 :
            print("exclu payment")
            return redirect(YOUR_DOMAIN + "/checkout2")
        else:
            print("Premi payment")
            return redirect(YOUR_DOMAIN + "/checkout3")

    return render_template("payment.html")

@app.route("/checkout1", methods=["GET", "POST"])
def checkout1():
     if request.method == "POST":
            req1 = request.form
            print(req1)
            
     # with this we will not be able to miss any thing or any data
            missing = list()
            for k, v in req1.items():
                if v == "":
                    missing.append(k)
            if missing:
                feedback = f"Missing fields for {', '.join(missing)}"
                return render_template("checkout1.html", feedback=feedback)

            flag  = cc_validation_num(req1["CreditCardNumber"])
            flag1 = cc_valid_cvc(req1["security_code"])
            flag2 = cc_expiration_date(req1["expiration_date"])
                                                                  #flag3 = cc_payment_amount(req["amount"])
            if flag == True & flag1 == True & flag2 == True:
                return redirect(YOUR_DOMAIN + "/succes")
            else:
                return redirect(YOUR_DOMAIN + "/cancel")
                                                         #return redirect(YOUR_DOMAIN + "/succes")                  # request.url
                                                                  #return render_template("checkout1.html")
     return render_template("checkout1.html")


@app.route("/checkout2", methods=["GET", "POST"])
def checkout2():
    if request.method == "POST":
        req2 = request.form
        print(req2)

        # with this we will not be able to miss any thing or any data
        missing = list()
        for k, v in req2.items():
            if v == "":
                missing.append(k)
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("checkout1.html", feedback=feedback)

        flag = cc_validation_num(req2["CreditCardNumber"])
        flag1 = cc_valid_cvc(req2["security_code"])
        flag2 = cc_expiration_date(req2["expiration_date"])
                                                        # flag3 = cc_payment_amount(req["amount"])
        if flag == True & flag1 == True & flag2 == True:
            return redirect(YOUR_DOMAIN + "/succes")
        else:
            return redirect(YOUR_DOMAIN + "/cancel")
            # return redirect(YOUR_DOMAIN + "/succes")                  # request.url
            # return render_template("checkout1.html")
    return render_template("checkout2.html")


@app.route("/checkout3", methods=["GET", "POST"])
def checkout3():
    if request.method == "POST":
        req3 = request.form
        print(req3)

        # with this we will not be able to miss any thing or any data
        missing = list()
        for k, v in req3.items():
            if v == "":
                missing.append(k)
        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("checkout1.html", feedback=feedback)

        flag = cc_validation_num(req3["CreditCardNumber"])
        flag1 = cc_valid_cvc(req3["security_code"])
        flag2 = cc_expiration_date(req3["expiration_date"])
        # flag3 = cc_payment_amount(req["amount"])
        if flag == True & flag1 == True & flag2 == True:
            return redirect(YOUR_DOMAIN + "/succes")
        else:
            return redirect(YOUR_DOMAIN + "/cancel")
            # return redirect(YOUR_DOMAIN + "/succes")                  # request.url
            # return render_template("checkout1.html")
    return render_template("checkout3.html")


@app.route("/succes", methods=["GET", "POST"])
def succes():
    return render_template("succes.html")

@app.route("/cancel", methods=["GET", "POST"])
def cancel():
    return render_template("cancel.html")

def cc_validation_num(number):
    # for Card Number                     # claculate number of digits
    digit = 0
    temporary = number
    for i in temporary:
        digit = digit+1
    print("\nSum of Values =",digit)
                                     # indicating that card number should not be more then 12
    if digit != 12:
        print("OK")
        return False                   # return redirect(YOUR_DOMAIN + "/cancel")
    else:
        print("success")
        return True                  #return redirect(YOUR_DOMAIN + "/succes")

def cc_valid_cvc(cvc):
    #print(cvc)
    a = 0
    x = cvc
    for j in x:
        a = a+1
    print("\nSum of Values =",a)

    if a == 3:
        return True                      #print("OK")
    else:
        return False

def cc_expiration_date(date):
    x = print(date)
    present_day = datetime.now().date()
    print(present_day)
    d = datetime.strptime(date, "%Y-%m-%d").date()
    print(d)

    if d >= present_day:
        return True
        #print("can do process")
    else:
        return False
        #print("can not do process")


if __name__ == '__main__':
    app.run(port=4242)

# {% extends "public/templates/public_template.html" %}
# {% extends "templates/checkout1.html" %}