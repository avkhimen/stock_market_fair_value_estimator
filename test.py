import requests
import json
from pprint import pprint

# def get_eps(symbol):
# 	r = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/' + symbol + '?period=quarter')
# 	eps = []
# 	for item in json.loads(r.text)['financials']:
# 		eps.append(float(item['EPS']))
	
# 	return eps

# def get_average_eps(num_eps_for_finance, eps_list):
# 		"""Returns the average eps from the quantity of num_eps_for_finance"""
# 		avg_eps = 0
# 		for i in range(1, num_eps_for_finance):
# 			avg_eps = (avg_eps + float(eps_list[i])) / i

# 		return avg_eps

f = open("guru99.txt", "a+")
for i in range(5, 10):
     f.write("This is line {}\r".format(i+1))
f.close()

class CompanyRecord:
	def __init__(self, company_symbol, current_value, fair_value, document_name):
		self.company_symbol = company_symbol
		self.current_value = current_value
		self.fair_value = fair_value
		self.document_name = document_name

	def create_record(self):
		"""Opens the document and werites info"""
		f = open(self.document_name, "a+")
		f.write("{}, current value:, {}, fair value:, {}\r".format(self.company_symbol, self.current_value, self.fair_value))
		f.close()