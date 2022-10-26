### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

1. JavaScript is a scripting language that helps you create interactive web pages, while Python is a high-level object-oriented programming language that has built-in data structures, combined with dynamic binding and typing, which makes it an ideal choice for rapid application development.
2. JavaScript has no concept of mutable and immutable but Python has mutable and immutable data types.
3. JavaScript should be encoded as UTF-16 as it does not offer any built-in support for manipulating raw bytes, whereas Python source code is ASCII by default unless you are specifying any encoding format.
4. JavaScript uses curly brackets whereas Python language uses indentation.
5. JavaScript objects have properties that can be composed of underlying attributes which let you define a property, and in Python programming language, getter and setter functions are used to defining an attribute.
6. JavaScript helps you to build a website or native application whereas Python is for tasks related to data analytics, machine learning, and math-intensive operations.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  1. Using get()
      If the key is present, the value associated with the key is printed, else the def_value passed in arguments is returned.
      Ex. ``print(dict.get('c', 'Not Found'))``

  2. Using setdefault()  
      Works in a similar way as to get(), but the difference is that each time a key is absent, a new key is created with the def_value associated with the key passed in arguments.
      Ex. ``dict.setdefault('c', 'Not Present')``
          ``print(dict['c'])``

- What is a unit test?

A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system (such as a method or function). 

- What is an integration test?

Integration Testing is a type of testing where software modules are integrated logically and tested as a group. The purpose of this level of testing is to expose defects in the interaction between these software modules when they are integrated.

- What is the role of web application framework, like Flask?

Web frameworks are a piece of software that offers a way to create and run web applications. They make it easy to route URLs to appropriate handlers, make the application front end interact with the backend databases, support sessions and user authentication, format output (e.g. HTML, XML, JSON) and improve application security against web attacks.

Flask, for example, can create serious websites out of the box. It contains a development server and debugger, and includes support for Jinja2 templating, secure cookies, unit testing, and RESTful request dispatching.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  There isn't an exact better way to do this but it depends on the situation. You can generally use query string parameters if you are describing the object you are on vs using the route for the object itself. For example, in the above case I would use /foods/pretzel and then use a query string parameter if I am decribing the pretzel such as /foods/pretzel?type=salty or /foods/pretzel?type=sugar.

- How do you collect data from a URL placeholder parameter using Flask?

You can specify the variable in the app.route and then use that variable as a paramater in the routing function. Here is an example of the pretzel:

```py
@app.route('/foods/<food>')
def grocery(food):
x = food
```

- How do you collect data from the query string using Flask?

With a query string the data can be found in the request.args dictionary:

```py
@app.route('/foods')
def grocery():
x = request.args.get('type')
```

- How do you collect data from the body of the request using Flask?

You can get the data from a post request in the body using the request.form dictionary

```py
@app.route('/foods')
def grocery():
x = request.form.get('type')
```

- What is a cookie and what kinds of things are they commonly used for?

Cookies are text files with small pieces of data — like a username and password — that are used to identify your computer.

- What is the session object in Flask?

The session object is built off of using cookies. It allows the server to set many different things in the session for the client to remember wihout having to create many different cookies and just have one session. It is also encoded so that someone can't change session data on the client before sending it to the server.

- What does Flask's `jsonify()` do?

jsonify will take JSON serializeable data in python and convert it to a JSON string.
