from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,"amadon_app/index.html")

def process(request):
    if request.method == 'POST':
        if 'sum' not in request.session:
            request.session['sum'] = 0
        if 'product' not in request.session:
            request.session['product'] = ""
        if 'price' not in request.session:
            request.session['price'] = 0
        if 'total_quantity' not in request.session:
            request.session['total_quantity'] = 0

        request.session['product'] = request.POST['product_id']
        print "product id.....{}".format(request.session['product'])
        quantity = request.POST['quantity']
        print "quantity is...{}".format(quantity)
        if request.session['product'] == '1015':
            request.session['price'] = float(quantity) * 19.99
            request.session['total_quantity']+=int(quantity)
            # request.session.modified = True
        if request.session['product'] == '1016':
            request.session['price'] = float(quantity) * 29.99
            request.session['total_quantity']+=int(quantity)
            # request.session.modified = True
        if request.session['product'] == '1017':
            request.session['price'] = float(quantity) * 4.99
            request.session['total_quantity']+=int(quantity)
            # request.session.modified = True
        if request.session['product'] == '1018':
            request.session['price'] = float(quantity) * 49.99
            request.session['total_quantity']+=int(quantity)
            # request.session.modified = True
        request.session['sum'] += request.session['price']
        return redirect('/result') 
    else:
        return redirect('/')

def result(request):
    return render(request,"amadon_app/result.html")