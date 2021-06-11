# FourFront Prelaunch Landing Page
This is the documentation for the FourFront Prelaunch Website backend.

## What to Know About the Postgresql 13 Database Tables
### Contacts App
In this app, responses from the questionnaire are saved in the database under the table *contacts_survey*.
* **tech_exp** asks whether or not the contact has technical experience (options: yes, no, other).
* **tech_exp_text** is the input field for if the contact responded *other*.
* **tech_founder** asks if the contact is a technical founder (options: yes, no, other).
* **tech_founder_text** is the input field for if the contact responded *other*.
* **startup_stage** asks which startup stage the contact is in (options: have an idea, no proof of concept (no-proof); done proof of concept, not validated (proof); pre-revenue (pre-rev); revenue (rev); validated and committed (val-comm); other (other)).
* **startup_stage_text** is the input field for if the contact responded *other*.
* **startup_description** asks the contact to give more details about their startup.
* **access_freq** asks the contact to select at which frequency they would like to have access to a tech expert (options: always, often, occassionally, rarely, never, other).
* **access_freq_text** is the input field for if the contact responded *other*.
* **tech_challenge** asks the contact to rate the importance of their technical needs from 1-7. 1 being the least important and 7 being the most important.
* **tech_challenge_description** asks the contact to describe their most immediate tech challenge.
* **roadblocks** asks the contact to select all roadblocks that they have in the way of achieving their goals (options: articulating your technology needs (tech-need); having a single person of contact to give quality advice (advice)), lack of resources/money (lack));
meeting deadlines (deadlines); working with a dev agency (dev-agency); other (other)).
* **roadblocks_text** is the input field for if the contact responded *other*.
* **timeline** asks the contact to identify what the timeline to solve their immediate technical challenge is (options: within 4 weeks (within-4w); within 1 month (within-1m); within 3 months (within-3m); within 6 months (within-6m); Within 1 year (within-1y); other (other)).
* **timeline_text** is the input field for if the contact responded *other*.
* **subscriber_first_name** is the contact's first name.
* **subscriber_last_name** is the contact's last name.
* **subscriber_email** is the contact's email address.
* **created_at** is when the contact submitted the form.

When a new form is submitted, an email is sent to all superusers from the **support@fourfront.io** email address.

### Pages App
In this app, new experts and advisors can be added and dynamically rendered onto the landing page via the **Django Admin Page** by a superuser.  Experts and Advisors are saved into the table *pages_expert*.
* **name** is the expert/advisor's *full* name.
* **linkedin** is the *link* to the expert/advisor's LinkedIn profile page.
* **headshot** is the expert/advisor's headshot.
* **company1** is the uploaded .png file of a recent company the expert/advisor worked at (can be blank when creating an expert/advisor, but is necessary for dynamically rendering a card in the Expert section on the landing page).
* **company2** is the uploaded .png file of a recent company the expert/advisor worked at (can be blank when creating an expert/advisor, but is necessary for dynamically rendering a card in the Expert section on the landing page).
* **created_at** is when the expert/advisor was added in Admin.
* **designation** is a *charfield* that differentiates between experts, advisors, CEOS, etc.


### Subscriber App
In this app, people interested in reaching out to FourFront can leave their email addresses for direct contact.  A list of all contacts are stored in the *subscriber_emails* table.
* **subscriber_email** is the contact's email address
* **created_at** is when the contact submitted the form

When a new form is submitted, an email is sent to all superusers from the **support@fourfront.io** email address.

## Django Admin
When on the Admin Page, a user can access the different tables in the database via the different apps.  The only app that will effect the website is the Pages App (adding new experts (catch-all term for experts, advisors, CEOs, etc) will add them to the website assuming all fields are filled out).  This app is also the only one with a filter on the entries via designation.  

All apps have a search feature that will let users search by name and designation where appropriate.

## Contact
If you have questions, please reach out to Jo at **jonayah@thinkhalcyon.com**.