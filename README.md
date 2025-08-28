# Cars API

## Start Frontend App
- cd frontend/
- npm i
- npm run dev

## Start Backend
- cd backend/
- python -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- ./run_compose
- python manage.py runserver

  - View the url endpoints:
  - http://127.0.0.1:8000/api/ads/
  - http://127.0.0.1:8000/api/cars/
  - http://127.0.0.1:8000/api/models/
  - http://127.0.0.1:8000/api/users/
  - http://127.0.0.1:8000/api/profiles/
  
  - Run python manage.py createsuperuser to view as admin @ http://127.0.0.1:8000/admin/
  - Remember to just run, "deactivate" to stop the venv when you're done.
  
## 

Over the next three days your team will implement a DRF API for the [cars database](https://github.com/Golf-Evenings-and-Weekends/cars_database) schema.  Your goal should be to adhere to the specifications as closely as possible.  Your API should be able to perform the full range of CRUD operations.  It should be containerized.

Since you will have three days to work on this, it will be worth your while to do some team planning before you start writing code.  Here are some questions you might ask:
- How long will it likely take to complete this?
- What does "complete" look like?
- What are some difficulties/unknowns that might hinder our work?
- What material will the class cover in the coming days, and how can we use that to help us?
- How will we communicate, coordinate and divide up work?
- How do we distinguish between "core" features and "nice-to-have" features?

At the end of the third day, each group will present their solutions and answer any questions that arise.
