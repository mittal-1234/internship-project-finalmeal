import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
django.setup()

from delivery.models import Item

# Clear all corrupted picture data
Item.objects.all().update(picture='')
print("[OK] Cleared all corrupted picture data")

# Restore correct URLs for all 40 items
mapping = {
    # Dominos Pizza (5)
    'Margherita Pizza': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Pizza_Margherita_stu_spivack.jpg',
    'Pepperoni Pizza': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?q=80&w=1000&auto=format&fit=crop',
    'Veggie Paradise Pizza': 'https://images.pexels.com/photos/33593000/pexels-photo-33593000.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Chicken Golden Delight': 'https://images.pexels.com/photos/5639555/pexels-photo-5639555.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Paneer Makhani Pizza': 'https://images.pexels.com/photos/35123976/pexels-photo-35123976.jpeg?auto=compress&cs=tinysrgb&w=800',
    # Belgium Waffle House (5)
    'Chocolate Waffle': 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?q=80&w=1000&auto=format&fit=crop',
    'Strawberry Waffle': 'https://images.unsplash.com/photo-1459789034005-ba29c5783491?q=80&w=1000&auto=format&fit=crop',
    'Blueberry Waffle': 'https://images.pexels.com/photos/29569373/pexels-photo-29569373.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Nutella Waffle': 'https://images.pexels.com/photos/37436076/pexels-photo-37436076.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Honey Butter Waffle': 'https://images.pexels.com/photos/8160967/pexels-photo-8160967.jpeg?auto=compress&cs=tinysrgb&w=800',
    # Burger King (5)
    'Classic Cheeseburger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop',
    'Veggie Burger': 'https://images.unsplash.com/photo-1520072959219-c595dc870360?q=80&w=1000&auto=format&fit=crop',
    'Whopper Jr.': 'https://images.pexels.com/photos/7159268/pexels-photo-7159268.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Crispy Chicken Wrap': 'https://images.pexels.com/photos/9624298/pexels-photo-9624298.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Onion Rings': 'https://images.pexels.com/photos/9738991/pexels-photo-9738991.jpeg?auto=compress&cs=tinysrgb&w=800',
    # Paneer House (5)
    'Paneer Tikka': 'https://images.pexels.com/photos/20395267/pexels-photo-20395267.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Butter Chicken': 'https://images.pexels.com/photos/29685054/pexels-photo-29685054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Paneer Tikka Masala': 'https://images.pexels.com/photos/30858402/pexels-photo-30858402.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Dal Makhani': 'https://images.pexels.com/photos/37182514/pexels-photo-37182514.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Garlic Naan': 'https://images.pexels.com/photos/10337726/pexels-photo-10337726.jpeg?auto=compress&cs=tinysrgb&w=800',
    # Chinese Express (5)
    'Hakka Noodles': 'https://images.pexels.com/photos/2764905/pexels-photo-2764905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Chicken Fried Rice': 'https://images.pexels.com/photos/34668502/pexels-photo-34668502.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Veg Manchurian': 'https://images.pexels.com/photos/35066808/pexels-photo-35066808.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Spring Rolls': 'https://images.pexels.com/photos/35407775/pexels-photo-35407775.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Chili Chicken': 'https://images.pexels.com/photos/5339083/pexels-photo-5339083.jpeg?auto=compress&cs=tinysrgb&w=800',
    # veggies (5)
    'Paneer Fried Rice': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMUSOkW6xq2izua5XRhxKlwMydHly1iBIxxg&s',
    'Vegetable Biryani': 'https://images.pexels.com/photos/9609848/pexels-photo-9609848.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Masala Dosa': 'https://images.pexels.com/photos/12392915/pexels-photo-12392915.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Chole Bhature': 'https://images.pexels.com/photos/36388454/pexels-photo-36388454.jpeg?auto=compress&cs=tinysrgb&w=800',
    'Veg Pulao': 'https://vegecravings.com/wp-content/uploads/2016/07/veg-pulao-recipe-step-by-step-instructions.jpg',
    # Cake De Lite (5)
    'Chocolate Truffle': 'https://images.pexels.com/photos/34802628/pexels-photo-34802628.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Pineapple Cake': 'https://images.pexels.com/photos/8820012/pexels-photo-8820012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Red Velvet Pastry': 'https://images.unsplash.com/photo-1586788680434-30d324b2d46f?q=80&w=1000&auto=format&fit=crop',
    'Blueberry Muffin': 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?q=80&w=1000&auto=format&fit=crop',
    'Vanilla Pastry': 'https://images.pexels.com/photos/10249466/pexels-photo-10249466.jpeg?auto=compress&cs=tinysrgb&w=800',
    # Frozen Bottle (5)
    'Belgian Chocolate': 'https://imagedelivery.net/EtcVECyqIuOr1FjP12iTCg/eb06eec2-bf26-4b24-1bdb-5fa07c7be600/w=300',
    'Strawberry Shake': 'https://static.wixstatic.com/media/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg',
    'Cold Coffee': 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?q=80&w=1000&auto=format&fit=crop',
    'Oreo Overload': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?q=80&w=1000&auto=format&fit=crop',
    'KitKat Shake': 'https://images.pexels.com/photos/20205940/pexels-photo-20205940.jpeg?auto=compress&cs=tinysrgb&w=800',
}

for name, url in mapping.items():
    Item.objects.filter(name=name).update(picture=url)
    
print(f"[OK] Updated {len(mapping)} items with correct image URLs")

# Verify fixes
items = Item.objects.all()
print(f"\n[OK] Verification - Total items: {items.count()}")
bad_items = items.filter(picture='')
if bad_items.exists():
    print(f"[WARN] {bad_items.count()} items still missing images: {', '.join([i.name for i in bad_items[:5]])}")
else:
    print(f"[OK] All items have images assigned")

sample = items[:3]
for i in sample:
    print(f"  - {i.name}: URL length={len(i.picture)} chars")
