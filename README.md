# Hackathon-COVID-Webapp-Data-Processing

Our project is designed for the scenario in which we return to campus but must maintain proper COVID protocol. We focused on two main hurdles of an on-campus experience: the avoidance of high traffic areas and  contact-tracing. Both are crucial to managing a safe and plausible on-campus experience, but can infringe on personal data security in the sense of locations services. Therefore, we opted for a required self-logging system of entrance and exit patterns of individuals through buildings around campus. 

For high traffic areas, we aimed to help students find public spaces with lower foot traffic in order to lower their risk of exposure to COVID. If student A is looking for a study space, they might seek an area that is the least crowded and thus safer. Student A looks at our app and finds the lowest traffic areas for the hour, based on the previous hour’s data. When Student A gets there, since they use the same web app to log their entry of the public space, they will be providing data for the next day’s and hour’s prediction.

Using this same data, we can combine it with a list of students known to have tested positive for COVID to create a system of reliable contact tracing by comparing the entrance and exit times of COVID-positive students with other students to know if they spent time in the same room together.

Given the Hackathon’s time constraint, and the reality that our team is composed of first time Hackathoners, we took a MVP (minimum viable product) approach. The backend proof of concept, a group of data processing functions, uses Python to demonstrate how we would use the simple set of data collected by the web app to generate traffic comparison data, contract tracing insights, etc. Separately, the front end proof of concept, a deployed multi page web-app, shows how the user experience might look like. We used vanilla JS, html, css (with minimum use of bootstrap) as well as Mapbox.js to create the site. Though it is not a fully functional product (backend and frontend has yet been connected), we are confident in it as a proof of concept. 


DATA FILES: 
- Capacity_data.csv:Used in max_capacity.csv. Building name, furniture space percentage, total sq ft 
- Movement_data.csv: Used in High_traffic_spaces_daily.py, High_traffic_spaces_hourly.py. Student ID, Building, Entrance Time, Exit Time 
- Positive_data.csv: Used in Contact_tracing.py 
- Positive_times.csv: Used in Contact_tracing.py. Created by running def positive_times in Contact_tracing.py
- Thedata.csv: Used in max_capacity.py. Student ID, Building, Entrance Time, Exit Time 

CODE: 
- Contact_tracing.py: Using student movement data and COVID-testing data, this code returns a list of student  IDs who have come in contact with one or more COVID-positive students on a specific  day, warranting immediate testing, quarantine, and safety measures on their behalf.
- High_traffic_spaces_daily.py: Using student movement data, this code returns a list of the buildings on campus and  their visits per day, presented in descending order. With this information, students can  choose safer areas to travel to or through, maximizing individual and group safety.
- High_traffic_spaces_hourly.py: Using student movement data, this code returns a list of the buildings on campus and  their visits each hour. With this information, students can choose safer areas to travel to  or through, maximizing individual and group safety. 
- Max_capacity.py: Returns a T or F value for a certain building, T = capacity has been reached or passed,  F = capacity has not been reached. Capacity is calculated by the formula, (1 -  furn_space/100) * total_space/36. Formula was found from this site. 
- Plot_hourly_data.py: Plots hourly data created by the High_traffic_spaces_hourly.py. Will require some  rearrangement of High_traffic_spaces_hourly.py’s data before input. 

