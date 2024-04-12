run-ai :
	docker-compose up 

install-llama2:
	docker exec -it ollama ollama run llama2 