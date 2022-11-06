# Data Preparation and Understanding

## Description of Initial Data from GOV.UK
The dataset shows the gender pay gap situations reported from different companies in various sizes and 
from different industries and regions. It consists of six separate csv spreadsheets, which show situations from reporting
year 2017-18 to 2022-23 respectively. It can be downloaded from [website of Gender Pay Gap Service of UK Government.](https://gender-pay-gap.service.gov.uk)
Each spreadsheet has the same 27 columns which can ba grouped into
three categories:

| Company Basic Info                                                                                                                       | Gender Pay Gap Figures                                                                                                                                                                                                                                                                                                 | Submission Time                                   |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| EmployerName, EmployerID, Address, PostCode, CompanyNumber, SicCodes, CompanyLinkToGPGInfo, ResponsiblePerson, EmployerSize, CurrentName | DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent, MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile, FemaleLowerQuartile, MaleLowerMiddleQuartile, FemaleLowerMiddleQuartile, MaleUpperMiddleQuartile, FemaleUpperMiddleQuartile, MaleTopQuartile, FemaleTopQuartile | SubmittedAfterTheDeadline, DueDate, DateSubmitted |
                                                                                                                                                                                                                                                                                                                                                                                                            
In case of data types, the 27 columns can also be grouped into three:

| Text                                                                                                                         | Numerical                                                                                                                                                                                                                                                                                                                          | Boolean                   |
|------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| EmployerName, Address, PostCode, CompanyNumber, SicCodes, CompanyLinkToGPGInfo, ResponsiblePerson, EmployerSize, CurrentName | EmployerId, DiffMeanHourlyPercent, DiffMedianHourlyPercent, DiffMeanBonusPercent, DiffMedianBonusPercent, MaleBonusPercent, FemaleBonusPercent, MaleLowerQuartile, FemaleLowerQuartile, MaleLowerMiddleQuartile, FemaleLowerMiddleQuartile, MaleUpperMiddleQuartile, FemaleUpperMiddleQuartile, MaleTopQuartile, FemaleTopQuartile | SubmittedAfterTheDeadline |

The number of rows of each table is shown below:

| Reporting Year | Rows      |
|----------------|-----------|
| 2017-18        | 10225     |
| 2018-19        | 10466     |
| 2019-20        | 6921      |
| 2020-21        | 10532     |
| 2021-22        | 10491     |
| 2022-23        | 353       |
|                |           |
| **Total**      | **48988** |

The exact meaning of each column can be checked from the original website. 
In case readers of this file do not have time to check on their own and some names are not quite intuitive, 
it is necessary to explain some vague meanings:

1. **SicCodes** represents Standard Industrial Classification code of the company at the time of submission, showing its nature of business;
2. All **Diff** values show the % difference between male and female, where the negative figures indicate female has higher pay;
3. The remaining **Gender Pay Gap Figures** represent the percentage of certain gender employee paid a bonus or in certain quarter of payment levels within their company.

## Data Preparation
After loading the six spreadsheets into the data_prep python file and looking at their basic information mentioned in 
the previous section, we decided to merge all the tables into one single dataframe they all contain the same columns. 
The merger is inconsequential as we do not expect the situation would vary a lot within these years and we do not plan 
to analyze in time series. Instead, we wish to have a look at the gender pay gap situation across different industries, 
regions and company sizes.
### Delete Unnecessary Columns
Since the time series are no loger considered, columns including 
**SubmittedAfterTheDeadline, DueDate & DateSubmitted** can be removed. Meanwhile, in order to protect privacy and 
prevent direct focus on a particular company, information including **Address, EmployerName, EmployerId, 
CompanyNumber, CompanyLinkToGPGInfo,ResponsiblePerson & CurrentName** that can locate a specific company or person 
are removed as well. Although **PostCode** can also indicate the address of that single company, it is kept at this stage 
and will be processed later as the project needs to analyze on regional patterns. 



