from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
import random
import json

from .models import Customer, Restaurant, Item, Cart

import razorpay
from django.conf import settings

# Create your views here.
def index(request):
    return render(request, 'delivery/index.html')

def open_signin(request):
    return render(request, 'delivery/signin.html')

def open_signup(request):
    return render(request, 'delivery/signup.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        try:
            Customer.objects.get(username = username)
            return HttpResponse("Duplicate username!")
        except:
            Customer.objects.create(
                username = username,
                password = password,
                email = email,
                mobile = mobile,
                address = address,
            )
    return render(request, 'delivery/signin.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            Customer.objects.get(username = username, password = password)
            if username == 'admin':
                return render(request, 'delivery/admin_home.html')
            else:
                restaurantList = Restaurant.objects.all()
                return render(request, 'delivery/customer_home.html',{"restaurantList" : restaurantList, "username" : username})

        except Customer.DoesNotExist:
            return render(request, 'delivery/fail.html')
    
    return render(request, 'delivery/signin.html')
    
def open_add_restaurant(request):
    return render(request, 'delivery/add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        
        try:
            Restaurant.objects.get(name = name)
            return HttpResponse("Duplicate restaurant!")
        except:
            Restaurant.objects.create(
                name = name,
                picture = picture,
                cuisine = cuisine,
                rating = rating,
            )
    return render(request, 'delivery/admin_home.html')

def open_show_restaurant(request):
    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html',{"restaurantList" : restaurantList})

def open_update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    return render(request, 'delivery/update_restaurant.html', {"restaurant" : restaurant})

def update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        
        restaurant.name = name
        restaurant.picture = picture
        restaurant.cuisine = cuisine
        restaurant.rating = rating

        restaurant.save()

    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html',{"restaurantList" : restaurantList})


def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    restaurant.delete()

    restaurantList = Restaurant.objects.all()
    return render(request, 'delivery/show_restaurants.html',{"restaurantList" : restaurantList})


def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    itemList = restaurant.items.all()
    #itemList = Item.objects.all()
    return render(request, 'delivery/update_menu.html',{"itemList" : itemList, "restaurant" : restaurant})
    
def update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vegeterian = request.POST.get('vegeterian') == 'on'
        picture = request.POST.get('picture')
        
        try:
            Item.objects.get(name = name)
            return HttpResponse("Duplicate item!")
        except:
            Item.objects.create(
                restaurant = restaurant,
                name = name,
                description = description,
                price = price,
                vegeterian = vegeterian,
                picture = picture,
            )
    return render(request, 'delivery/admin_home.html')

def view_menu(request, restaurant_id, username):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    itemList = restaurant.items.all()
    #itemList = Item.objects.all()
    return render(request, 'delivery/customer_menu.html'
                  ,{"itemList" : itemList,
                     "restaurant" : restaurant, 
                     "username":username})

def add_to_cart(request, item_id, username):
    item = Item.objects.get(id = item_id)
    customer = Customer.objects.get(username = username)

    cart, created = Cart.objects.get_or_create(customer = customer)

    cart.items.add(item)

    return HttpResponse('added to cart')

def remove_from_cart(request, item_id, username):
    item = get_object_or_404(Item, id=item_id)
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()
    
    if cart:
        cart.items.remove(item)
        
    return redirect('show_cart', username=username)

def show_cart(request, username):
    customer = Customer.objects.get(username = username)
    cart = Cart.objects.filter(customer=customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    return render(request, 'delivery/cart.html',{"itemList" : items, "total_price" : total_price, "username":username})

# Checkout View
def checkout(request, username):
    # Fetch customer and their cart
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'delivery/checkout.html', {
            'error': 'Your cart is empty!',
        })

    # Initialize Razorpay client
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    # Create Razorpay order
    order_data = {
        'amount': int(total_price * 100),  # Amount in paisa
        'currency': 'INR',
        'payment_capture': '1',  # Automatically capture payment
    }
    order = client.order.create(data=order_data)

    # Pass the order details to the frontend
    return render(request, 'delivery/checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],  # Razorpay order ID
        'amount': total_price,
    })


# Orders Page
def orders(request, username):
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()

    # Fetch cart items and total price before clearing the cart
    cart_items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0

    # Clear the cart after fetching its details
    if cart:
        cart.items.clear()

    return render(request, 'delivery/orders.html', {
        'username': username,
        'customer': customer,
        'cart_items': cart_items,
        'total_price': total_price,
    })

def chatbot_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        message = data.get('message', '').lower().strip()
        
        restaurants = list(Restaurant.objects.all())
        items = list(Item.objects.all())
        
        if not message:
            return JsonResponse({'reply': "Please type something so I can help you find delicious food!"})
        
        # Greeting detection
        greetings = ['hi', 'hello', 'hey', 'hola', 'sup', 'yo', 'good morning', 'good evening']
        if any(message == g or message.startswith(g + ' ') or message.startswith(g + ',') for g in greetings):
            return JsonResponse({'reply': "Hey there! 👋 I'm your AI Food Buddy! Tell me what you're craving — pizza, burgers, desserts, Indian food — or just say 'surprise me' and I'll pick something amazing for you!"})
        
        # "Surprise me" or random
        if any(w in message for w in ['surprise', 'random', 'anything', 'whatever', "don't know", 'dont know', 'confused', 'not sure']):
            picks = random.sample(items, min(3, len(items)))
            response = "🎲 Here are some surprise picks for you!\n\n"
            for i in picks:
                veg = "🟢 Veg" if i.vegeterian else "🔴 Non-Veg"
                response += f"• {i.name} — ₹{int(i.price)} ({veg}) from {i.restaurant.name}\n"
            return JsonResponse({'reply': response})
        
        # Food category keywords mapping
        categories = {
            'pizza': ['pizza'],
            'burger': ['burger', 'whopper', 'cheeseburger'],
            'waffle': ['waffle'],
            'shake': ['shake', 'cold coffee', 'coffee', 'milkshake', 'overload', 'kitkat'],
            'cake': ['cake', 'truffle', 'pastry', 'muffin'],
            'chinese': ['noodles', 'noodle', 'manchurian', 'spring roll', 'fried rice', 'chili chicken', 'chinese'],
            'indian': ['paneer', 'tikka', 'biryani', 'dal', 'naan', 'butter chicken', 'chole', 'bhature', 'dosa', 'pulao', 'indian'],
            'dessert': ['dessert', 'sweet', 'chocolate', 'ice cream', 'sundae', 'gulab'],
            'veg': ['veg', 'vegetarian', 'vegetable'],
            'non-veg': ['non-veg', 'nonveg', 'non veg', 'chicken', 'meat', 'egg'],
            'snack': ['fries', 'onion ring', 'garlic bread', 'wrap', 'roll', 'snack', 'side'],
            'drink': ['drink', 'beverage', 'juice', 'shake', 'coffee', 'cold'],
            'wrap': ['wrap', 'shawarma', 'falafel', 'roll'],
            'rice': ['rice', 'biryani', 'pulao', 'fried rice'],
            'bread': ['naan', 'bread', 'roti', 'bhature'],
        }
        
        # Search for matching items
        relevant_items = []
        
        # 1. Direct name match
        for item in items:
            if item.name.lower() in message or message in item.name.lower():
                relevant_items.append(item)
        
        # 2. Category/keyword match
        if not relevant_items:
            matched_keywords = []
            for category, keywords in categories.items():
                for kw in keywords:
                    if kw in message:
                        matched_keywords.append(kw)
            
            if matched_keywords:
                for item in items:
                    item_text = f"{item.name} {item.description} {item.restaurant.cuisine}".lower()
                    if any(kw in item_text for kw in matched_keywords):
                        if item not in relevant_items:
                            relevant_items.append(item)
        
        # 3. Restaurant name match
        if not relevant_items:
            for r in restaurants:
                if r.name.lower() in message or message in r.name.lower():
                    relevant_items = [i for i in items if i.restaurant.id == r.id]
                    break
        
        # 4. Veg/Non-veg filter
        if not relevant_items:
            if any(w in message for w in ['veg', 'vegetarian', 'vegetable']):
                veg_items = [i for i in items if i.vegeterian]
                relevant_items = random.sample(veg_items, min(5, len(veg_items)))
            elif any(w in message for w in ['non-veg', 'nonveg', 'chicken', 'meat']):
                nv_items = [i for i in items if not i.vegeterian]
                relevant_items = random.sample(nv_items, min(5, len(nv_items)))
        
        # 5. Fuzzy word-by-word match as last resort
        if not relevant_items:
            words = [w for w in message.split() if len(w) > 2 and w not in ['the', 'and', 'for', 'want', 'give', 'show', 'get', 'some', 'any', 'have', 'like', 'need', 'can', 'please', 'what', 'which', 'with', 'from', 'this', 'that', 'good', 'best', 'try', 'eat', 'food', 'meal', 'order', 'menu']]
            for item in items:
                item_text = f"{item.name} {item.description} {item.restaurant.name} {item.restaurant.cuisine}".lower()
                if any(w in item_text for w in words):
                    if item not in relevant_items:
                        relevant_items.append(item)
        
        # Build response
        if relevant_items:
            # Limit to 5 items max
            show_items = relevant_items[:5]
            response = f"🍽️ I found {len(relevant_items)} item(s) for you!\n\n"
            for i in show_items:
                veg = "🟢 Veg" if i.vegeterian else "🔴 Non-Veg"
                response += f"• {i.name} — ₹{int(i.price)} ({veg})\n  📍 {i.restaurant.name}\n\n"
            if len(relevant_items) > 5:
                response += f"...and {len(relevant_items) - 5} more! Try being more specific."
            return JsonResponse({'reply': response})
        
        # Nothing matched — give helpful suggestions
        picks = random.sample(items, min(3, len(items)))
        response = "I couldn't find an exact match, but here are some popular picks!\n\n"
        for i in picks:
            veg = "🟢 Veg" if i.vegeterian else "🔴 Non-Veg"
            response += f"• {i.name} — ₹{int(i.price)} ({veg}) from {i.restaurant.name}\n"
        response += "\n💡 Try: 'pizza', 'burger', 'dessert', 'Chinese', 'Indian', 'veg', or a restaurant name!"
        return JsonResponse({'reply': response})
        
    return JsonResponse({'error': 'Invalid request'}, status=400)


def sync_database(request):
    """Hidden view to trigger database cleanup and setup on Render"""
    import subprocess
    import sys
    try:
        # Run the cleanup_and_setup.py script
        result = subprocess.run([sys.executable, 'cleanup_and_setup.py'], capture_output=True, text=True)
        return HttpResponse(f"Database sync successful!<br><pre>{result.stdout}</pre>")
    except Exception as e:
        return HttpResponse(f"Database sync failed: {str(e)}", status=500)
