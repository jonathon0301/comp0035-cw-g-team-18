# Data preparation and understanding

## Data Preparation

### Description of Initial Data from GOV.UK
The dataset shows the gender pay gap situations reported from different companies in various sizes and 
from different regions. It consists of six separate csv spreadsheets, which show situations from reporting
year 2017-18 to 2022-23 respectively. Each spreadsheet has the same 27 columns which can ba grouped into
three categories:

| Company Basic Info                                                                                                                       | Gender Pay Gap Figures                                                                                                                                                                                                                                                                                                 | Submission Time                                   |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| EmployerName, EmployerID, Address, PostCode, CompanyNumber, SicCodes, CompanyLinkToGPGInfo, ResponsiblePerson, EmployerSize, CurrentName | DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent, MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile, FemaleLowerQuartile, MaleLowerMiddleQuartile, FemaleLowerMiddleQuartile, MaleUpperMiddleQuartile, FemaleUpperMiddleQuartile, MaleTopQuartile, FemaleTopQuartile | SubmittedAfterTheDeadline, DueDate, DateSubmitted |
                                                                                                                                                                                                                                                                                                                                                                                                            

