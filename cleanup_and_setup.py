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
    # Dominos Pizza (5 items)
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Margherita Pizza',
        'description': 'A timeless classic featuring a thin, crispy crust topped with rich San Marzano tomato sauce, fresh mozzarella pearls, and fragrant basil leaves.',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Pizza_Margherita_stu_spivack.jpg'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Pepperoni Pizza',
        'description': 'The ultimate crowd-pleaser! Loaded with spicy, zesty pepperoni slices and a mountain of melted mozzarella cheese on our signature hand-tossed dough.',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Veggie Paradise Pizza',
        'description': 'A garden-fresh delight topped with golden corn, black olives, crisp capsicum, and red paprika on a bed of gooey mozzarella.',
        'price': 329,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/33593000/pexels-photo-33593000.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Chicken Golden Delight',
        'description': 'Mouth-watering double-pepper chicken, golden corn, and extra mozzarella cheese for a rich, satisfying bite.',
        'price': 399,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/5639555/pexels-photo-5639555.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Dominos Pizza'],
        'name': 'Paneer Makhani Pizza',
        'description': 'A fusion masterpiece! Creamy paneer makhani gravy, succulent paneer cubes, and crunchy onions on a perfectly baked crust.',
        'price': 379,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/35123976/pexels-photo-35123976.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # Belgium Waffle House (5 items)
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Chocolate Waffle',
        'description': 'Indulge in a warm, crispy Belgian waffle drenched in premium dark chocolate ganache, topped with chocolate shavings.',
        'price': 199,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Strawberry Waffle',
        'description': 'A delightful treat of golden waffles topped with fresh, juicy strawberries, a drizzle of sweet strawberry coulis, and a dusting of powdered sugar.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1459789034005-ba29c5783491?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Blueberry Waffle',
        'description': 'Warm waffles topped with a vibrant homemade blueberry compote and a dollop of fresh whipped cream.',
        'price': 210,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/29569373/pexels-photo-29569373.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Nutella Waffle',
        'description': 'Every chocolate lover\'s dream! Crispy waffles spread thick with Nutella and finished with a sprinkle of crushed hazelnuts.',
        'price': 249,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/37436076/pexels-photo-37436076.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Belgium Waffle House'],
        'name': 'Honey Butter Waffle',
        'description': 'Simple and elegant. A buttery waffle drizzled with pure organic honey for a light yet satisfying dessert.',
        'price': 159,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/8160967/pexels-photo-8160967.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # Burger King (5 items)
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Classic Cheeseburger',
        'description': 'A juicy, flame-grilled beef patty topped with melted cheddar, crisp lettuce, vine-ripened tomatoes, and our secret house sauce.',
        'price': 279,
        'vegeterian': False,
        'picture': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Veggie Burger',
        'description': 'A protein-packed garden patty made with fresh vegetables and grains, topped with avocado and sprouts on a whole-grain bun.',
        'price': 229,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1520072959219-c595dc870360?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Whopper Jr.',
        'description': 'The classic flame-grilled Whopper taste in a smaller size. Perfectly seasoned and topped with fresh pickles and onions.',
        'price': 189,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/7159268/pexels-photo-7159268.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Crispy Chicken Wrap',
        'description': 'Tender crispy chicken strips wrapped in a soft tortilla with shredded lettuce and creamy ranch dressing.',
        'price': 199,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/9624298/pexels-photo-9624298.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Burger King'],
        'name': 'Onion Rings',
        'description': 'Crispy, golden-brown fried onion rings seasoned to perfection. The ultimate side for any meal.',
        'price': 129,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/9738991/pexels-photo-9738991.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # Paneer House (5 items)
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Paneer Tikka',
        'description': 'Succulent cubes of cottage cheese marinated in a spicy yogurt blend, char-grilled to perfection for a smoky flavor.',
        'price': 299,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/20395267/pexels-photo-20395267.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Butter Chicken',
        'description': 'A world-famous North Indian delicacy! Tender chicken pieces simmered in a rich, velvety tomato and butter gravy.',
        'price': 349,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/29685054/pexels-photo-29685054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Paneer Tikka Masala',
        'description': 'Grilled paneer cubes served in a rich, creamy, and spicy onion-tomato gravy. A true vegetarian classic.',
        'price': 329,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/30858402/pexels-photo-30858402.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Dal Makhani',
        'description': 'Black lentils and kidney beans slow-cooked overnight with butter and cream for an authentic, deep flavor.',
        'price': 249,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/37182514/pexels-photo-37182514.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Paneer House'],
        'name': 'Garlic Naan',
        'description': 'Soft, leavened flatbread brushed with melted butter and topped with fresh minced garlic and cilantro.',
        'price': 69,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/10337726/pexels-photo-10337726.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # Chinese Express (5 items)
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Hakka Noodles',
        'description': 'Wok-tossed thin noodles with crisp vegetables, seasoned with aromatic Indo-Chinese spices and soy sauce.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/2764905/pexels-photo-2764905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Chicken Fried Rice',
        'description': 'Fragrant stir-fried rice with tender chicken bits, scrambled eggs, and fresh spring onions.',
        'price': 229,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/34668502/pexels-photo-34668502.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Veg Manchurian',
        'description': 'Crispy vegetable dumplings tossed in a zesty and slightly spicy ginger-garlic sauce.',
        'price': 210,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/35066808/pexels-photo-35066808.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Spring Rolls',
        'description': 'Crispy golden pastry shells filled with a savory mix of stir-fried vegetables and glass noodles.',
        'price': 159,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/35407775/pexels-photo-35407775.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['Chinese Express'],
        'name': 'Chili Chicken',
        'description': 'Tender pieces of chicken sautéed with peppers, onions, and a spicy chili-soy glaze. A spicy favorite.',
        'price': 279,
        'vegeterian': False,
        'picture': 'https://images.pexels.com/photos/5339083/pexels-photo-5339083.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # veggies (5 items)
    {
        'restaurant': restaurants['veggies'],
        'name': 'Paneer Fried Rice',
        'description': 'A vegetarian favorite! Aromatic rice tossed with cubes of golden-fried paneer and fresh garden vegetables.',
        'price': 189,
        'vegeterian': True,
        'picture': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMUSOkW6xq2izua5XRhxKlwMydHly1iBIxxg&s'
    },
    {
        'restaurant': restaurants['veggies'],
        'name': 'Vegetable Biryani',
        'description': 'Fragrant long-grain basmati rice layered with mixed vegetables, saffron, and aromatic spices. Served with raita.',
        'price': 249,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/9609848/pexels-photo-9609848.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['veggies'],
        'name': 'Masala Dosa',
        'description': 'A thin, crispy rice crepe filled with a savory spiced potato mash. Served with sambar and coconut chutney.',
        'price': 149,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/12392915/pexels-photo-12392915.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['veggies'],
        'name': 'Chole Bhature',
        'description': 'Spicy chickpeas served with fluffy, deep-fried bread. An iconic North Indian breakfast delicacy.',
        'price': 199,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/36388454/pexels-photo-36388454.jpeg?auto=compress&cs=tinysrgb&w=800'
    },
    {
        'restaurant': restaurants['veggies'],
        'name': 'Veg Pulao',
        'description': 'Light and aromatic rice cooked with seasonal vegetables and mild whole spices. A healthy, wholesome choice.',
        'price': 179,
        'vegeterian': True,
        'picture': 'https://vegecravings.com/wp-content/uploads/2016/07/veg-pulao-recipe-step-by-step-instructions.jpg'
    },

    # Cake De Lite (5 items)
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Chocolate Truffle',
        'description': 'A decadent masterpiece. Layers of moist cocoa sponge filled and frosted with silky dark chocolate truffle cream.',
        'price': 350,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/34802628/pexels-photo-34802628.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Pineapple Cake',
        'description': 'A tropical delight featuring light vanilla sponge layered with fresh pineapple chunks and whipped cream.',
        'price': 300,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/8820012/pexels-photo-8820012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Red Velvet Pastry',
        'description': 'Velvety red cocoa sponge layered with tangy cream cheese frosting. Elegant and perfectly balanced.',
        'price': 120,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1586788680434-30d324b2d46f?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Blueberry Muffin',
        'description': 'Buttery muffins bursting with fresh blueberries and topped with a crunchy streusel crumble.',
        'price': 80,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Cake De Lite'],
        'name': 'Vanilla Pastry',
        'description': 'A light and fluffy classic vanilla sponge pastry with smooth white chocolate shavings.',
        'price': 90,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/10249466/pexels-photo-10249466.jpeg?auto=compress&cs=tinysrgb&w=800'
    },

    # Frozen Bottle (5 items)
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Belgian Chocolate',
        'description': 'Our signature thick shake made with authentic Belgian dark chocolate, blended to perfection.',
        'price': 180,
        'vegeterian': True,
        'picture': 'https://imagedelivery.net/EtcVECyqIuOr1FjP12iTCg/eb06eec2-bf26-4b24-1bdb-5fa07c7be600/w=300'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Strawberry Shake',
        'description': 'A refreshing blend of sun-ripened strawberries and creamy vanilla ice cream.',
        'price': 150,
        'vegeterian': True,
        'picture': 'https://static.wixstatic.com/media/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Cold Coffee',
        'description': 'The perfect pick-me-up! Rich espresso blended with chilled milk and a scoop of vanilla ice cream.',
        'price': 120,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'Oreo Overload',
        'description': 'A thick vanilla shake loaded with crushed Oreo cookies and chocolate sauce.',
        'price': 210,
        'vegeterian': True,
        'picture': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?q=80&w=1000&auto=format&fit=crop'
    },
    {
        'restaurant': restaurants['Frozen Bottle'],
        'name': 'KitKat Shake',
        'description': 'A crunchy and creamy shake blended with real KitKat bars and chocolate syrup.',
        'price': 220,
        'vegeterian': True,
        'picture': 'https://images.pexels.com/photos/20205940/pexels-photo-20205940.jpeg?auto=compress&cs=tinysrgb&w=800'
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
