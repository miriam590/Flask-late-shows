from app import app, db
from models import Episode, Guest, Appearance

def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        episodes = [
            Episode(date="3/20/01", number=7),  
            Episode(date="4/25/01", number=8),  
            Episode(date="5/15/01", number=9),
            Episode(date="6/12/01", number=10),
            Episode(date="7/18/01", number=11),
            Episode(date="8/22/01", number=12)
        ]
        db.session.add_all(episodes)

        guests = [
            Guest(name="miriam yego", occupation="actress"),
            Guest(name="christine maina", occupation="comedian"),
            Guest(name="dahine muchere", occupation="radio presenter"),  
            Guest(name="james ngugi", occupation="author"),
            Guest(name="alice mutuku", occupation="chef"),
            Guest(name="mark odinga", occupation="musician"),
            Guest(name="lucy wanjiku", occupation="journalist"),
            Guest(name="paul mwangi", occupation="scientist")
        ]
        db.session.add_all(guests)

        appearances = [
            Appearance(rating=4, episode_id=10, guest_id=1),  
            Appearance(rating=3, episode_id=11, guest_id=2),  
            Appearance(rating=5, episode_id=12, guest_id=3),
            Appearance(rating=4, episode_id=10, guest_id=4),
            Appearance(rating=5, episode_id=11, guest_id=5),
            Appearance(rating=3, episode_id=12, guest_id=6),
            Appearance(rating=4, episode_id=7, guest_id=7),
            Appearance(rating=5, episode_id=8, guest_id=8)
        ]
        db.session.add_all(appearances)

        db.session.commit()

if __name__ == '__main__':
    seed_database()
