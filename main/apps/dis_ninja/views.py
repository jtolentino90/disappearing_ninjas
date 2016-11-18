from django.shortcuts import render

# Create your views here.
def index(request):
	print("*"*100)
	print('Render complete')
	print("*"*100)
	return render(request, "dis_ninja/index.html")

def ninjas(request):
	print('x'*100)
	print('All the ninjas!')
	print('x'*100)
	return render(request, "dis_ninja/ninjas.html")

def ninjas_color(request, ninjas_color):
	print('c'*100)
	print('Separate colors')
	print('c'*100)

	context = { 'ninjas_color': ninjas_color }

	if ninjas_color == 'blue':
		context['img_tag'] = "dis_ninja/images/leonardo.jpg"
		context['name'] = "Leonardo"
	elif ninjas_color == 'red':
		context['img_tag'] = "dis_ninja/images/raphael.jpg"
		context['name'] = "Raphael"
	elif ninjas_color == 'orange':
		context['img_tag'] = "dis_ninja/images/michaelangelo.jpg"
		context['name'] = "Michaelangelo"
	elif ninjas_color == 'purple':
		context['img_tag'] = "dis_ninja/images/donatello.jpg"
		context['name'] = "Donatello"
	else:
		context['img_tag'] = "dis_ninja/images/april.jpg"
		context['name'] = "April (Not really a ninja..)"
	return render(request, 'dis_ninja/ninjas_color.html', context)

	#
	#
	# context = {
	# 	'blue': ninjas_color,
	# 	'red': ninjas_color
	# }
	# return render(request, 'dis_ninja/ninjas_color.html', context)


# def show(request, id):
# 	context = {
# 		'id': id
# 	}
# 	return render(request, 'second_app/show.html', context)
