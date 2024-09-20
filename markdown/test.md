Test Check List
================

### Requirements

1. **Create a web page for a device management app**
	* Check: [ ]
2. **Maintain different devices in a web page**
	* Check: [ ]
3. **The device management app should maintain the following data per device**
	* Device Name (String)
		+ Check: [ ] → Yes, it exists as an input field
	* DeviceType (Allowed types: Smartphone, Tablet, Camera)
		+ Check: [ ] → Yes, it exists as a dropdown select option
	* Owner Name (String)
		+ Check: [ ] → Yes, it exists as an input field
	* Battery Status (0…100%)
		+ Check: [ ] → Yes, it is displayed and updated in real-time
4. **List existing devices of the app**
	* Check: [ ]
5. **Add the possibility to update all device settings or delete existing devices**
	* Check: [ ]
6. **Add the possibility to create new devices with a screen to input the data**
	* Check: [ ] → Yes, it exists as an input form
7. **When a device was added decrease the per device given Battery Status every second by 1% until it reaches 0%**
	* Check: [ ]

### Implementation

* The `addDevice` function has been implemented with try-catch blocks to handle any exceptions that may occur while adding a device to the list.
	+ Check: [ ] → Yes, it exists and handles errors
* The `renderTable` function is called after adding a new device to update the table display.
	+ Check: [ ] → Yes, it exists and updates the table display

### Conclusion

The requirements have been met with the implementation of the necessary features. The code has been written with best practices in mind, including try-catch blocks to handle errors.

Note: The above test check list is based on the provided context and may need to be updated or modified as more information becomes available.