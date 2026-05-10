#!/usr/bin/env python
"""
Script to clean up database:
1. Delete all current items except 10 selected ones
2. Create 5 new restaurants
3. Assign items to restaurants
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
django.setup()

from delivery.models import Restaurant, Item

print("=" * 60)
print("STARTING DATABASE CLEANUP AND RESTRUCTURING")
print("=" * 60)

# Step 1: Delete all current items and restaurants
print("\n[1] Clearing old data...")
Item.objects.all().delete()
Restaurant.objects.all().delete()
print("[OK] Old items and restaurants deleted")

# Step 2: Create 5 restaurants
print("\n[2] Creating 5 restaurants...")
restaurants_data = [
    {
        'name': 'Dominos Pizza',
        'cuisine': 'Pizza',
        'rating': 4.5,
        'picture': 'https://play-lh.googleusercontent.com/_lq2HX0YJNDrr0EeUebLAB2JsGbRGyoFY-XOnuUFTPfeEqaHNIyMOGqLx-oq4mUWPpn0'
    },
    {
        'name': 'Belgium Waffle House',
        'cuisine': 'Desserts & Waffles',
        'rating': 4.3,
        'picture': 'https://s3-media0.fl.yelpcdn.com/bphoto/4vw8uGpbnjmIN47EZEoKig/1000s.jpg'
    },
    {
        'name': 'Burger King',
        'cuisine': 'Burgers & Fast Food',
        'rating': 4.2,
        'picture': 'https://www.allrecipes.com/thmb/xVGw1xqe1jDcc9jYmNZkY621atQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/ar-burger-king-getty-4x3-2-25772f696b734be5b78cb73cc4529ec7.jpg'
    },
    {
        'name': 'Paneer House',
        'cuisine': 'Indian Vegetarian',
        'rating': 4.4,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcReQxiXNenuPYL0REN1hp_0oWIBk0WUmRJc9Q&s'
    },
    {
        'name': 'Chinese Express',
        'cuisine': 'Chinese',
        'rating': 4.1,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRu-lhvqHnEgVp2WEjEHMrY-lHFgk67TqcoWg&s'
    },
    {
        'name': 'veggies',
        'cuisine': 'Multicultural Cuisine',
        'rating': 4.9,
        'picture': 'https://img.restaurantguru.com/ree9-Ashokas-Veggies-logo.jpg'
    },
    {
        'name': 'Cake De Lite',
        'cuisine': 'Desserts, Cakes, Bakery',
        'rating': 4.5,
        'picture': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&q=80'
    },
    {
        'name': 'Frozen Bottle',
        'cuisine': 'Milkshakes, Desserts, Ice Cream',
        'rating': 4.3,
        'picture': 'https://images.unsplash.com/photo-1579954115545-a95591f28be0?w=800&q=80'
    }
]

restaurants = {}
for r_data in restaurants_data:
    restaurant = Restaurant.objects.create(**r_data)
    restaurants[r_data['name']] = restaurant
    print(f"  [OK] Created {r_data['name']} ({r_data['cuisine']})")

# Step 3: Create 10 menu items distributed across restaurants (2 per restaurant)
print("\n[3] Creating 10 menu items...")

# Update Frozen Bottle restaurant image
fb = restaurants.get('Frozen Bottle')
if fb:
    fb.picture = 'https://cdn.shopify.com/s/files/1/0611/5878/5188/files/Frozen_Bottle_Logo.png?v=1701495352'
    fb.save()

items_data = [
    # Dominos Pizza (2 items)
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Margherita Pizza',
        'description': 'A timeless classic featuring a thin, crispy crust topped with rich San Marzano tomato sauce, fresh mozzarella pearls, and fragrant basil leaves.',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1574129623612-9865b206677a?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Pepperoni Pizza',
        'description': 'The ultimate crowd-pleaser! Loaded with spicy, zesty pepperoni slices and a mountain of melted mozzarella cheese on our signature hand-tossed dough.',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?q=80&w=1000&auto=format&fit=crop'
    },
    # Belgium Waffle House (2 items)
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Chocolate Waffle',
        'description': 'Indulge in a warm, crispy Belgian waffle drenched in premium dark chocolate ganache, topped with chocolate shavings.',
        'price': 199,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1593531182844-d2ad0d03b0c5?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Strawberry Waffle',
        'description': 'A delightful treat of golden waffles topped with fresh, juicy strawberries, a drizzle of sweet strawberry coulis, and a dusting of powdered sugar.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1459789034005-ba29c5783491?q=80&w=1000&auto=format&fit=crop'
    },
    # Burger King (2 items)
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Classic Cheeseburger',
        'description': 'A juicy, flame-grilled beef patty topped with melted cheddar, crisp lettuce, vine-ripened tomatoes, and our secret house sauce on a toasted brioche bun.',
        'price': 279,
        'vegeterian': False,
        'picture': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Veggie Burger',
        'description': 'A protein-packed garden patty made with fresh vegetables and grains, topped with avocado, sprouts, and vegan aioli on a whole-grain bun.',
        'price': 229,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1520072959219-c595dc870360?q=80&w=1000&auto=format&fit=crop'
    },
    # Paneer House (2 items)
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Paneer Tikka',
        'description': 'Succulent cubes of cottage cheese marinated in a spicy yogurt blend, char-grilled to perfection in a traditional tandoor for a smoky flavor.',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/3928854/pexels-photo-3928854.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Butter Chicken',
        'description': 'A world-famous North Indian delicacy! Tender chicken pieces simmered in a rich, velvety tomato and butter gravy.',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/29685054/pexels-photo-29685054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    # Chinese Express (2 items)
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Hakka Noodles',
        'description': 'Wok-tossed thin noodles with a colorful array of crisp vegetables, seasoned with aromatic Indo-Chinese spices and soy sauce.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/2764905/pexels-photo-2764905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Chicken Fried Rice',
        'description': 'Fragrant stir-fried rice with tender chicken bits, scrambled eggs, and fresh spring onions for a perfect savory meal.',
        'price': 229,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/34668502/pexels-photo-34668502.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['veggies'],
        'name': 'Paneer Fried Rice',
        'description': 'A vegetarian favorite! Aromatic rice tossed with cubes of golden-fried paneer and fresh garden vegetables in a savory sauce.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/31783383/pexels-photo-31783383.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    # Cake De Lite (4 items)
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Chocolate Truffle',
        'description': 'A decadent masterpiece for chocolate lovers. Layers of moist cocoa sponge filled and frosted with silky dark chocolate truffle cream.',
        'price': 350,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1578985543062-d413826bb0a8?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Pineapple Cake',
        'description': 'A tropical delight featuring light vanilla sponge soaked in pineapple juice, layered with fresh pineapple chunks and whipped cream.',
        'price': 300,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1621303837174-89787a7d4729?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Red Velvet Pastry',
        'description': 'Vibrant and velvety red cocoa sponge layered with tangy cream cheese frosting. A perfect balance of sweetness and elegance.',
        'price': 120,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1586788680434-30d324b2d46f?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Blueberry Muffin',
        'description': 'Bursting with fresh blueberries, these buttery muffins feature a hint of lemon zest and a crunchy streusel topping.',
        'price': 80,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?q=80&w=1000&auto=format&fit=crop'
    },
    # Frozen Bottle (4 items)
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Belgian Chocolate',
        'description': 'Our signature thick shake made with authentic Belgian dark chocolate, blended to perfection for an intense experience.',
        'price': 180,
        'vegeterian': True,
        'picture': 'https://imagedelivery.net/EtcVECyqIuOr1FjP12iTCg/eb06eec2-bf26-4b24-1bdb-5fa07c7be600/w=300'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Strawberry Shake',
        'description': 'A refreshing blend of sun-ripened strawberries and creamy vanilla ice cream, topped with a fresh strawberry.',
        'price': 150,
        'vegeterian': True,
        'picture': 'https://static.wixstatic.com/media/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Cold Coffee',
        'description': 'The perfect pick-me-up! Rich espresso blended with chilled milk and a scoop of vanilla ice cream, served over ice.',
        'price': 120,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Oreo Overload',
        'description': 'A cookies-and-cream dream. A thick vanilla shake loaded with crushed Oreo cookies and chocolate sauce.',
        'price': 210,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?q=80&w=1000&auto=format&fit=crop'
    },
]
for item_data in items_data:
    item = Item.objects.create(**item_data)
    print(f"  [OK] Created {item_data['name']} at {item_data['restaurant'].name}")

print("\n" + "=" * 60)
print("DATABASE SETUP COMPLETE!")
print("=" * 60)
print(f"[OK] Total Restaurants: {Restaurant.objects.count()}")
print(f"[OK] Total Items: {Item.objects.count()}")
print("\nRestaurants:")
for r in Restaurant.objects.all():
    item_count = Item.objects.filter(restaurant=r).count()
    print(f"  - {r.name} ({r.cuisine}) - {item_count} items - Rating: {r.rating}")
print("\n" + "=" * 60)
