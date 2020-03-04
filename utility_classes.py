import requests
import json
from pprint import pprint

class Company():
	def __init__(self, symbol, num_eps_for_adj = 10, num_for_avg_eps = 5, Y = 1.8, no_growth_eps = 7, growth_factor = 1):
		self.symbol = symbol
		self.num_eps_for_adj = num_eps_for_adj
		self.num_for_avg_eps = num_for_avg_eps
		self.Y = Y
		self.no_growth_eps = no_growth_eps
		self.growth_factor = growth_factor

	def get_realtime_stock_price(self):
		"""Returns real time stock price"""
		try:
			r = requests.get('https://financialmodelingprep.com/api/v3/quote/' + self.symbol)
		except Exception as e:
			print(e)
		else:
			real_time_stock_price = float(json.loads(r.text)[0]['price'])
			return real_time_stock_price

	def get_50_day_average_stock_price(self):
		"""Returns 50-day average stock price"""
		try:
			r = requests.get('https://financialmodelingprep.com/api/v3/quote/' + self.symbol)
		except Exception as e:
			print(e)
		else:
			average_stock_price_50_day = float(json.loads(r.text)[0]['priceAvg50'])

		return average_stock_price_50_day

	def get_eps(self):
		"""Returns all the eps into a list"""
		r = requests.get('https://financialmodelingprep.com/api/v3/financials/income-statement/' + self.symbol)
		eps = []
		for item in json.loads(r.text)['financials']:
			try:
				eps.append(float(item['EPS']))
			except Exception as e:
				pass

		return eps

	def get_eps_length(self):
		eps = self.get_eps()
		return len(eps)

	def get_adjusted_eps(self):
		"""Returns the adjusted eps over num_eps_for_adj previous years"""
		eps = self.get_eps()
		adj_eps = 0
		iter_length = min(self.get_eps_length(), self.num_eps_for_adj)
		for i in range(1, iter_length):
			adj_eps = (adj_eps + eps[i]) / i

		return adj_eps

	def get_expected_growth(self):
		"""Returns the expected growth as an average eps from the quantity of num_for_avg_eps"""
		eps = self.get_eps()
		iter_length = min(self.get_eps_length(), self.num_for_avg_eps)
		expected_growth = 100*(abs((eps[iter_length - 1]-eps[0]) / (iter_length - 1)))/abs(eps[iter_length - 1])

		return expected_growth

	def get_company_fair_value(self):
		"""Returns the fair value of the company"""
		fair_value = self.get_adjusted_eps() * (self.no_growth_eps + self.growth_factor * self.get_expected_growth()) * 4.4 / self.Y

		return fair_value

class Symbols:
	def __init__(self, market):
		self.market = market # ETF|MUTUAL_FUND|COMMODITY|INDEX|CRYPTO|FOREX|TSX|AMEX|NASDAQ|NYSE|EURONEXT

	def get_all_symbols(self):
		"""Returns the list of symbols for each exchange"""
		r = requests.get('https://financialmodelingprep.com/api/v3/search?query=&exchange=' + self.market)
		symbols = []
		for item in json.loads(r.text):
			symbols.append(item['symbol'])

		return symbols

class UndervaluedCompany():
	def __init__(self, fair_value, actual_value, num_of_eps_statements, min_num_of_eps_statements = 4):
		self.fair_value = fair_value
		self.actual_value = actual_value
		self.num_of_eps_statements = num_of_eps_statements
		self.min_num_of_eps_statements = min_num_of_eps_statements

	def is_company_undervalued(self):
		if self.fair_value < self.actual_value and self.num_of_eps_statements > self.min_num_of_eps_statements:
			return True
		else:
			return False

class CompanyRecord:
	def __init__(self, company_symbol, fair_value, current_value, market):
		self.company_symbol = company_symbol
		self.fair_value = fair_value
		self.current_value = current_value
		self.document_name = str(market + '.txt')

	def create_record(self):
		"""Opens the document and werites info"""
		f = open(self.document_name, "a+")
		f.write("{}, current value:, {}, fair value:, {}\r".format(self.company_symbol, self.current_value, self.fair_value))
		print("Created record for {}".format(self.company_symbol))
		f.close()


