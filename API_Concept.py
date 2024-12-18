import requests

"""
API stands for Application Programming Interface. It is a set of rules and tools that allows different 
software applications to communicate with each other. Think of it as a bridge that lets different 
software systems interact.
"""

"""
API Key Concepts:-

Endpoints:
An endpoint is a specific URL where an API can be accessed. It’s like a door through which you can 
enter and interact with a system. For example, https://api.example.com/users might be an endpoint to 
get user data.

Requests and Responses:
Request: When you want to retrieve or send data, you make a request to an API. The request includes the method (like GET, POST, PUT, DELETE) and sometimes additional information like headers or data payload.
Response: After the API processes the request, it sends back a response, which usually includes data or status information.

Methods:
GET: Retrieve data from the server.
POST: Send data to the server to create or update something.
PUT: Update existing data on the server.
DELETE: Remove data from the server.

Headers:
Headers are additional information sent with the request or response. They might include metadata like content type, authorization tokens, or caching instructions.
Headers are key-value pairs sent with an API request or response. They provide additional information about the request or response. Headers can be used to convey metadata, control the behavior of the request/response, and manage various aspects of the interaction between client and server.

Common Headers
Content-Type:
Indicates the type of data being sent in the request or response.
For example, Content-Type: application/json tells the server that the request body contains JSON data.
Authorization:
Used to send credentials (like API keys or tokens) to authenticate the request.
For example, Authorization: Bearer YOUR_API_KEY is used to send a token for authentication.
Accept:
Specifies the media types that the client is willing to receive from the server.
For example, Accept: application/json means the client expects JSON data in response.
User-Agent:
Provides information about the client software making the request.
For example, User-Agent: Mozilla/5.0 might identify the request as coming from a web browser.
Cache-Control:
Directs the caching mechanisms in both the client and server.
For example, Cache-Control: no-cache tells the server and client not to cache the response.

Payload:
The payload is the data sent with a request (especially with POST or PUT requests). It could be in 
formats like JSON or XML.

Payload refers to the data sent in the body of an API request, especially for POST and PUT requests 
where you need to send data to the server. The payload is often in JSON format but can also be in 
other formats like XML or form-data.

Payload Formats
JSON (JavaScript Object Notation):
A popular format for sending data because it's easy for both humans and machines to read and write.
Example: {"name": "John", "age": 30}

XML (eXtensible Markup Language):
Another format for data exchange, though less commonly used than JSON in modern APIs.
Example: <person><name>John</name><age>30</age></person>

Form-Data:
Used for sending data as if it were coming from a form submission.
Example: name=John&age=30

Status Codes:
Status codes are part of the HTTP response and indicate the result of the request. Common codes include:
200 OK: The request was successful.
201 Created: The request was successful and a resource was created.
400 Bad Request: There was an error with the request.
401 Unauthorized: Authentication failed.
404 Not Found: The requested resource could not be found.
500 Internal Server Error: There was an error on the server.
"""

BASE_URL = "https://jsonplaceholder.typicode.com/users"

# Here’s a simple example to fetch data from a public API
def get_users():
    """Fetches the list of users from the API."""
    try:
        response = requests.get(BASE_URL)
        # Print the status code and response text for debugging
        print(f"Status Code: {response.status_code}")
        print(f"Response Text: {response.text}")

        # Check if the status code indicates success
        if response.status_code == 200:
            # Try to parse JSON response
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                print("Error decoding JSON response")
                return {"error": "Response is not in JSON format"}
        else:
            return {"error": f"Failed to fetch users, status code: {response.status_code}"}
    except requests.RequestException as e:
        return {"error": str(e)}

def main():
    users = get_users()
    print("Current Users:", users)

if __name__ == "__main__":
    main()
