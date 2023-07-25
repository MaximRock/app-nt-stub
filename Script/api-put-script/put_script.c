put_script()
{
	web_set_sockets_option("SSL_VERSION", "2&3");
	
	web_rest("PUT: http://127.0.0.1:5000/music/{id}",
			"URL=http://127.0.0.1:5000/music/{id}",
			"Method=PUT",
			"EncType=raw",
			"BodyFilePath=data.json",
			HEADERS,
			"Name=Accept", "Value=application/json", ENDHEADER,
			"Name=Content-Type", "Value=application/json", ENDHEADER,
			LAST);

	return 0;
}
