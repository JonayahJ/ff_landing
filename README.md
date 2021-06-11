# FourFront Prelaunch Landing Page
This is the documentation for the FourFront Prelaunch Website backend.

## What to Know About the Postgresql 13 Database Tables
### Contacts App
* **tech_exp** asks whether or not the contact has technical experience (options: yes, no, other) 
* **tech_exp_text** is the input field for if the contact responded *other*
* **tech_founder** asks if the contact is a technical founder (options: yes, no, other) 
* **tech_founder_text** is the input field for if the contact responded *other*
* **startup_stage** asks which startup stage the contact is in (options: have an idea, no proof of concept (no-proof); done proof of concept, not validated (proof); pre-revenue (pre-rev); revenue (rev); validated and committed (val-comm); other (other))
* **startup_stage_text** is the input field for if the contact responded *other*
* **startup_description** asks the contact to give more details about their startup
* **access_freq** asks the contact to select at which frequency they would like to have access to a tech expert (options: always, often, occassionally, rarely, never, other)
* **access_freq_text** is the input field for if the contact responded *other*
* **tech_challenge** asks the contact to rate the importance of their technical needs from 1-7. 1 being the least important and 7 being the most important.
* **tech_challenge_description** asks the contact to describe their most immediate tech challenge
* **roadblocks** asks the contact to select all roadblocks that they have in the way of achieving their goals (options: articulating your technology needs (tech-need); having a single person of contact to give quality advice (advice)), lack of resources/money (lack));
meeting deadlines (deadlines); working with a dev agency (dev-agency); other (other))
* **roadblocks_text** is the input field for if the contact responded *other*
* **timeline** asks the contact to identify what the timeline to solve their immediate technical challenge is (options: within 4 weeks (within-4w); within 1 month (within-1m); within 3 months (within-3m); within 6 months (within-6m); Within 1 year (within-1y); other (other))
* **timeline_text** is the input field for if the contact responded *other*
* **subscriber_first_name** is the contact's first name
* **subscriber_last_name** is the contact's last name
* **subscriber_email** is the contact's email address
* **created_at** is when the contact submitted the form

### Subscriber App