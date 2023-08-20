import json

# Import companies.json, save as companies
with open("companies.json", "r") as company_data:
    companies = json.load(company_data)


def show_locations():
    for company in companies:
        id = company['id']
        company_name = company['company']
        city = company['city']
        zone = company['timezone']
        print(f"{id}: {company_name}, located in {city}, {zone} time.")


def validate_company():
    selected_company = int(input())
    for company in companies:
        company_id = company['id']
        if selected_company == company_id:
            company_info = {
                "id": company['id'],
                "company": company['company'],
                "city": company['city'],
                "timezone": company['timezone']
            }
            return company_info
