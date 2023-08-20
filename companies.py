import json


# with open('companies.json', 'r') as json_file:
#     companies = json.load(json_file)


def get_companies():
    with open('companies.json', 'r') as json_file:
        companies = json.load(json_file)
    for company in companies:
        print(f"{company['id']}: {company['company']} in {company['city']}.")


class Companies:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_company_details(self):
        with open('companies.json', 'r') as json_file:
            companies = json.load(json_file)

        company_info_list = []

        for company in companies:
            company_id = company['id']
            company_name = company['company']
            company_city = company['city']
            city_timezone = company['timezone']

            if company_id is not None and company_name is not None and company_city is not None and city_timezone is not None:
                company_info = {
                    'company_id': company_id,
                    'company_name': company_name,
                    'company_city': company_city,
                    'city_timezone': city_timezone
                }
                company_info_list.append(company_info)

        return company_info_list

