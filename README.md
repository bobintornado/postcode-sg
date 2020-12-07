# Setup
```
conda create -n postcodessg python=3.9
pip install -r requirements.txt
```

# Plan
1. Have a worker run on free tier of Heroku project
2. Use PostgreSQL to save all the records (combine of a few must be unique)
3. Remove data older than 4 weeks?
4. Dump to CSV upon request
5. One query endpoint
