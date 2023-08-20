
import json


class Companies:
    def __init__(self, file_path):
        self.file_path = file_path


    def get_company_details(self):
        with open('companies.json', 'r') as json_file:
            companies = json.load(json_file)

        company_info_list = []

        for company in companies:
            company_id = company.get('company_id')
            company_name = company.get('company_name')
            company_city = company.get('company_location', {}).get('city')
            city_timezone = company.get('company_location', {}).get('timezone')

            if company_id is not None and company_name is not None and company_city is not None and city_timezone is not None:
                company_info = {
                    'company_id': company_id,
                    'company_name': company_name,
                    'company_city': company_city,
                    'city_timezone': city_timezone
                }
                company_info_list.append(company_info)

        return company_info_list

    def get_companies(self):
        company_info = self.get_company_details()
        for company in company_info:
            print("Company Name:", company['company_name'])
        print("-" * 20)




# def get_companies():
#     for company in companies:
#         company_id = company['id']
#         company_name = company['company']
#         city = company['city']
#         zone = company['timezone']
#         print(f"{company_id}: {company_name}, located in {city}, {zone} time.")
#
#
# def validate_company():
#     selected_company = int(input())
#     for company in companies:
#         company_id = company['id']
#         if selected_company == company_id:
#             company_info = {
#                 "id": company['id'],
#                 "company": company['company'],
#                 "city": company['city'],
#                 "timezone": company['timezone']
#             }
#             return company_info
def get_companies():
    return None
