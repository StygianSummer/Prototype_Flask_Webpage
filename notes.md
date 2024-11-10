look at this link: https://www.geeksforgeeks.org/flask-creating-first-simple-application/
This part:
Flask – (Creating first simple application) – FAQs

# Some Code explanations
## add_url_rule(<url rule>, <endpoint>, <view function>) 
- <url rule>: This is the URL pattern or route (e.g., '/hello/<name>').
- <endpoint>: This is the internal name used to refer to the route (e.g., 'hello_name'). It’s often the same as the view function name but doesn’t have to be.
- <view function>: This is the function that handles the route (e.g., hello_name)

# HTTP(unencrypted) stuff:
- GET : Sends data in simple or unencrypted form to the server.
- HEAD : Sends data in simple or unencrypted form to the server without body. 
- PUT : A PUT request is used to modify the data on the server. It replaces the entire content at a 
  particular location with data that is passed in the body payload. 
  If there are no resources that match the request, it will generate one. 
- PATCH: PATCH is similar to a PUT request, but the only difference is, it modifies a part of the data. 
  It will only replace the content that you want to update.
- DELETE : Deletes target resource provided as URL.
- POST: to submit data to be processed to the server.

POST: data is sent in the request body, not in the URL (like with GET)
  - GET is for fetching data, appending parameters in the URL, ideal for searches. 
  - POST, used for updates, sends data securely in the request body, perfect for form

By default, the Flask route responds to the GET requests. However, this preference
can be altered by providing methods argument to route() decorator.

# Route conversions
- when you define a route with a variable (like <id>), Flask treats the variable as a string by default. 
- But what if you want the variable to be a specific data type, like an integer or a UUID? 
- That’s where converters come in!
- string (default): Accepts any text without slashes (/). 
  - Example: <string:name>
- int: Accepts positive integers only. 
  - Example: <int:id>
- float: Accepts positive floating-point numbers.
  - Example: <float:price>
- path: Accepts strings with slashes (/).
  - Example: <path:subpath>
- uuid: Accepts a UUID string (e.g., 123e4567-e89b-12d3-a456-426614174000).
  - Example: <uuid:identifier>

Why use them?
- Validation: ensures that variables are the type we want
  - The route /post/<int:id> expects the id to be an integer.
    - If you visit http://127.0.0.1:5000/post/123, it will display the page 
    - If you try to visit http://127.0.0.1:5000/post/abc, you’ll get a 404 error because abc is not an integer.
- Cleaner code
- Error Handling