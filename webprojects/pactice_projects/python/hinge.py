import requests
import sys

# Define a function to check registration status on Hinge
def check_hinge_registration(api_key, phone_or_email):
    try:
        # Set up the API endpoint
        hinge_url = "https://api.hinge.com/v1/check_registration"

        # Prepare the request payload
        payload = {
            "identifier": phone_or_email  # Either phone number or email address
        }

        # Prepare headers with the provided API key
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        # Send a POST request to the Hinge API
        response = requests.post(hinge_url, json=payload, headers=headers)

        # Check if the response indicates success
        if response.status_code == 200:
            data = response.json()
            return data.get("is_registered", False)
        else:
            print(f"Error from Hinge API: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Exception during Hinge API call: {e}")
        return None


# Define a function to check registration status on Tinder
def check_tinder_registration(api_key, phone_or_email):
    try:
        # Set up the API endpoint
        tinder_url = "https://api.gotinder.com/v2/auth/check_registration"

        # Prepare the request payload
        payload = {
            "identifier": phone_or_email  # Either phone number or email address
        }

        # Prepare headers with the provided API key
        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        # Send a POST request to the Tinder API
        response = requests.post(tinder_url, json=payload, headers=headers)

        # Check if the response indicates success
        if response.status_code == 200:
            data = response.json()
            return data.get("is_registered", False)
        else:
            print(f"Error from Tinder API: {response.status_code}, {response.text}")
            return None
    except Exception as e:
        print(f"Exception during Tinder API call: {e}")
        return None


# Main function to orchestrate the registration check
def main():
    try:
        # Retrieve API keys and input
        hinge_api_key = input("Enter Hinge API key: ")
        tinder_api_key = input("Enter Tinder API key: ")
        phone_or_email = input("Enter phone number or email address to check: ")

        # Check registration status on both platforms
        hinge_result = check_hinge_registration(hinge_api_key, phone_or_email)
        tinder_result = check_tinder_registration(tinder_api_key, phone_or_email)

        # Print the results
        print("\nRegistration Status:")
        print(f"Hinge: {'Registered' if hinge_result else 'Not Registered'}")
        print(f"Tinder: {'Registered' if tinder_result else 'Not Registered'}")

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Run the main function
if __name__ == "__main__":
    main()
