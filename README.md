
# Parking reservation application 
##  Feature: ## 
1. You can create/update/delete parking space using locality, lane, slot.
2. You can reservation/cancellation of parking slot. 
3. Application is developed using Django 1.11, database is SQLite,uses faker module to import dummy data, BootStrap4 for UI.
4. Deployment steps are done using django manage.py file.

## Steps: ## 
1. Load test data by running "python populate_parking_data.py
2. Do migrations
```
python manage.py makemigrations parking_reservation
python mange.py migrate
```

3. Run server
```
python manage.py runserver
```

##  @TODO:   
1. Advanced visualization. 
2. Advanced authentication and authorization.

