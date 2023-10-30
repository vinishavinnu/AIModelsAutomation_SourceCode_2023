import requests

# Define the API endpoint for image upload validation
api_url = "https://agi.nslhub.com/fs/DetectViolation/eating"

# Define test scenarios with image filenames and expected responses
test_scenarios = [
    {"image_file": "EatingValid1.jpg", "expected_response": "Valid"},
    {"image_file": "EatingInvalid.jpg", "expected_response": "Invalid"},
    {"image_file": "EatingValid2.jpg", "expected_response": "Invalid"},
    {"image_file": "EatingValid3.jpg", "expected_response": "Valid"},
    # Add more test scenarios as neededrr5rff
]

# Loop through each test scenario
for scenario in test_scenarios:
    image_file = scenario["image_file"]
    expected_response = scenario["expected_response"]

    # Create a dictionary to hold the form data
    payload = {"file": (image_file, open(image_file, "rb"))}

    # Send a POST request to the API with the image file as form data
    response = requests.post(api_url, files=payload)
    # APIResponse=response.text
    # print(APIResponse)
    GREEN = "\033[92m"
    RESET = "\033[0m"
    RED = "\033[91m"
    RESET = "\033[0m"

    # Check if the response matches the expected outcome
    if response.status_code == 200:
        api_response = response.json()
        if api_response["message"] == expected_response:
            
            print(f"{GREEN}Test PASSED{RESET}: {image_file} is {expected_response}")
        else:
            print(f"{RED}Test FAILED{RESET}: {image_file} is not {expected_response}")
    else:
        print(f"Test FAILED: Error uploading {image_file}")

    # Optionally, you can add assertions to handle the test result based on your testing framework.
