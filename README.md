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
1. Install `flask` and `flask_mysqldb`. 
2. Clone this repository and add GoogleAPIKey and the mysql root password for your system in the configuration files.
3. Replicate the schema and add entries as required. Don't forget to put your photo files in the `/static/` directory. 
4. Run `python myTravelMap.py`
5. Open `http://127.0.0.1:5000/` in a browser. 

### TODO
- [x] Push SQL dump. 
- [ ] Heroku Deployment. 
- [ ] UI for adding into db. 
- [ ] Changing infoview style to look better. 
