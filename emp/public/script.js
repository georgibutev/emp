function clearTextField(element) {
	// Get reference to a text field
	field = document.getElementById(element);
	// Clear the preset value
	field.setAttribute("value", "");
}