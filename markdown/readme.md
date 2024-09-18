# Error Handling System Documentation
=====================================

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Using the Error Handler](#using-the-error-handler)
3. [Adding Devices](#adding-devices)
4. [Error Handling](#error-handling)

## Introduction
---------------

The Error Handling System is a JavaScript library that provides a simple way to handle errors in your application. It allows you to log and display errors in a user-friendly manner.

### Features

*   Log errors with detailed information
*   Display error messages to the user
*   Support for catching and handling errors in try-catch blocks

## Using the Error Handler
---------------------------

To use the error handler, simply include the JavaScript file in your HTML document:

```html
<script src="https://cdn.jsdelivr.net/npm/error-handling-system@1.0.0/dist/error-handling-system.min.js"></script>
```

### Creating an Instance of the Error Handler

To create a new instance of the error handler, use the following code:

```javascript
const errorHandler = new ErrorHandlingSystem();
```

## Adding Devices
-----------------

To add devices to your database, you can use the `addDevice` function. This function takes three parameters: `id`, `name`, and `description`.

### Example Usage

```javascript
db.addDevice({
    id: 1,
    name: "Device 1",
    description: "This is device 1"
});
```

## Error Handling
-----------------

The error handler provides a simple way to catch and handle errors in your application. You can use the `try`-`catch` block to catch errors, and then log and display them using the error handler.

### Example Usage

```javascript
try {
    // Simulating a database operation
    db.addDevice({
        id: 1,
        name: "Device 1",
        description: "This is device 1"
    });
} catch (error) {
    // Use the error handler to log and display the error
    errorHandler.logError(error);
}
```

## Adding a Device Form
-------------------------

The following form can be used to add devices:

```html
<form>
    <label for="id">ID:</label>
    <input type="text" id="id" name="id"><br><br>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="description">Description:</label>
    <textarea id="description" name="description"></textarea><br><br>
    <button type="button" onclick="addDevice()">Add Device</button>
</form>
```

### Notes

*   The `addDevice` function should be called when the form is submitted.
*   The error handler can be used to log and display errors that occur during device addition.

This documentation provides a complete guide on how to use the Error Handling System, including creating an instance of the error handler, adding devices, and handling errors.