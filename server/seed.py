from app import app, db, Hero, Power, HeroPower

def seed_data():
    with app.app_context():
        # Create example powers
        # Create example powers
        power1 = Power(name="Super Strength", description="Superhuman strength with extra power")
        power2 = Power(name="Flight", description="Ability to fly very high")
        power3 = Power(name="Telepathy", description="Mind-reading capability")


        # Create example heroes
        hero1 = Hero(name="Superman", super_name="Clark Kent")
        hero2 = Hero(name="Wonder Woman", super_name="Diana Prince")
        hero3 = Hero(name="Spider-Man", super_name="Peter Parker")

        # Create hero-power relationships
        hero_power1 = HeroPower(strength="Strong", hero=hero1, power=power1)
        hero_power2 = HeroPower(strength="Average", hero=hero2, power=power2)
        hero_power3 = HeroPower(strength="Weak", hero=hero3, power=power3)

        # Add objects to the session and commit
        db.session.add_all([power1, power2, power3, hero1, hero2, hero3, hero_power1, hero_power2, hero_power3])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully.')
