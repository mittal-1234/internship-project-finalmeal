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
print("✓ Old items and restaurants deleted")

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
    }
]

restaurants = {}
for r_data in restaurants_data:
    restaurant = Restaurant.objects.create(**r_data)
    restaurants[r_data['name']] = restaurant
    print(f"  ✓ Created {r_data['name']} ({r_data['cuisine']})")

# Step 3: Create 10 menu items distributed across restaurants (2 per restaurant)
print("\n[3] Creating 10 menu items...")
items_data = [
    # Dominos Pizza (2 items)
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Margherita Pizza',
        'description': 'Classic pizza with cheese and tomato',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?w=800&q=80'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Pepperoni Pizza',
        'description': 'Spicy pepperoni with mozzarella',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://i0.wp.com/www.spicesinmydna.com/wp-content/uploads/2024/02/Pepperoni-Pizza-with-Hot-Honey-Ricotta-Olives-and-Basil-9.jpg?fit=907%2C1360&ssl=1'
    },
    # Belgium Waffle House (2 items)
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Chocolate Waffle',
        'description': 'Crispy waffle with chocolate sauce',
        'price': 199,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&q=80'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Strawberry Waffle',
        'description': 'Fresh waffle with strawberry toppings',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=80'
    },
    # Burger King (2 items)
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Classic Cheeseburger',
        'description': 'Juicy beef patty with melted cheese',
        'price': 279,
        'vegeterian': False,
        'picture': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Veggie Burger',
        'description': 'Delicious vegetable patty burger',
        'price': 229,
        'vegeterian': True,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuf0USTKRQ5eRKoNDaTlq-bsxdYm89Pf-m7A&s'
    },
    # Paneer House (2 items)
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Paneer Tikka',
        'description': 'Grilled paneer cubes with spices',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://c.ndtvimg.com/2024-07/9fe2b05g_paneer-tikka_625x300_01_July_24.jpg'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Butter Chicken',
        'description': 'Tender chicken in creamy tomato sauce',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://www.licious.in/blog/wp-content/uploads/2020/10/butter-chicken--600x600.jpg'
    },
    # Chinese Express (2 items)
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Hakka Noodles',
        'description': 'Stir-fried noodles with vegetables',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR6byAqaBbNC3Wry-VBaTSbPUz9GccdcPJwdw&s'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Chicken Fried Rice',
        'description': 'Fragrant fried rice with chicken',
        'price': 229,
        'vegeterian': False,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQuNpzLejJ8aQrhiv1xJo5ytBFZwHY3wfeKKw&s'
    },
    
]
for item_data in items_data:
    item = Item.objects.create(**item_data)
    print(f"  ✓ Created {item_data['name']} at {item_data['restaurant'].name}")

print("\n" + "=" * 60)
print("DATABASE SETUP COMPLETE!")
print("=" * 60)
print(f"✓ Total Restaurants: {Restaurant.objects.count()}")
print(f"✓ Total Items: {Item.objects.count()}")
print("\nRestaurants:")
for r in Restaurant.objects.all():
    item_count = Item.objects.filter(restaurant=r).count()
    print(f"  • {r.name} ({r.cuisine}) - {item_count} items - ⭐ {r.rating}")
print("\n" + "=" * 60)
