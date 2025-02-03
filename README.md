# LOL-matchups-scraper
Web scraper used to scrape data from lolalytics website for matchups analysis.

Used to create a spreadsheet of normalised matchup win rate deltas. 
To generate the up-to-date spreadsheet, simply run the spreadsheetCreator script in the command line with the following args:

--key : one of [base, delta1, delta2]
    
--filename : the name of the output spreadsheet including .xlsx extension

#### Example
```
python spreadsheetCreator --key delta2 --filename matchups.xlsx
```

## Generated Matchups Spreadsheet
![sheet](/images/matchups_ss.png)

### Built With
- Beautiful Soup 4
- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)


## Authors
- Ling Chen, LingC2001@gmail.com
