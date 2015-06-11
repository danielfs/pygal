import pygal
from flask import Flask, Response, render_template
from pygal.style import DarkGreenStyle

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	""" render svg figures on html """
	return render_template('index.html')

@app.route('/barchart/')
def forecast():
	""" render svg graph """
	bar_chart = pygal.Bar(width=500, height=400)
	bar_chart.title = "Barchart"
	lower, higher, params = [12, 13], [15, 18], ['param1', 'param2']
	bar_chart.add('lower', lower)
	bar_chart.add('higher', higher)
	bar_chart.x_labels = params
	return Response(response=bar_chart.render(), content_type='image/svg+xml')

@app.route('/piechart/')
def piechart():
	pie_chart = pygal.Pie(style=DarkGreenStyle)
	pie_chart.title = 'Expenses'
	# Add Category and it's percentage in pie chart
	pie_chart.add('Rent', 35)
	pie_chart.add('Trips', 15)
	pie_chart.add('Food', 40)
	pie_chart.add('Commuting', 10)
	return Response(response=pie_chart.render(), content_type='image/svg+xml')

@app.route('/linechart/')
def linechart():
	line_chart = pygal.Line()
	line_chart.title = 'Browser usage evolution (in %)'
	line_chart.x_labels = map(str, range(2002, 2013))
	line_chart.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
	line_chart.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
	line_chart.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
	line_chart.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
	return Response(response=line_chart.render(), content_type='image/svg+xml')

@app.route('/scatterplot/')
def scatterplot():
	xy_chart = pygal.XY(stroke=False)
	xy_chart.title = 'Correlation'
	xy_chart.add('A', [(0, 0), (.1, .2), (.3, .1), (.5, 1), (.8, .6), (1, 1.08), (1.3, 1.1), (2, 3.23), (2.43, 2)])
	xy_chart.add('B', [(.1, .15), (.12, .23), (.4, .3), (.6, .4), (.21, .21), (.5, .3), (.6, .8), (.7, .8)])
	xy_chart.add('C', [(.05, .01), (.13, .02), (1.5, 1.7), (1.52, 1.6), (1.8, 1.63), (1.5, 1.82), (1.7, 1.23), (2.1, 2.23), (2.3, 1.98)])
	return Response(response=xy_chart.render(), content_type='image/svg+xml')

@app.route('/countrymap/')
def countrymap():
	worldmap_chart = pygal.Worldmap()
	worldmap_chart.title = 'Minimum deaths by capital punishement (source: Amnesty International)'
	# Here you need to add intensity factor or rank of countries
	worldmap_chart.add('In 2012', {
		'af': 14,
		'bd': 1,
		'by': 3,
		'cn': 1000,
		'gm': 9,
		'in': 1,
		'ir': 314,
		'iq': 129,
		'jp': 7,
		'kp': 6,
		'pk': 1,
		'ps': 6,
		'sa': 79,
		'so': 6,
		'sd': 5,
		'tw': 6,
		'ae': 1,
		'us': 43,
		'ye': 28
	})
	return Response(response=worldmap_chart.render(), content_type='image/svg+xml')

if __name__ == '__main__':
	app.config['DEBUG'] = True
	app.run('0.0.0.0', 5000)
