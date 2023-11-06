# Flask Routing and Views Lab

## Learning Goals

- Build and run a Flask application on your computer.
- Manipulate and test the structure of a request object.

---

## Key Vocab

- **Web Framework**: software that is designed to support the development of web
  applications. Web frameworks provide built-in tools for generating web
  servers, turning Python objects into HTML, and more.
- **Extension**: a package or module that adds functionality to a Flask
  application that it does not have by default.
- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided by
  a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made over
  the internet.
- **Web Server Gateway Interface (WSGI)**: an interface between web servers and
  applications.
- **Template Engine**: software that takes in strings with tokenized values,
  replacing the tokens with their values as output in a web browser.

---

## Instructions

> This is a **test-driven lab**, so please fork and clone the repo.

Run `pipenv install && pipenv shell` to generate and enter your virtual
environment.

```console
$ pipenv install && pipenv shell
```

Change into the `server` directory, where you will run the application and
tests:

```console
$ cd server
```

You can run the application as a script within the `server/` directory:

```console
$ python app.py
```

If you prefer working in a Flask environment, remember to configure it with the
following commands within the `server/` directory:

```console
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
$ flask run
```

Run `pytest -x` to run your tests:

```console
$ pytest -x
```

Use these instructions and `pytest`'s error messages to complete your work.

Lab Requirements:

- Implement a Flask application with the following views.
- An `index()` view routed using a base URL of `/`. The response should contain
  an `h1` element with the text "Python Operations with Flask Routing and
  Views".
- A `greet()` view that takes one parameter, a string containing a first name.
  Its route should be of the format `/greet/<string:name>`. The view should
  return a paragraph element that welcomes the person by name, for example
  "Welcome Amir!".
- A `count()` view that takes one parameter, an integer. Its route should be of
  the format `/count/<int:num>`. The view should display all numbers in the
  `range` of that parameter in an unordered list, with each number as a separate
  list item.
- A `math()` view that takes three parameters: `num1`, `operation`, and `num2`.
  Its route should be of the format
  `/math/<int:num1>/<string:operation>/<int:num2>`. It must perform the
  appropriate operation on the two numbers in the order that they are presented.
  The included operations should be: `+`, `-`, `*`, `div` (`/` would change the
  URL path), and `%`. The view should return an h2 element containing a math
  equation including the result of applying the operation to the numbers, for
  example "6+3=9". If the operation is not valid, return a paragraph element
  with the error message "Operation not recognized."

Once all of your tests are passing, commit and push your work using `git` to
submit.

---

## Resources

- [A Minimal Application - Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/#a-minimal-application)
- [Routing - Flask](https://flask.palletsprojects.com/en/2.3.x/quickstart/#routing)
- [Chapter 2. Basic Application Structure - Flask Web Development, 2nd Edition](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html#idm140583868985008)
