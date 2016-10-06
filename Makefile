start:
	docker build -t wscmp .
	docker run -p 80:80 wscmp