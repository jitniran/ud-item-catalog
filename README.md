# Udacity ND Item Catalog project

    A Web app built using flask with to showcase how to build CRUD functions,API's and OAuth authentication. You can add a sport as category and add sport items of that particular sport

## Running the application

    1. Other than flask you need install OAuthClient
        'pip3 install oauthclient'
    2. run 'python3 app.py'

### HTML endpoints

#### Sport

    1.'/catalog' : shows latest added items with categories
    2.'catalog/<sport>/new' : add new sport (protected)
    3.'catalog/<sport>/edit' : edits sport (protected)
    4.'catalog/<sport>/delete' : deletes sport (protected)

#### SportItems

    1.'/catalog/<sport>/item/show' : shows sports items of that sport
    2.'/catalog/item/<sportitem>/view' : shows a sport item (protected)
    3.'/catalog/item/<sportitem>/edit' : edit a sport item (protected)
    4.'/catalog/item/<sportitem>/delete' : delete a sport item (protected)
    5.'/catalog/item/<sportitem>/new' : add a new sport item (protected)

(protected) means you need to login to view, access the page will redirect to Login 

### JSON endpoints

    1.'/catalog/JSON' : returns the present list of sports categories and items
    2.'/catalog/item/<item>/JSON' : returns a Sport item