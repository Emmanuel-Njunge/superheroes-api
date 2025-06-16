from app import app
from models import db, Hero, Power, HeroPower

with app.app_context():
    db.drop_all()
    db.create_all()

    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]

    powers = [
    Power(name="super strength", description="gives the wielder super-human strengths"),
    Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
    Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
    Power(name="elasticity", description="can stretch the human body to extreme lengths"),
    Power(name="telepathy", description="enables mind reading and communication through thoughts"),
    Power(name="invisibility", description="grants the ability to become unseen at will"),
    Power(name="energy blasts", description="allows the user to release powerful energy beams"),
    Power(name="telekinesis", description="gives the ability to move objects with the mind"),
]


    db.session.add_all(heroes + powers)
    db.session.commit()

    hero_powers = [
        HeroPower(strength="Average", hero_id=2, power_id=1),
        HeroPower(strength="Weak", hero_id=3, power_id=4),
        HeroPower(strength="Strong", hero_id=4, power_id=3),
        HeroPower(strength="Strong", hero_id=5, power_id=2),
        HeroPower(strength="Weak", hero_id=6, power_id=1),
        HeroPower(strength="Average", hero_id=7, power_id=2),
        HeroPower(strength="Strong", hero_id=8, power_id=4),
        HeroPower(strength="Weak", hero_id=9, power_id=3),
        HeroPower(strength="Average", hero_id=10, power_id=1),
    ]

    db.session.add_all(hero_powers)
    db.session.commit()
    print("🌱 Seeding complete!")

