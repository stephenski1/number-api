# 📌 Number Classification API

## 📖 Overview
The **Number Classification API** is a simple web service that takes a number as input and returns interesting mathematical properties about it. This includes checking if the number is **prime**, **perfect**, **Armstrong**, **odd/even**, and also provides the **sum of its digits** along with a fun fact from the **Numbers API**.

The API is built using **Flask** and deployed on an **AWS EC2 instance** using **Gunicorn and Nginx**.

---

## 🚀 Features
✅ **Check if a number is prime**  
✅ **Determine if a number is a perfect number**  
✅ **Identify Armstrong numbers**  
✅ **Classify numbers as odd/even**  
✅ **Calculate the sum of digits**  
✅ **Fetch a fun fact using the Numbers API**  
✅ **Fast API response (<500ms)**  
✅ **CORS enabled for external access**  

---

## 🌐 API Endpoint
- **Base URL:** `http://13.53.205.219`  
- **Endpoint:** `/13.53.205.219/classify-number?number=<number>`

### **📥 Example Request**
```http
GET http://13.53.205.219/api/classify-number?number=371


Example Response

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}



🛠️ Installation & Setup


1- Clone the Repository

git clone https://github.com/stephenski1/number-api.git
cd number-api

2️⃣ Set Up a Virtual Environment

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Run the Flask App Locally

python app.py


🚀 Deployment (AWS EC2 + Gunicorn + Nginx)

1️⃣ Start Gunicorn

gunicorn --workers 3 --bind 0.0.0.0:8000 app:app

2️⃣ Set Up Nginx Reverse Proxy
Configure Nginx to forward requests from port 80 → Gunicorn (8000)

Restart Nginx:
sudo systemctl restart nginx





🔍 How It Works-

Mathematical Classifications;

- Prime Number: A number greater than 1 with no divisors other than 1 and itself.
- Perfect Number: A number where the sum of its proper divisors equals the number.
- Armstrong Number: A number that is equal to the sum of its own digits, each    raised to the power of the number of digits.

- Properties Field Logic

Condition                 	Properties Output
Armstrong + Odd            	["armstrong", "odd"]
Armstrong + Even	          ["armstrong", "even"]
Not Armstrong + Odd	        ["odd"]
Not Armstrong + Even	      ["even"]



✅ Example Numbers-

Number    	Prime?	    Perfect?	    Armstrong?	    Odd/Even	    Digit Sum
371        	❌ No	      ❌ No	        ✅ Yes	        🟢 Odd	        11
6	          ❌ No      ✅ Yes	      ❌ No          	🔵 Even       	6
7	          ✅ Yes	   ❌ No          ❌ No	        🟢 Odd	        7
153	        ❌ No	      ❌ No	        ✅ Yes	        🟢 Odd	        9



📡 Technologies Used-

- Programming Language: Python 🐍
- Framework: Flask 🌎
- Server: Gunicorn 🦄
- Reverse Proxy: Nginx 🌐
- Hosting: AWS EC2 ☁️
- External API: Numbers API 🔢


🔗 API Hosting & Documentation-

- Public API URL: [http://13.53.205.219/api/classify-number?number=371]
GitHub Repository: https://github.com/stephenski1/number-api/tree/main
