from locust import HttpUser, between, task
import logging

class APIUser(HttpUser):
    wait_time = between(1, 5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO
    
    @task
    def index(self):
        self.client.get("/")
        

    @task
    def predict_image(self):
        with open("stress_test/dog.jpeg", "rb") as f:
            files = {'file': f}
            self.client.post("/predict", files=files)
            # logging.info(f'response: {response.json()}')
    
    
    @task
    def feedback(self):
        data = {
            'filename': 'dinosaur.jpg', 
            'prediction': 'triceratops', 
            'score': 0.9931 
        }
        self.client.post("/feedback", data=data)