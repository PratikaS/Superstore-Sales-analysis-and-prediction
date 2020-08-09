from flask import Flask, request, render_template
import predictionDaily
import predictionMonthly
import predictionYearly
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')
    #return "Welcome"

@app.route('/predict')
def predict_page():
    return render_template("Main.html")

@app.route("/predict/Daily_prediction")
def daily_predict():
    return render_template("prediction1.html")

@app.route('/predict/Daily_prediction/prediction', methods=["POST"])
def predict():
    algorithm=int(request.form['algorithm'])
    Region1 = (request.form['Region'])
    Country1 = (request.form['Country'])
    City1 = (request.form['City'])
    Segment = int(request.form['Segment'])
    Category1 = (request.form['Category'])
    Sub_Category1 = (request.form['Sub_Category'])
    Discount = int(request.form['Discount'])
    Price = float(request.form['Price'])
    Date = (request.form['Date'])

    Day, Month, Year = Date.split('-')
    regionList = ["Central", "Africa", "Oceania", "Central Asia", "Canada", "Southeast Asia","Caribbean"]
    regionlist1 = [3, 0, 9, 4, 1, 11,2]
    countrylist = ["Thailand", "Indonesia", "Spain", "Australia", "Belgium", "Austria", "Cuba", "Canada", "Angola","Egypt", "Libya", "South Africa", "El Salvador", "France", "India"]
    countrylist1 = [129, 58, 6, 119, 13, 7, 30, 22, 3, 37, 73, 116, 38, 44, 57]
    citylist = ["Benguela", "Cairo", "Alexandria", "Johannesburg", "London", "New York City", "Santa Clara",
                "Santiago de Cuba", "Manzanillo","Vienna", "Graz", "Namur", "Ghent", "Mejicanos", "San Salvador", "Soyapango", "Lille", "Lyon", "Paris",
                "Pune", "New Delhi", "Gorakhpur", "Brisbane", "Adelaide", "Melbourne", "Sydney",
                "Wollongong", "Barcelona", "Madrid", "Jakarta", "Bandung", "Bangkok"]
    citylist1 = [358, 554, 70, 1557, 1895, 2290, 2889, 2903, 2006, 3391, 1229, 2246, 4514, 2080, 2870, 3047, 1855, 1948,
                 2445, 2613, 2287, 1209, 497, 26,
                 2082, 3107, 3518, 291, 1959, 1508, 274, 276]
    index = regionList.index(Region1)
    print(f"index  {index}")
    Region = regionlist1[index]
    print(f"value : {Region}")
    index = countrylist.index(Country1)
    print(f"index  {index}")
    Country = countrylist1[index]
    print(f"value : {Country}")
    index = citylist.index(City1)
    print(f"index  {index}")
    City = citylist1[index]
    print(f"value : {City}")
    CategoryList = ["Office Supplies", "Furniture", "Technology"]
    Categorylist1 = [1, 0, 2]
    Sub_CategoryList = ["Envelopes", "Fasteners", "Appliances", "Storage", "Supplies","Binders","Paper","Art","Furnishings","Bookcases","Chairs","Tables","Copiers","Accessories","Phones","Machines"]
    Sub_CategoryList1 = [7, 8, 1, 14, 15,3,12,2,9,4,5,16,6,0,13,11]
    index = CategoryList.index(Category1)
    Category = Categorylist1[index]
    index = Sub_CategoryList.index(Sub_Category1)
    Sub_Category = Sub_CategoryList1[index]
    values = [City,Country, Segment, Region, Category, Sub_Category, Discount, Price,Day,Month,Year]
    # print(values)

    algorithm_name=''
    accuracy=0

    if algorithm==0:
        prediction=predictionDaily.classifier_rf.predict([values])
        algorithm_name="Random Forest"
        accuracy=predictionDaily.rf_accuracy
    elif algorithm==1:
        prediction=predictionDaily.classifier_dt.predict([values])
        algorithm_name="Decision Tree"
        accuracy=predictionDaily.dt_accuracy

    return render_template("result.html",Discount=Discount, Price=Price,Prediction=int(prediction[0]),accuracy=accuracy,algorithm=algorithm_name)

@app.route("/predict/monthly_prediction")
def Monthly_predict():
    return render_template("predictionMonthly.html")

@app.route('/predict/monthly_prediction/prediction', methods=["POST"])
def predict_monthly():
    algorithm=int(request.form['algorithm'])
    Region1 = (request.form['Region'])
    Country1 = (request.form['Country'])
    City1 = (request.form['City'])
    Segment = int(request.form['Segment'])
    Category1 = (request.form['Category'])
    Sub_Category1 = (request.form['Sub_Category'])
    Discount = float(request.form['Discount'])
    Price = float(request.form['Price'])
    Year = int(request.form['Year'])
    Month = int(request.form['Month'])

    regionList = ["Central", "Africa", "Oceania", "Central Asia", "Canada", "Southeast Asia","Caribbean"]
    regionlist1 = [3, 0, 9, 4, 1, 11,2]
    countrylist = ["Thailand", "Indonesia", "Spain", "Australia", "Belgium", "Austria", "Cuba", "Canada", "Angola",
                   "Egypt", "Libya", "South Africa", "El Salvador", "France", "India"]
    countrylist1 = [129, 58, 6, 119, 13, 7, 30, 22, 3, 37, 73, 116, 38, 44, 57]
    citylist = ["Benguela", "Cairo", "Alexandria", "Johannesburg", "London", "New York City", "Santa Clara",
                "Santiago de Cuba", "Manzanillo","Vienna", "Graz", "Namur", "Ghent", "Mejicanos", "San Salvador", "Soyapango", "Lille", "Lyon", "Paris",
                "Pune", "New Delhi", "Gorakhpur", "Brisbane", "Adelaide", "Melbourne", "Sydney",
                "Wollongong", "Barcelona", "Madrid", "Jakarta", "Bandung", "Bangkok"]
    citylist1 = [358, 554, 70, 1557, 1895, 2290, 2889, 2903, 2006, 3391, 1229, 2246, 4514, 2080, 2870, 3047, 1855, 1948,
                 2445, 2613, 2287, 1209, 497, 26,
                 2082, 3107, 3518, 291, 1959, 1508, 274, 276]
    index = regionList.index(Region1)
    print(f"index  {index}")
    Region = regionlist1[index]
    print(f"value : {Region}")
    index = countrylist.index(Country1)
    print(f"index  {index}")
    Country = countrylist1[index]
    print(f"value : {Country}")
    index = citylist.index(City1)
    print(f"index  {index}")
    City = citylist1[index]
    print(f"value : {City}")
    CategoryList = ["Office Supplies", "Furniture", "Technology"]
    Categorylist1 = [1, 0, 2]
    Sub_CategoryList = ["Envelopes", "Fasteners", "Appliances", "Storage", "Supplies", "Binders", "Paper", "Art","Furnishings", "Bookcases", "Chairs", "Tables", "Copiers", "Accessories", "Phones", "Machines"]
    Sub_CategoryList1 = [7, 8, 1, 14, 15, 3, 12, 2, 9, 4, 5, 16, 6, 0, 13, 11]
    index = CategoryList.index(Category1)
    Category = Categorylist1[index]
    index = Sub_CategoryList.index(Sub_Category1)
    Sub_Category = Sub_CategoryList1[index]
    values = [City, Country, Segment, Region, Category, Sub_Category, Discount, Price,Month, Year]
    print(values)

    algorithm_name=''
    accuracy=0

    if algorithm==0:
        prediction=predictionMonthly.classifier_rf.predict([values])
        algorithm_name="Random Forest"
        accuracy=predictionMonthly.rf_accuracy
    elif algorithm==1:
        prediction=predictionMonthly.classifier_dt.predict([values])
        algorithm_name="Decision Tree"
        accuracy=predictionMonthly.dt_accuracy

    return render_template("result.html",Discount=Discount, Price=Price,Prediction=int(prediction[0]),accuracy=accuracy,algorithm=algorithm_name)

@app.route("/predict/yearly_prediction")
def Yearly_predict():
    return render_template("predictionYearly.html")

@app.route('/predict/yearly_prediction/prediction', methods=["POST"])
def predict_yearly():
    algorithm=int(request.form['algorithm'])
    Region1 =(request.form['Region'])
    Country1 = (request.form['Country'])
    City1 = (request.form['City'])
    Segment = int(request.form['Segment'])
    Category1 = (request.form['Category'])
    Sub_Category1 = (request.form['Sub_Category'])
    Discount = float(request.form['Discount'])
    Price = float(request.form['Price'])
    Year = int(request.form['Year'])
    regionList = ["Central", "Africa", "Oceania", "Central Asia", "Canada", "Southeast Asia","Caribbean"]
    regionlist1 = [3, 0, 9, 4, 1, 11,2]
    countrylist = ["Thailand", "Indonesia", "Spain", "Australia", "Belgium", "Austria", "Cuba", "Canada", "Angola",
                   "Egypt", "Libya", "South Africa", "El Salvador", "France", "India"]
    countrylist1 = [129, 58, 6, 119, 13, 7, 30, 22, 3, 37, 73, 116, 38, 44, 57]
    citylist = ["Benguela", "Cairo", "Alexandria", "Johannesburg", "London", "New York City", "Santa Clara",
                "Santiago de Cuba", "Manzanillo", "Vienna", "Graz", "Namur", "Ghent", "Mejicanos", "San Salvador", "Soyapango", "Lille", "Lyon", "Paris",
                "Pune", "New Delhi", "Gorakhpur", "Brisbane", "Adelaide", "Melbourne", "Sydney",
                "Wollongong", "Barcelona", "Madrid", "Jakarta", "Bandung", "Bangkok"]
    citylist1 = [358, 554, 70, 1557, 1895, 2290, 2889, 2903, 2006, 3391, 1229, 2246, 4514, 2080, 2870, 3047, 1855, 1948,
                 2445, 2613, 2287, 1209, 497, 26,
                 2082, 3107, 3518, 291, 1959, 1508, 274, 276]
    index = regionList.index(Region1)
    print(f"index  {index}")
    Region = regionlist1[index]
    print(f"value : {Region}")
    index = countrylist.index(Country1)
    print(f"index  {index}")
    Country = countrylist1[index]
    print(f"value : {Country}")
    index = citylist.index(City1)
    print(f"index  {index}")
    City = citylist1[index]
    print(f"value : {City}")
    CategoryList = ["Office Supplies", "Furniture", "Technology"]
    Categorylist1 = [1, 0, 2]
    Sub_CategoryList = ["Envelopes", "Fasteners", "Appliances", "Storage", "Supplies", "Binders", "Paper", "Art",
                        "Furnishings", "Bookcases", "Chairs", "Tables", "Copiers", "Accessories", "Phones", "Machines"]
    Sub_CategoryList1 = [7, 8, 1, 14, 15, 3, 12, 2, 9, 4, 5, 16, 6, 0, 13, 11]
    index = CategoryList.index(Category1)
    Category = Categorylist1[index]
    index = Sub_CategoryList.index(Sub_Category1)
    Sub_Category = Sub_CategoryList1[index]
    values = [City,Country, Segment, Region, Category, Sub_Category, Discount, Price,Year]
    print(values)

    algorithm_name=''
    accuracy=0

    if algorithm==0:
        prediction=predictionYearly.classifier_rf.predict([values])
        algorithm_name="Random Forest"
        accuracy=predictionYearly.rf_accuracy
    elif algorithm==1:
        prediction=predictionYearly.classifier_dt.predict([values])
        algorithm_name="Decision Tree"
        accuracy=predictionYearly.dt_accuracy

    return render_template("result.html",Discount=Discount, Price=Price,Prediction=int(prediction[0]),accuracy=accuracy,algorithm=algorithm_name)


@app.route('/analyse')
def analyse_data():
    return render_template("analyse.html")

@app.route('/analyse/generic')
def analysis_generic():
    return render_template("analyse1.html")

@app.route('/analyse/daily')
def analysis_daily():
    return render_template("analyse2.html")

@app.route('/analyse/monthly')
def analysis_monthly():
    return render_template("analyse3.html")

@app.route('/analyse/yearly')
def analysis_weekly():
    return render_template("analyse4.html")

app.run(port=4013, host='0.0.0.0', debug=True)