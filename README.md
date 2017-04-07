# Travel-Map
On the lines of instagram's photo map.

### Sample

<a href="http://tinypic.com?ref=2ed8589" target="_blank"><img src="http://i66.tinypic.com/2ed8589.png" border="0" alt="Image and video hosting by TinyPic"></a>

### Introduction
This is a python-flask-mysql application which lets you add markers to locations on the map and attach infoviews
containing photographs.

### Database
The scheme of the MySQL DB is:

Database Name: `TravelMap`

Table Name: `PHOTOS`

Attributes: `ID`, `PLACE` (Name of the place), `LAT` (Latitude), `LNG` (Longitude), `PHOTO`(Name of photo file)

The table creation has been put as a mysql dump in the file `db.sql`

### Running the app
1. Clone the repository
2. Create a virtualenv and in the environment, run `sudo -r pip install -r requirements.txt`. It's likely you will need to run `sudo apt-get install libmysqlclient-dev python-dev` before pip can install `flask-mysqldb`.
3. Add GoogleAPIKey and the mysql root password for your system in the configuration files.
4. Create a db with name `TravelMap` and run `mysql -u root -p TravelMap < db.sql` from the shell being in the root dir of the project. 
5. Run `python myTravelMap.py`
6. Open `http://127.0.0.1:5000/` in a browser. 

You can add entries into the db and add your pictures in the `/static/` folder to add them to the map. 

### TODO
- [x] Push SQL dump. 
- [ ] Heroku Deployment. 
- [ ] UI for adding into db. 
- [ ] Changing infoview style to look better. 
