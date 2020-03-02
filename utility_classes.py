import requests
import json
from pprint import pprint

class FairValue():
	def __init__(self, symbol, regression_data_points, num_financial_eps, market, Y = 1.8, no_growth_eps = 7, growth_factor = 1):
		self.symbol = symbol
		self.regression_data_points = regression_data_points
		self.num_financial_eps = num_financial_eps
		self.market = market # ETF|MUTUAL_FUND|COMMODITY|INDEX|CRYPTO|FOREX|TSX|AMEX|NASDAQ|NYSE|EURONEXT
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
		pass

	def get_average_eps(self):
		pass

	def get_expected_growth(self):
		pass

	def company_fair_value(self):
		"""Returns the fair value of the company"""
		fair_value = self.get_average_eps() * (self.no_growth_eps + self.growth_factor * self.get_expected_growth()) * 4.4 / self.Y

		return fair_value

class Symbols:
	def __init__(self, market):
		self.market = market

	def return_all_symbols(self):
		r = requests.get('https://financialmodelingprep.com/api/v3/search?query=&exchange=' + self.market)
		symbols = []
		for item in json.loads(r.text):
			symbols.append(item['symbol'])

		return symbols

class UndervaluedCompanies():
	def __init__(self, fair_value, actual_value):
		pass

	def return_undervalued_company(self):
		if self.is_company_undervalued():
			return True
		else:
			return False

	def is_company_undervalued(self):
		if self.fair_value < self.actual_value:
			return True
		else:
			return False

