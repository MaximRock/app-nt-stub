post_script()
{
	web_set_sockets_option("SSL_VERSION", "2&3");
	
	web_rest("POST: http://127.0.0.1:5000/music",
			"URL=http://127.0.0.1:5000/music",
			"Method=POST",
			"EncType=raw",
			"Body={\r\n"
			"\"musical_style\": \"{musical_style}\",\r\n"
			"\"group_name\": \"{group_name}\",\r\n"
			"\"album\": \"{album}\",\r\n"
			"\"release_year\": {release_year},\r\n"
			"\"carrier\": \"{carrier}\",\r\n"
			"\"description\": \"description\"\r\n"
			"}",
	HEADERS,
	"Name=Accept", "Value=application/json", ENDHEADER,
	"Name=Content-Type", "Value=application/json", ENDHEADER,
	LAST);
	
	return 0;
}
