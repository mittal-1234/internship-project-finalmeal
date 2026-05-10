import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
django.setup()

from delivery.models import Item

# Clear all corrupted picture data
Item.objects.all().update(picture='')
print("[OK] Cleared all corrupted picture data")

# Restore correct Unsplash URLs
mapping = {
    'farmhouse pizza': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=1000&auto=format&fit=crop',
    'cheese burst pizza': 'https://images.unsplash.com/photo-1601924534193-9d79f1f09b71?q=80&w=1000&auto=format&fit=crop',
    'Chocolate Waffle': 'https://images.unsplash.com/photo-1562376552-0d160a2f238d?q=80&w=1000&auto=format&fit=crop',
    'Strawberry Waffle': 'https://images.unsplash.com/photo-1459789034005-ba29c5783491?q=80&w=1000&auto=format&fit=crop',
    'garlic bread': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?q=80&w=1000&auto=format&fit=crop',
    'alfredo pasta': 'https://images.unsplash.com/photo-1512058564366-c9d84e6d0f0c?q=80&w=1000&auto=format&fit=crop',
    'chocolate shake': 'https://images.unsplash.com/photo-1601924638867-3ec8d5a911f9?q=80&w=1000&auto=format&fit=crop',
    'fries': 'https://images.unsplash.com/photo-1551892589-865f69869449?q=80&w=1000&auto=format&fit=crop',
    'Classic Cheeseburger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1000&auto=format&fit=crop',
    'Spicy Chicken Burger': 'https://images.unsplash.com/photo-1562547256-fa1bef46e7d8?q=80&w=1000&auto=format&fit=crop',
    'Veggie Burger': 'https://images.unsplash.com/photo-1520072959219-c595dc870360?q=80&w=1000&auto=format&fit=crop',
    'Hyderabadi Biryani': 'https://images.unsplash.com/photo-1622311483299-152b9cc86ea2?q=80&w=1000&auto=format&fit=crop',
    'Paneer Tikka Biryani': 'https://images.unsplash.com/photo-1623325325314-0b9d173d0388?q=80&w=1000&auto=format&fit=crop',
    'Chicken Tikka Rice': 'https://images.unsplash.com/photo-1604908177521-58b4da1bbfc5?q=80&w=1000&auto=format&fit=crop',
    'Margherita Pizza': 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Pizza_Margherita_stu_spivack.jpg',
    'Pepperoni Pizza': 'https://images.unsplash.com/photo-1628840042765-356cda07504e?q=80&w=1000&auto=format&fit=crop',
    'Veggie Supreme Pizza': 'https://images.unsplash.com/photo-1511689915289-025f5b846b35?q=80&w=1000&auto=format&fit=crop',
    'Butter Chicken': 'https://images.pexels.com/photos/29685054/pexels-photo-29685054.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Paneer Tikka': 'https://images.pexels.com/photos/3928854/pexels-photo-3928854.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Paneer Makhani': 'https://images.unsplash.com/photo-1604908176627-93b6b1b3fa3f?q=80&w=1000&auto=format&fit=crop',
    'Chole Bhature': 'https://images.unsplash.com/photo-1589923188900-2e3da6214f1a?q=80&w=1000&auto=format&fit=crop',
    'Hakka Noodles': 'https://images.pexels.com/photos/2764905/pexels-photo-2764905.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Chicken Fried Rice': 'https://images.pexels.com/photos/34668502/pexels-photo-34668502.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Paneer Fried Rice': 'https://images.pexels.com/photos/31783383/pexels-photo-31783383.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Shrimp Pad Thai': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc46e?q=80&w=1000&auto=format&fit=crop',
    'Chicken Shawarma': 'https://images.unsplash.com/photo-1599599810694-b5ac4dd33e2b?q=80&w=1000&auto=format&fit=crop',
    'Falafel Wrap': 'https://images.unsplash.com/photo-1585238341710-4913de44e5a8?q=80&w=1000&auto=format&fit=crop',
    'Grilled Paneer Wrap': 'https://images.unsplash.com/photo-1599599810236-8b8218e3a89c?q=80&w=1000&auto=format&fit=crop',
    'Gulab Jamun': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?q=80&w=1000&auto=format&fit=crop',
    'Chocolate Cake': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?q=80&w=1000&auto=format&fit=crop',
    'Ice Cream Sundae': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?q=80&w=1000&auto=format&fit=crop',
    'Chocolate Truffle': 'https://images.pexels.com/photos/34802628/pexels-photo-34802628.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Pineapple Cake': 'https://images.pexels.com/photos/8820012/pexels-photo-8820012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'Red Velvet Pastry': 'https://images.unsplash.com/photo-1586788680434-30d324b2d46f?q=80&w=1000&auto=format&fit=crop',
    'Blueberry Muffin': 'https://images.unsplash.com/photo-1550617931-e17a7b70dce2?q=80&w=1000&auto=format&fit=crop',
    'Belgian Chocolate': 'https://imagedelivery.net/EtcVECyqIuOr1FjP12iTCg/eb06eec2-bf26-4b24-1bdb-5fa07c7be600/w=300',
    'Strawberry Shake': 'https://static.wixstatic.com/media/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg/v1/fill/w_256,h_256,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/567605_55130247aebd43f997572cc7dc472fb8~mv2.jpeg',
    'Cold Coffee': 'https://images.unsplash.com/photo-1517701604599-bb29b565090c?q=80&w=1000&auto=format&fit=crop',
    'Oreo Overload': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?q=80&w=1000&auto=format&fit=crop',
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
