from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class Products(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField(max_length=500)
    product_price = models.DecimalField('Price',max_digits=7,decimal_places=2)
    product_discounted_price = models.DecimalField('Discounted Price',max_digits=7,decimal_places=2,null=True,blank=True)
    product_delivery_charge = models.IntegerField(default=0)
    product_tax_rate = models.DecimalField(decimal_places=3,max_digits=5, null= True, blank= True)
    product_specification = models.TextField(null= True, blank= True)
    product_posted_date = models.DateField( auto_now_add=True)
    product_images = models.ImageField(upload_to='products/')
    product_images2 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images3 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images4 = models.ImageField(null=True,blank=True,upload_to='products/')
    product_images5 = models.ImageField(null=True,blank=True,upload_to='products/')
    categories_choices = product_categories = {
    "ELECTRONICS": "Electronics",
    "CLOTHING & ACCESSORIES": "Clothing & Accessories",
    "HOME & KITCHEN": "Home & Kitchen",
    "BEAUTY & PERSONAL CARE": "Beauty & Personal Care",
    "HEALTH & FITNESS": "Health & Fitness",
    "TOYS & GAMES": "Toys & Games",
    "BOOKS & MEDIA": "Books & Media",
    "AUTOMOTIVE": "Automotive",
    "SPORTS & OUTDOORS": "Sports & Outdoors",
    "PET SUPPLIES": "Pet Supplies",
    "HOME APPLIANCES": "Home Appliances",
    "OFFICE SUPPLIES": "Office Supplies",
    "FURNITURE & DECOR": "Furniture & Decor",
    "JEWELRY & WATCHES": "Jewelry & Watches",
    "BABY & TODDLER": "Baby & Toddler",
    "FOOD & GROCERIES": "Food & Groceries",
    "ARTS & CRAFTS": "Arts & Crafts",
    "MUSICAL INSTRUMENTS": "Musical Instruments",
    "GARDEN & OUTDOOR LIVING": "Garden & Outdoor Living",
    "TRAVEL & LUGGAGE": "Travel & Luggage",
    "SMARTPHONE": "Smartphone",
    "LAPTOP": "Laptop",
    "CAMERA": "Camera",
    "TV": "TV",
    "HEADPHONE": "Headphone",
    "GADGET": "Gadget",
    "APPAREL": "Apparel",
    "BAG": "Bag",
    "JEWELRY": "Jewelry",
    "SUNGLASSES": "Sunglasses",
    "WATCH": "Watch",
    "HOME IMPROVEMENT": "Home Improvement",
    "DECOR": "Decor",
    "KITCHEN APPLIANCES": "Kitchen Appliances",
    "COOKWARE": "Cookware",
    "FURNITURE": "Furniture",
    "SKINCARE": "Skincare",
    "MAKEUP": "Makeup",
    "HAIRCARE": "Haircare",
    "GROOMING": "Grooming",
    "FRAGRANCES": "Fragrances",
    "EXERCISE EQUIPMENT": "Exercise Equipment",
    "NUTRITIONAL SUPPLEMENTS": "Nutritional Supplements",
    "FITNESS TRACKERS": "Fitness Trackers",
    "YOGA MATS": "Yoga Mats",
    "TOYS": "Toys",
    "BOARD GAMES": "Board Games",
    "PUZZLES": "Puzzles",
    "EDUCATIONAL TOYS": "Educational Toys",
    "OUTDOOR PLAY EQUIPMENT": "Outdoor Play Equipment",
    "BOOKS": "Books",
    "E-BOOKS": "E-books",
    "AUDIOBOOKS": "Audiobooks",
    "DVDS": "DVDs",
    "CDS": "CDs",
    "DIGITAL MEDIA": "Digital Media",
    "CAR PARTS": "Car Parts",
    "ACCESSORIES": "Accessories",
    "TOOLS": "Tools",
    "MAINTENANCE SUPPLIES": "Maintenance Supplies",
    "ELECTRONICS": "Electronics",
    "SPORTING EQUIPMENT": "Sporting Equipment",
    "CAMPING GEAR": "Camping Gear",
    "HIKING GEAR": "Hiking Gear",
    "OUTDOOR CLOTHING": "Outdoor Clothing",
    "FOOD": "Food",
    "TOYS": "Toys",
    "GROOMING PRODUCTS": "Grooming Products",
    "BEDS": "Beds",
    "CARRIERS": "Carriers",
    "LARGE APPLIANCES": "Large Appliances",
    "SMALL APPLIANCES": "Small Appliances",
    "STATIONERY": "Stationery",
    "DESK ORGANIZERS": "Desk Organizers",
    "PRINTERS": "Printers",
    "OFFICE FURNITURE": "Office Furniture",
    "TECHNOLOGY ACCESSORIES": "Technology Accessories",
    "SOFAS": "Sofas",
    "CHAIRS": "Chairs",
    "TABLES": "Tables",
    "LIGHTING FIXTURES": "Lighting Fixtures",
    "RUGS": "Rugs",
    "RINGS": "Rings",
    "NECKLACES": "Necklaces",
    "BRACELETS": "Bracelets",
    "EARRINGS": "Earrings",
    "WATCHES": "Watches",
    "CLOTHING": "Clothing",
    "DIAPERS": "Diapers",
    "FEEDING SUPPLIES": "Feeding Supplies",
    "STROLLERS": "Strollers",
    "TOYS": "Toys",
    "NON-PERISHABLE FOOD": "Non-perishable Food",
    "SNACKS": "Snacks",
    "BEVERAGES": "Beverages",
    "GOURMET FOODS": "Gourmet Foods",
    "SPICES": "Spices",
    "ART SUPPLIES": "Art Supplies",
    "CRAFTING MATERIALS": "Crafting Materials",
    "DIY KITS": "DIY Kits",
    "SEWING SUPPLIES": "Sewing Supplies",
    "GUITARS": "Guitars",
    "KEYBOARDS": "Keyboards",
    "DRUMS": "Drums",
    "VIOLINS": "Violins",
    "WIND INSTRUMENTS": "Wind Instruments",
    "GARDENING TOOLS": "Gardening Tools",
    "PLANTS": "Plants",
    "OUTDOOR FURNITURE": "Outdoor Furniture",
    "BBQ GRILLS": "BBQ Grills",
    "LUGGAGE SETS": "Luggage Sets",
    "BACKPACKS": "Backpacks",
    "TRAVEL ACCESSORIES": "Travel Accessories",
    "TOILETRIES": "Toiletries",
    "OUTDOOR GEAR": "Outdoor Gear"
    }

    product_category = models.CharField('category',max_length=100,choices=categories_choices)
    product_quantity = models.PositiveIntegerField()
    sellor_name = models.CharField(max_length=100)
    company_name = models.CharField(null= True, blank= True, max_length=200)
    product_website = models.URLField(null= True,blank=True)
    def __str__(self) -> str:
        return self.product_name
            
class Purchase(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    sellor = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='sellor')
    quantity = models.PositiveIntegerField()     
    price = models.DecimalField(max_digits=7,decimal_places=2)
    date = models.DateField(auto_now_add=True)
    posted_time = models.DateTimeField(auto_now_add= True)
    read = models.BooleanField(default=False)
    buyer = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    buyer_phone = models.CharField(max_length=13)
    buyer_address = models.CharField(max_length=200)
    buyer_city = models.CharField(max_length=100)
    buyer_state = models.CharField(max_length=100)
    buyer_zip_code = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.product.product_name

class Reviews(models.Model):

    product = models.ForeignKey(Products, on_delete= models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete= models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField()
    posted_time = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.review
    
