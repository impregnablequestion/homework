## What is responsible for defining the routes of the games resource?

The express function in create_router.js is responsible for defining the routes for the get, post, delete and put HTTP requests.

## What do you notice about the folder structure? Whats the client responsible for? Whats the server responsible for?

The client is responsible for creating, editing, deleting and displaying the games, while the server is responsible for storing the information in the database and providing the correct information on request.

## What are the the responsibilities of server.js?

server.js is responsible for connecting to the mongodb collection, and using the router from create_router to provide the front end with the api links to use.

## What are the responsibilities of the gamesRouter?

The responsibilities of the gamesRouter are storing and retrieving the games in the games collection using the createRouter function defined in the create_router.js file.

## What process does the the client (front-end) use to communicate with the server?

The client uses fetch requests to the API that the server provides.

## What optional second argument does the fetch method take? And what is it used for in this application? Hint: See Using Fetch on the MDN docs

The fetch can take a second argument that defines the method, body, and headers of the request. For exampmle, you would use it to indicate that the request was a POST request rather than the default GET.

## Which of the games API routes does the front-end application consume (i.e. make requests to)?

"http://localhost:9000/api/games a

## What are we using the MongoDB Driver for?

To interact programmatically with the database