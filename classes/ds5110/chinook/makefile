URL=https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite

# most popular tracks
q1:data/chinook.db
	python -B src/exercise1.py

# most expensive invoice
q2:data/chinook.db
	python -B src/excersie2.py

# table info
q3:data/chinook.db
	python -B src/excersise3.py


# Plot histogram
hist: data/chinook.db
	mkdir -p figs
	python -B src/main.py

# Create the database from the text file with SQL commands
data/chinook.db: data/Chinook_Sqlite.sql
	sqlite3 data/chinook.db < data/Chinook_Sqlite.sql

# Get the SQL (and a copy of the database)
data/Chinook_Sqlite.sql:
	mkdir -p data
	cd data; curl -LO $(URL).sqlite
	cd data; curl -LO $(URL).sql

clean:
	rm data/chinook.db
