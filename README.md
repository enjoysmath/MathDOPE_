# Abstract Spacecraft #

Abstract Spacecraft is a responsive web application for editing commutative diagrams using the well-known __[Quiver CD Editor](http://q.uiver.app)__.

Here is Quiver's repository: https://github.com/varkor/quiver

The version of Quiver (which for technical reasons we had to include) found within this repository was forked from Quiver's master branch on December 29, 2021.  Only slight modifications have been made so far to Quiver's source, but we may need to totally remove its orginal GUI buttons (would entail JS code editing) in order to make a more efficently loaded web app.  Currently we just disable them in CSS with `display: none`.

Additionally, we've outfitted it with a __Neo4j graph database__ for storing these commutative diagrams (CD's) and thus eventually for the purpose of constructing human-readable proofs in the areas of __Category Theory, Homological Algebra, Topos Theory__, etc.  That is, usually any abstract math area that is arrow-theoretic.

These definitions & proofs will then be freely accessible to math enthusiasts on the web, via their phone, table, or desktop computer.

We need to find someway to monetize slightly, even if only to support the Neo4j server costs.  However, that can be considered a software feature, and so the simplest solution is to have everything be free at first.

And I'd like people to work with me on this code before forking it, which is mainly why it's currently a private repo.

### Technology stack: ###
* Bootstrap Studio + django-bootstrap5 + BSS to Django export script
* Django / Python 3 / SQLite
* Neo4j graph DB + Django Neomodel Python library
* Aura DB managed Neo4j host
* HTML / CSS / Javascript (Quiver is mainly JS-coded)

### Current live version of the site: ###
[(TODO)](http://www.heroku.com)

### How do I get set up as a developer? ###

1. Purchase a $30 license for Bootstrap Studio (or borrow someone's license seat).
2. Clone this repository to your (Windows for now) desktop.
3. Have Python 3 already installed and on your path.
4. Download and install [Wingware Pro](https://wingware.com/downloads/wing-pro) for a Python IDE.  Alternatively, import the project files into your favorite IDE, say PyCharm, and add your project file to this source repo, as well as a note here.
5. Open the `abstract_spacecraft.wpr` Wingware project.  Wait for it to load and analyze certain parts.  
6. Do `pip install -r requirements.txt` from a command line, when in the Django root of this project (i.e. where `manage.py` is located).
7. With the project open in Wing, click the Run/Debug button.  It should now report no errors in the Debug I/O pane of the Wing IDE, and also say to point your web browser at the address: [http://127.0.0.1:8000](http://127.0.0.1:8000).

### Deployment to Heroku & Aura DB ###
1. [Install Heroku CLI & follow Getting Started instructions](https://devcenter.heroku.com/articles/heroku-cli)
2. [Follow these deployment instructions](https://devcenter.heroku.com/articles/preparing-a-codebase-for-heroku-deployment)

### Videos of current state of the project ###
_(Most recent are listed first)_

1. [Got CD saved to DB](https://youtu.be/lp1dGmL8qQk)

2. (Coming soon!)
