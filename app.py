from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Stock_Market():
    return render_template('index.html')

@app.route("/tata")
def TATA():
    from pandas_datareader import data
    import datetime
    from datetime import date
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    now=date.today()
    start=datetime.datetime(2021,9,20)
    end=now
    df=data.DataReader(name='TTM', data_source='yahoo',start=start,end=end)

    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c <o:
            value="Decrease"
        else:
            value="Equal"
        return value
    df["Status"]=[inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"]=(df.Close+df.Open)/2
    df["Height"]=abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1500, height=400)
    p.title.text="Candlestick Charts" 
    p.grid.grid_line_alpha=0.3

    Hours_12=12*60*60*1000
    p.segment(df.index, df.High, df.index, df.Low, color='black')

    p.rect(df.index[df.Status=='Increase'], df.Middle[df.Status=='Increase'], Hours_12, df.Height[df.Status=='Increase'],
        fill_color='#32CD32', line_color='black')

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], Hours_12, df.Height[df.Status=="Decrease"],
        fill_color="#CD5C5C", line_color="black")
    script1, div1 = components(p)
    cdn_js=CDN.js_files
    cdn_css=CDN.css_files
    return render_template('tata.html', script1=script1, div1=div1, cdn_js=cdn_js)
    

@app.route("/google")
def google():
    from pandas_datareader import data
    import datetime
    from datetime import date
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    now=date.today()
    start=datetime.datetime(2021,9,20)
    end=now
    df=data.DataReader(name='GOOG', data_source='yahoo',start=start,end=end)

    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c <o:
            value="Decrease"
        else:
            value="Equal"
        return value
    df["Status"]=[inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"]=(df.Close+df.Open)/2
    df["Height"]=abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1500, height=400)
    p.title.text="Candlestick Charts" 
    p.grid.grid_line_alpha=0.3

    Hours_12=12*60*60*1000
    p.segment(df.index, df.High, df.index, df.Low, color='black')

    p.rect(df.index[df.Status=='Increase'], df.Middle[df.Status=='Increase'], Hours_12, df.Height[df.Status=='Increase'],
        fill_color='#32CD32', line_color='black')

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], Hours_12, df.Height[df.Status=="Decrease"],
        fill_color="#CD5C5C", line_color="black")
    script1, div1 = components(p)
    cdn_js=CDN.js_files
    cdn_css=CDN.css_files
    return render_template('google.html', script1=script1, div1=div1, cdn_js=cdn_js)

@app.route("/apple")
def apple():
    from pandas_datareader import data
    import datetime
    from datetime import date
    from bokeh.plotting import figure, show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN

    now=date.today()
    start=datetime.datetime(2021,9,20)
    end=now
    df=data.DataReader(name='AAPL', data_source='yahoo',start=start,end=end)

    def inc_dec(c, o):
        if c > o:
            value="Increase"
        elif c <o:
            value="Decrease"
        else:
            value="Equal"
        return value
    df["Status"]=[inc_dec(c, o) for c, o in zip(df.Close, df.Open)]
    df["Middle"]=(df.Close+df.Open)/2
    df["Height"]=abs(df.Close-df.Open)
    df

    p=figure(x_axis_type='datetime', width=1500, height=400)
    p.title.text="Candlestick Charts" 
    p.grid.grid_line_alpha=0.3

    Hours_12=12*60*60*1000
    p.segment(df.index, df.High, df.index, df.Low, color='black')

    p.rect(df.index[df.Status=='Increase'], df.Middle[df.Status=='Increase'], Hours_12, df.Height[df.Status=='Increase'],
        fill_color='#32CD32', line_color='black')

    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], Hours_12, df.Height[df.Status=="Decrease"],
        fill_color="#CD5C5C", line_color="black")
    script1, div1 = components(p)
    cdn_js=CDN.js_files
    cdn_css=CDN.css_files
    return render_template('apple.html', script1=script1, div1=div1, cdn_js=cdn_js)
    #return "Know your stocks in details"

@app.route("/stocks")
def Stock_Market_details():
    return "Detailed level about stocks"

if __name__=="__main__":
    app.run(debug=True) 