import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'meal_buddy.settings')
django.setup()

from delivery.models import Item

# Clear all corrupted picture data
Item.objects.all().update(picture='')
print("✓ Cleared all corrupted picture data")

# Restore correct Unsplash URLs
mapping = {
    'farmhouse pizza': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800&q=80',
    'cheese burst pizza': 'https://images.unsplash.com/photo-1601924534193-9d79f1f09b71?w=800&q=80',
    'garlic bread': 'https://images.unsplash.com/photo-1540189549336-e6e99c3679fe?w=800&q=80',
    'alfredo pasta': 'https://images.unsplash.com/photo-1512058564366-c9d84e6d0f0c?w=800&q=80',
    'chocolate shake': 'https://images.unsplash.com/photo-1601924638867-3ec8d5a911f9?w=800&q=80',
    'fries': 'https://images.unsplash.com/photo-1551892589-865f69869449?w=800&q=80',
    'Classic Cheeseburger': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=80',
    'Spicy Chicken Burger': 'https://images.unsplash.com/photo-1562547256-fa1bef46e7d8?w=800&q=80',
    'Veggie Burger': 'https://images.unsplash.com/photo-1585238341710-4913de44e5a8?w=800&q=80',
    'Hyderabadi Biryani': 'https://images.unsplash.com/photo-1622311483299-152b9cc86ea2?w=800&q=80',
    'Paneer Tikka Biryani': 'https://images.unsplash.com/photo-1623325325314-0b9d173d0388?w=800&q=80',
    'Chicken Tikka Rice': 'https://images.unsplash.com/photo-1604908177521-58b4da1bbfc5?w=800&q=80',
    'Margherita Pizza': 'https://images.unsplash.com/photo-1604068549290-dea0e4a305ca?w=800&q=80',
    'Pepperoni Pizza': 'https://images.unsplash.com/photo-1628840042765-356cda07f4ee?w=800&q=80',
    'Veggie Supreme Pizza': 'https://images.unsplash.com/photo-1511689915289-025f5b846b35?w=800&q=80',
    'Butter Chicken': 'https://images.unsplash.com/photo-1608239366580-361798d2d6a3?w=800&q=80',
    'Paneer Makhani': 'https://images.unsplash.com/photo-1604908176627-93b6b1b3fa3f?w=800&q=80',
    'Chole Bhature': 'https://images.unsplash.com/photo-1589923188900-2e3da6214f1a?w=800&q=80',
    'Hakka Noodles': 'https://images.unsplash.com/photo-1608837035181-8d0d2e98ca84?w=800&q=80',
    'Chicken Fried Rice': 'https://images.unsplash.com/photo-1596103442097-8ad28f25ff91?w=800&q=80',
    'Shrimp Pad Thai': 'https://images.unsplash.com/photo-1626082927389-6cd097cdc46e?w=800&q=80',
    'Chicken Shawarma': 'https://images.unsplash.com/photo-1599599810694-b5ac4dd33e2b?w=800&q=80',
    'Falafel Wrap': 'https://images.unsplash.com/photo-1585238341710-4913de44e5a8?w=800&q=80',
    'Grilled Paneer Wrap': 'https://images.unsplash.com/photo-1599599810236-8b8218e3a89c?w=800&q=80',
    'Gulab Jamun': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&q=80',
    'Chocolate Cake': 'https://images.unsplash.com/photo-1578985545062-69928b1d9587?w=800&q=80',
    'Ice Cream Sundae': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=80',
}

for name, url in mapping.items():
    Item.objects.filter(name=name).update(picture=url)
    
print(f"✓ Updated {len(mapping)} items with correct image URLs")

# Verify fixes
items = Item.objects.all()
print(f"\n✓ Verification - Total items: {items.count()}")
bad_items = items.filter(picture='')
if bad_items.exists():
    print(f"⚠ {bad_items.count()} items still missing images: {', '.join([i.name for i in bad_items[:5]])}")
else:
    print(f"✓ All items have images assigned")

sample = items[:3]
for i in sample:
    print(f"  - {i.name}: URL length={len(i.picture)} chars")
