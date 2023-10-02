from app import app, db, Hero, Power, HeroPower

def seed_data():
    with app.app_context():
        # Create example powers
        power1 = Power(name="Super Strength", description="Superhuman strength with extra power")
        power2 = Power(name="Flight", description="Ability to fly very high")
        power3 = Power(name="Telepathy", description="Mind-reading capability")
        power4 = Power(name="Invisibility", description="Ability to become invisible")
        power5 = Power(name="Telekinesis", description="Move objects with the mind")
        power6 = Power(name="Super Speed", description="Incredible speed and agility")

        # Create example heroes
        hero1 = Hero(name="Superman", super_name="Clark Kent")
        hero2 = Hero(name="Wonder Woman", super_name="Diana Prince")
        hero3 = Hero(name="Spider-Man", super_name="Peter Parker")
        hero4 = Hero(name="Batman", super_name="Bruce Wayne")
        hero5 = Hero(name="Green Arrow", super_name="Oliver Queen")
        hero6 = Hero(name="The Flash", super_name="Barry Allen")

        # Create hero-power relationships
        hero_power1 = HeroPower(strength="Strong", hero=hero1, power=power1)
        hero_power2 = HeroPower(strength="Average", hero=hero2, power=power2)
        hero_power3 = HeroPower(strength="Weak", hero=hero3, power=power3)
        hero_power4 = HeroPower(strength="Strong", hero=hero4, power=power4)
        hero_power5 = HeroPower(strength="Average", hero=hero5, power=power5)
        hero_power6 = HeroPower(strength="Strong", hero=hero6, power=power6)

        # Add objects to the session and commit
        db.session.add_all([power1, power2, power3, power4, power5, power6, hero1, hero2, hero3, hero4, hero5, hero6, hero_power1, hero_power2, hero_power3, hero_power4, hero_power5, hero_power6])
        db.session.commit()

if __name__ == '__main__':
    seed_data()
    print('Database seeded successfully with additional powers and hero-power relationships.')
