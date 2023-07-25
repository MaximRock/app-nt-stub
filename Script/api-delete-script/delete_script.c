delete_script()
{
		web_rest("DELETE: http://127.0.0.1:5000/music/{id}",
		"URL=http://127.0.0.1:5000/music/{id}",
		"Method=DELETE",
		"EncType=raw",
		LAST);
	
	return 0;
}
