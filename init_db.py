from app import app, db, Product, User

def init_database():
    with app.app_context():
        # Drop all tables (CAUTION: This deletes all data!)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        print('✅ Database tables created!')
        
        # Check if admin user exists
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                email='admin@frozenkadai.com',
                phone='9999999999',
                address='Admin Address',
                password='admin123'
            )
            db.session.add(admin)
            print('✅ Admin user created!')
        
        # Add sample products if none exist
        if Product.query.count() == 0:
            products = [
                Product(name='Frozen Whole Chicken', 
                       description='Farm fresh whole chicken', 
                       price_per_kg=280, 
                       category='Whole Chicken',
                       image_file='whole-chicken.jpg',
                       stock_status='In Stock',
                       is_bestseller=True),
                Product(name='Chicken Breast', 
                       description='Boneless chicken breast', 
                       price_per_kg=450, 
                       category='Chicken',
                       image_file='chicken-breast.jpg',
                       stock_status='In Stock',
                       is_bestseller=True),
            ]
            for product in products:
                db.session.add(product)
            print(f'✅ Added {len(products)} sample products!')
        
        db.session.commit()
        print('🎉 Database initialization complete!')

if __name__ == '__main__':
    init_database()
