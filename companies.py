import json


def get_companies():
    with open('companies.json', 'r') as json_file:
        companies = json.load(json_file)
    for company in companies:
        print(f"{company['id']}: {company['company']} in {company['city']}.")


def get_company_details(choice):
    with open('companies.json', 'r') as json_file:
        companies = json.load(json_file)

    for company in companies:
        if choice == company['id']:
            company_info = {
                'company_id': company['id'],
                'company_name': company['company'],
                'company_city': company['city'],
                'city_timezone': company['timezone']
            }

            return company_info
