import requests
import pandas as pd
import time

# API URLs
search_api_url = "https://digitalapi.bluecrossma.com/digital/find-a-doctor/v2/providers"
profile_api_url = "https://digitalapi.bluecrossma.com/digital/find-a-doctor/v1/providers/profile"

# Headers (Ensure fresh Authorization Token)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Authorization": "Bearer V0u9GgZkTqAocgqoSjEFAjI8dv7u",  # Update token here
    "X-ClientName": "MyBlueWeb",
    "X-ClientVersion": "25.2.3.5",
    "X-ClientSessionId": "fc0066e1-d8b2-43fb-90b3-4264ff8860df",
    "X-ClientLocale": "EN",
    "Referer": "https://member.bluecrossma.com/",
    "Origin": "https://member.bluecrossma.com"
}

# Store provider details
all_providers = []

# Set the page number (change manually for each run)
page = 1

# Search API Parameters
search_params = {
    "geoLocation": "42.32439478409065,-71.08756313798686",
    "limit": 20,  # Only one page at a time
    "page": page,
    "radius": 25,
    "networkId": "311005002",
    "searchType": "specialty",
    "teleHealthIncluded": "true",
    "searchForTH": "true",
    "specialtyId": "311000088"
}

# Fetch providers from search API
search_response = requests.get(search_api_url, headers=headers, params=search_params)

if search_response.status_code == 200:
    search_data = search_response.json()
    providers = search_data.get("providers", [])

    for provider in providers:
        provider_id = provider.get("id", "N/A")
        full_provider_id = f"p{provider_id}"  # Ensure 'p' prefix

        name = provider.get("name", "N/A")
        specialty = provider.get("specialty", "N/A")
        gender = provider.get("gender", "N/A")
        languages = provider.get("languages", "N/A")
        distance = provider.get("distance", "N/A")

        # Extract Primary Location
        locations = provider.get("locations", [])
        primary_location = locations[0] if locations else {}

        primary_location_name = primary_location.get("name", "N/A")
        primary_address = primary_location.get("address", "N/A")
        primary_phone = primary_location.get("phone", "N/A")
        primary_accepting_patients = primary_location.get("acceptingNewPatients", "N/A")

        # Extract Location ID for Profile API
        location_id = primary_location.get("id", "N/A")

        # Profile API Parameters
        profile_params = {
            "networkId": "311005002",
            "geoLocation": "42.32439478409065,-71.08756313798686",
            "providerId": full_provider_id,
            "locationId": location_id,
            "searchForTH": "true",
            "out_of_network": "false"
        }

        # Fetch Provider Profile
        profile_response = requests.get(profile_api_url, headers=headers, params=profile_params)

        if profile_response.status_code == 200:
            profile_data = profile_response.json()

            # Extract Education
            education_data = profile_data.get("education", [])
            education_details = [edu.get("name", "N/A") for edu in education_data]
            education_str = "\n".join(education_details) if education_details else "N/A"

            # Extract Hospital Affiliations
            hospital_affiliations = profile_data.get("locations", [])[0].get("hospitalAffiliations", [])
            hospital_details = [hosp.get("name", "N/A") for hosp in hospital_affiliations]
            hospital_str = ", ".join(hospital_details) if hospital_details else "N/A"

            # Extract Group Affiliations
            group_affiliations = profile_data.get("locations", [])[0].get("groupAffiliations", [])
            group_details = [group.get("name", "N/A") for group in group_affiliations]
            group_str = ", ".join(group_details) if group_details else "N/A"

            # Extract Other Locations
            other_locations = profile_data.get("locations", [])[1:] if len(profile_data.get("locations", [])) > 1 else []
            other_location_details = [
                f"{loc.get('name', 'N/A')} | {loc.get('address', 'N/A')} | {loc.get('phone', 'N/A')}"
                for loc in other_locations
            ]
            other_locations_str = "\n".join(other_location_details) if other_location_details else "No Additional Locations"

        else:
            education_str = "N/A"
            hospital_str = "N/A"
            group_str = "N/A"
            other_locations_str = "N/A"

        # Append Data
        all_providers.append({
            "Name": name,
            "Specialty": specialty,
            "Gender": gender,
            "Languages": languages,
            "Primary Location Name": primary_location_name,
            "Primary Address": primary_address,
            "Primary Phone": primary_phone,
            "Primary Accepting New Patients": primary_accepting_patients,
            "Other Locations": other_locations_str,
            "Affiliated Hospitals": hospital_str,
            "Group Affiliations": group_str,
            "Education": education_str,
            "Distance (miles)": distance,
        })

        print(f"✅ Processed: {name}")

        # Delay to avoid rate limits
        time.sleep(1)

else:
    print(f"❌ Error: {search_response.status_code}, Response: {search_response.text}")

# Save to CSV
df = pd.DataFrame(all_providers)
filename = f"endocrinologists_page_{page}.csv"
df.to_csv(filename, index=False)
print(f"✅ Data saved: {filename}")
