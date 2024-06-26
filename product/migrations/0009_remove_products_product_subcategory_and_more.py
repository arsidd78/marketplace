# Generated by Django 5.0.4 on 2024-05-12 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_products_product_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_subcategory',
        ),
        migrations.AlterField(
            model_name='products',
            name='product_category',
            field=models.CharField(choices=[('ELECTRONICS', 'Electronics'), ('CLOTHING & ACCESSORIES', 'Clothing & Accessories'), ('HOME & KITCHEN', 'Home & Kitchen'), ('BEAUTY & PERSONAL CARE', 'Beauty & Personal Care'), ('HEALTH & FITNESS', 'Health & Fitness'), ('TOYS & GAMES', 'Toys & Games'), ('BOOKS & MEDIA', 'Books & Media'), ('AUTOMOTIVE', 'Automotive'), ('SPORTS & OUTDOORS', 'Sports & Outdoors'), ('PET SUPPLIES', 'Pet Supplies'), ('HOME APPLIANCES', 'Home Appliances'), ('OFFICE SUPPLIES', 'Office Supplies'), ('FURNITURE & DECOR', 'Furniture & Decor'), ('JEWELRY & WATCHES', 'Jewelry & Watches'), ('BABY & TODDLER', 'Baby & Toddler'), ('FOOD & GROCERIES', 'Food & Groceries'), ('ARTS & CRAFTS', 'Arts & Crafts'), ('MUSICAL INSTRUMENTS', 'Musical Instruments'), ('GARDEN & OUTDOOR LIVING', 'Garden & Outdoor Living'), ('TRAVEL & LUGGAGE', 'Travel & Luggage'), ('SMARTPHONE', 'Smartphone'), ('LAPTOP', 'Laptop'), ('CAMERA', 'Camera'), ('TV', 'TV'), ('HEADPHONE', 'Headphone'), ('GADGET', 'Gadget'), ('APPAREL', 'Apparel'), ('BAG', 'Bag'), ('JEWELRY', 'Jewelry'), ('SUNGLASSES', 'Sunglasses'), ('WATCH', 'Watch'), ('HOME IMPROVEMENT', 'Home Improvement'), ('DECOR', 'Decor'), ('KITCHEN APPLIANCES', 'Kitchen Appliances'), ('COOKWARE', 'Cookware'), ('FURNITURE', 'Furniture'), ('SKINCARE', 'Skincare'), ('MAKEUP', 'Makeup'), ('HAIRCARE', 'Haircare'), ('GROOMING', 'Grooming'), ('FRAGRANCES', 'Fragrances'), ('EXERCISE EQUIPMENT', 'Exercise Equipment'), ('NUTRITIONAL SUPPLEMENTS', 'Nutritional Supplements'), ('FITNESS TRACKERS', 'Fitness Trackers'), ('YOGA MATS', 'Yoga Mats'), ('TOYS', 'Toys'), ('BOARD GAMES', 'Board Games'), ('PUZZLES', 'Puzzles'), ('EDUCATIONAL TOYS', 'Educational Toys'), ('OUTDOOR PLAY EQUIPMENT', 'Outdoor Play Equipment'), ('BOOKS', 'Books'), ('E-BOOKS', 'E-books'), ('AUDIOBOOKS', 'Audiobooks'), ('DVDS', 'DVDs'), ('CDS', 'CDs'), ('DIGITAL MEDIA', 'Digital Media'), ('CAR PARTS', 'Car Parts'), ('ACCESSORIES', 'Accessories'), ('TOOLS', 'Tools'), ('MAINTENANCE SUPPLIES', 'Maintenance Supplies'), ('SPORTING EQUIPMENT', 'Sporting Equipment'), ('CAMPING GEAR', 'Camping Gear'), ('HIKING GEAR', 'Hiking Gear'), ('OUTDOOR CLOTHING', 'Outdoor Clothing'), ('FOOD', 'Food'), ('GROOMING PRODUCTS', 'Grooming Products'), ('BEDS', 'Beds'), ('CARRIERS', 'Carriers'), ('LARGE APPLIANCES', 'Large Appliances'), ('SMALL APPLIANCES', 'Small Appliances'), ('STATIONERY', 'Stationery'), ('DESK ORGANIZERS', 'Desk Organizers'), ('PRINTERS', 'Printers'), ('OFFICE FURNITURE', 'Office Furniture'), ('TECHNOLOGY ACCESSORIES', 'Technology Accessories'), ('SOFAS', 'Sofas'), ('CHAIRS', 'Chairs'), ('TABLES', 'Tables'), ('LIGHTING FIXTURES', 'Lighting Fixtures'), ('RUGS', 'Rugs'), ('RINGS', 'Rings'), ('NECKLACES', 'Necklaces'), ('BRACELETS', 'Bracelets'), ('EARRINGS', 'Earrings'), ('WATCHES', 'Watches'), ('CLOTHING', 'Clothing'), ('DIAPERS', 'Diapers'), ('FEEDING SUPPLIES', 'Feeding Supplies'), ('STROLLERS', 'Strollers'), ('NON-PERISHABLE FOOD', 'Non-perishable Food'), ('SNACKS', 'Snacks'), ('BEVERAGES', 'Beverages'), ('GOURMET FOODS', 'Gourmet Foods'), ('SPICES', 'Spices'), ('ART SUPPLIES', 'Art Supplies'), ('CRAFTING MATERIALS', 'Crafting Materials'), ('DIY KITS', 'DIY Kits'), ('SEWING SUPPLIES', 'Sewing Supplies'), ('GUITARS', 'Guitars'), ('KEYBOARDS', 'Keyboards'), ('DRUMS', 'Drums'), ('VIOLINS', 'Violins'), ('WIND INSTRUMENTS', 'Wind Instruments'), ('GARDENING TOOLS', 'Gardening Tools'), ('PLANTS', 'Plants'), ('OUTDOOR FURNITURE', 'Outdoor Furniture'), ('BBQ GRILLS', 'BBQ Grills'), ('LUGGAGE SETS', 'Luggage Sets'), ('BACKPACKS', 'Backpacks'), ('TRAVEL ACCESSORIES', 'Travel Accessories'), ('TOILETRIES', 'Toiletries'), ('OUTDOOR GEAR', 'Outdoor Gear')], max_length=100, verbose_name='category'),
        ),
    ]
