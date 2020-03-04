from utility_classes import Company, Symbols
from utility_classes import UndervaluedCompany, CompanyRecord
from support_functions import get_input_args
from pprint import pprint

def main():
	
	market = get_input_args().market
	
	symbols = Symbols(market).get_all_symbols()

	for item in symbols:
		try:
			print("Processing {}".format(item))
			company = Company(item)
			fair_value = company.get_company_fair_value()
			current_value = company.get_50_day_average_stock_price()
			num_of_eps_statements = company.get_eps_length()

			undervalued_company = UndervaluedCompany(fair_value, current_value, num_of_eps_statements)
			if undervalued_company.is_company_undervalued():
				CompanyRecord(item, fair_value, current_value, market).create_record()
		except Exception as e:
			print(e)

if __name__ == '__main__':
	main()