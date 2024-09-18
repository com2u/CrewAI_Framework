```markdown
# Device Manager

## Overview
The Device Manager is a simple web application for tracking various devices, their types, owners, and battery status. Users can add devices through a form, and the added devices will be listed on the same page.

## Features
- Add a device with details such as device name, type, owner name, and battery status.
- Validate the form fields to ensure correct input.
- Display added devices in a list.

## Table of Contents
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Form Validation](#form-validation)
- [Clearing Errors](#clearing-errors)
- [Resetting the Form](#resetting-the-form)

## Getting Started
To start using the Device Manager, simply open the provided `index.html` file in a web browser. Ensure that JavaScript is enabled in the browser settings for the application to function properly.

## Usage
1. Open the `index.html` file in any web browser.
2. Fill out the form with the following fields:
   - **Device Name:** A text field to enter the name of the device.
   - **Device Type:** A dropdown menu to select the type of device (Mobile, Tablet, Laptop, Desktop).
   - **Owner Name:** A text field to enter the name of the device owner.
   - **Battery Status (%):** A number field to enter the battery percentage, which must be between 1 and 100.

3. Click on the `Add Device` button to submit the form.
4. If all fields are correctly filled out, the new device will be added to the list displayed below the form.

## Form Validation
The application performs various validation checks to ensure the input data is correct:
- Device Name is required.
- Device Type is required.
- Owner Name is required.
- Battery Status must be a number between 1 and 100.

If any of these validations fail, an error message will be shown, and the corresponding fields will be highlighted in red.

## Clearing Errors
Before performing any new validation, the application clears all previous error styles by removing the `error` class from all input and select elements:
```javascript
// Clear previous error styles
document.querySelectorAll('input, select').forEach(element => {
    element.classList.remove('error');
});
```

## Resetting the Form
After successfully adding a device to the list, the form fields will be cleared using the `reset()` method:
```javascript
// Clear the form fields
form.reset();
```

## Example
Here's what a correctly filled out form might look like:
- **Device Name:** MyPhone
- **Device Type:** Mobile
- **Owner Name:** John Doe
- **Battery Status:** 80%

Once you click `Add Device`, the list will show:
```
Name: MyPhone, Type: Mobile, Owner: John Doe, Battery: 80%
```

## Conclusion
The Device Manager is a straightforward application designed to help manage a list of devices and their related information. By ensuring proper validation and user-friendly features, it simplifies the process of tracking device details.
```