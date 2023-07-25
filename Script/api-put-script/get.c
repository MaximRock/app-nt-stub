get()
{	
	web_set_sockets_option("SSL_VERSION", "2&3");
	
	web_rest("GET: http://127.0.0.1:5000/music/{id}",
	"URL=http://127.0.0.1:5000/music/{id}",
	"Method=GET",
	LAST);
	
	return 0;
}
