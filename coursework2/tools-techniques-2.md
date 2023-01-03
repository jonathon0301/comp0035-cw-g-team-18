# Use of software engineering tools and techniques (coursework 2)

Team 18 Group Repository: <https://github.com/ucl-comp0035/comp0035-cw-g-team-18.git>

## ***Very Important Message to Reader/Marker: Statement of Mixing GitHub Account***

A member in the team had used his another GitHub account on his IDE. :cry: 
This ultimately led to some of the changes were committed with that account name. The GitHub account that he registered with the 
module leader on Moodle was jonathon0301, which is in the team and organization. The account that he logged on his IDE was 
JonathonShi. It can be inferred that these two accounts are the same person from username. This statement is used to waive any 
suspicions on academic misconduct. :pray: Thank you!

## **CI Workflow Shows Fail**

This is due to the code to be tested contains bugs which did not return what it expects to do. Since we have tested all 
methods in the shopping_basket.py file, the two string representation methods have errors found after running pytest. The 
CI workflow will show fail if keeping tests for those two methods but will work as successful if remove tests for those. 
Details are explained in [testing.md](testing.md). The yml file can be found by clicking [Python application workflow](https://github.com/ucl-comp0035/comp0035-cw-g-team-18/blob/e1f1654776d4a817ac0612edea547fc7a819d153/.github/workflows/python-app.yml) 

## **GitHUb Source Code Control**

Like in the coursework 1, team members are allowed to access the group repository and coursework files using their 
own GitHub account. Later, team members work in parallel on their own machines with their selected 
IDE (VScode or PyCharm). Pull and Push requests were then used if a members wants to synchronize work from the repository 
and personal machine.

## **Python Coding Environment**

Like coursework 1, the coding part (test) of this coursework in done by Python. Since we have already set up git and virtual 
environment in the previous coursework, we will not explain in so much detail in this file.

## **Markdown for text**

Markdown is a commonly used format of documentation in software development. Similar to what we did in coursework 1, we 
have adopted a range of use in Markdown files including adding headings, styling, quoting codes, adding links, adding images, 
creating lists, creating tables, using emojis, and adding collapsed sections. 
***The evidence for utilization can be proven from this and testing.md file.***

## **Scrum**

As planned in coursework 1, we have adopted Scrum method in this stage of the project. This includes weekly (seen as a Sprint) 
update on Moodle and within group meetings from every team member. Meanwhile, user stories are used as a technique to specify 
requirements, where user story is a strong technique in Agile development process.

## **BABOK**

Some of the 9 elicitation techniques identified by BABOK were used when eliciting requirements, further details can be 
found in [requirements.pdf](requirements.pdf)

## **MoSCoW**

The technique was used in prioritizing requirements, further details can be found in [requirements.pdf](requirements.pdf)

## **Unified Modeling Language (UML) Diagram**
Both structure and behaviour diagrams were used in this coursework. For details, refer to Use Case Diagram in 
[requirements.pdf](requirements.pdf) & Class Diagram in [design.pdf](design.pdf).

## **Other tools used in design**

This includes flowchart, wireframes, MVC design pattern, HTTP Methods and ERD diagram. Please refer to [design.pdf](design.pdf)

## **Tools & Techniques Used in Unit Testing**

This includes use of pytest, fixtures, Continuous Integration, and coverage. Please see details in [testing.md](testing.md)





