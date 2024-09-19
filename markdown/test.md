# Test Checklist for Device Management App
=============================================

## Requirements

* Create a web page for a device management app
* Maintain different devices in a web page
* Display device data: Device Name, Device Type, Owner Name, Battery Status (0…100%)
* List existing devices of the app
* Add possibility to update all device settings or delete existing devices
* Add possibility to create new devices with a screen to input data
* Decrease per-device given Battery Status every second by 1% until it reaches 0%
* Store device data persistently

## Code Implementation

```html
<!-- HTML code for the web page -->
```

## Test Results
---------------

### Device Name (String)
:cross: Not implemented in the provided code snippet.

### Device Type (Allowed types: Smartphone, Tablet, Camera)
:cross: Not implemented in the provided code snippet.

### Owner Name (String)
:questionmark Not sure if it's implemented correctly.

### Battery Status (0…100%)
:x: Implemented incorrectly. The battery status is decreased every second by 1%, but there's no mechanism to display the current value.

### List existing devices of the app
:check: Implemented correctly. The `updateDeviceTable()` function retrieves data from the SQLite database and populates the device table with it.

### Add possibility to update all device settings or delete existing devices
:questionmark Not sure if it's implemented correctly.

### Add possibility to create new devices with a screen to input data
:x: Not implemented at all.

### Decrease per-device given Battery Status every second by 1% until it reaches 0%
:cross: Implemented incorrectly. The battery status is decreased every second, but there's no mechanism to stop the decrease once it reaches 0%.

### Store device data persistently
:check: Implemented correctly using SQLite database.

## Summary

The code implementation partially meets the requirements. However, some features are not implemented or implemented incorrectly. The battery status and creation of new devices with input fields are missing entirely. Additionally, the update and deletion of existing devices might need further investigation to ensure correct functionality.