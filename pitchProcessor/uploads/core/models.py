from __future__ import unicode_literals

from django.db import models
import re


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class FileData(models.Model):
    translation = {
        "s": "Symbol Clears",
        "A": "Add Orders",
        "d": "Add Orders",
        "E": "Orders Executed",
        "X": "Cancel Orders",
        "P": "Trades",
        "r": "Trades",
        "B": "Trade Breaks",
        "H": "Trading Statuses",
        "I": "Auction Updates",
        "J": "Auction Summaries",
        "R": "Retail Price Improvements"
    }

    data = {
        "Symbol Clears": 0,
        "Add Orders": 0,
        "Orders Executed": 0,
        "Cancel Orders": 0,
        "Trades": 0,
        "Trade Breaks": 0,
        "Trading Statuses": 0,
        "Auction Updates": 0,
        "Auction Summaries": 0,
        "Retail Price Improvements": 0,
    }

    def is_valid_alpha(self, query):
        return re.search("^[A-Z]+\s*$", query)

    def is_valid_base36_numeric(self, query):
        return re.search("^0*[0-9A-Z]+$", query)

    def is_valid_numeric(self, query):
        return (re.search("^0*[0-9]+$", query))

    def is_valid_price(self, query):
        try:
            whole_number_string = query[0:5]
            decimal_string = query[6:9]

            return re.search("^0*[0-9]+$", whole_number_string) and re.search("[0-9]+0*$", decimal_string)
        except:
            return False

    def is_valid_printable_ASCII(self, query):
        for char in query:
            if ord(char) < 32 or ord(char) > 126:
                return False
        return True

    def is_valid_timestamp(self, query):
        return re.search("^0*[0-9]+$", query)

    def is_valid_line(self, line):
        try:
            msgType = line[9]

            if msgType == "s":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[10:17])

                return valid_timestamp and valid_stock_symbol
            elif msgType == "A":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                curr_order_id = line[10:21]
                valid_order_id = self.is_valid_base36_numeric(
                    self, curr_order_id)

                valid_side_indicator = line[22] == "B" or line[22] == "S"
                valid_shares = self.is_valid_numeric(self, line[23:28])
                curr_stock_symbol = line[29:34]
                valid_stock_symbol = self.is_valid_printable_ASCII(self,
                                                                   curr_stock_symbol)
                valid_price = self.is_valid_price(self, line[35:44])
                valid_display = self.is_valid_alpha(self, line[45])

                return valid_timestamp and valid_order_id and valid_side_indicator and valid_shares and valid_stock_symbol and valid_price and valid_display
            elif msgType == "d":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                curr_order_id = line[10:21]
                valid_order_id = self.is_valid_base36_numeric(
                    self, curr_order_id)
                valid_side_indicator = line[22] == "B" or line[22] == "S"
                valid_shares = self.is_valid_numeric(self, line[line[23:28]])
                curr_stock_symbol = line[29:36]
                valid_stock_symbol = self.is_valid_printable_ASCII(self,
                                                                   curr_stock_symbol)
                valid_price = self.is_valid_price(self, line[37:46])
                valid_display = self.is_valid_alpha(self, line[47])
                pID = line[48:51]
                valid_participantID = pID == "MPID" or pID == "RTAL" or pID == "    "

                return valid_timestamp and valid_order_id and valid_side_indicator and valid_shares and valid_stock_symbol and valid_price and valid_display and valid_participantID
            elif msgType == "E":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_order_id = self.is_valid_base36_numeric(
                    self, line[10:21])

                valid_executed_shares = self.is_valid_numeric(
                    self, line[22:27])
                curr_execution_id = line[28:39]
                valid_execution_id = self.is_valid_base36_numeric(self,
                                                                  curr_execution_id)

                return valid_timestamp and valid_order_id and valid_executed_shares and valid_execution_id
            elif msgType == "X":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])

                valid_order_id = self.is_valid_base36_numeric(
                    self, line[10:21])

                valid_canceled_shares = self.is_valid_numeric(
                    self, line[22:27])

                return valid_timestamp and valid_order_id and valid_canceled_shares
            elif msgType == "P":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_order_id = self.is_valid_base36_numeric(
                    self, line[10:21])
                valid_side_indicator = line[22] == "B" or line[22] == "S"
                valid_shares = self.is_valid_numeric(self, line[23:28])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[29:34])
                valid_price = self.is_valid_price(self, line[35:44])
                valid_execution_id = self.is_valid_base36_numeric(
                    self, line[45:56])

                return valid_timestamp and valid_order_id and valid_side_indicator and valid_shares and valid_stock_symbol and valid_price and valid_execution_id
            elif msgType == "r":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_order_id = self.is_valid_base36_numeric(
                    self, line[10:21])
                valid_side_indicator = line[22] == "B"
                valid_shares = self.is_valid_numeric(self, line[23:28])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[29:36])
                valid_price = self.is_valid_price(self, line[37:46])
                valid_execution_id = self.is_valid_base36_numeric(
                    self, line[47:58])

                return valid_timestamp and valid_order_id and valid_side_indicator and valid_shares and valid_stock_symbol and valid_price and valid_execution_id
            elif msgType == "B":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_execution_id = self.is_valid_base36_numeric(
                    self, line[10:21])
                return valid_timestamp and valid_execution_id
            elif msgType == "H":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[10:17])
                valid_halt_status = line[18] == "A" or line[18] == "H" or line[18] == "Q" or line[18] == "S" or line[19] == "T"
                valid_REG_SHO_Action = line[19] == "0" or line[19] == "1"
                valid_reserved1 = self.is_valid_alpha(self, line[20])
                valid_reserved2 = self.is_valid_alpha(self, line[21])
                return valid_timestamp and valid_stock_symbol and valid_halt_status and valid_REG_SHO_Action and valid_reserved1 and valid_reserved2
            elif msgType == "I":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[10:17])
                valid_auction_type = line[18] == "O" or line[18] == "C" or line[18] == "H" or line[18] == "I"
                valid_reference_price = self.is_valid_price(self, line[19])
                valid_buy_shares = self.is_valid_numeric(self, line[29:38])
                valid_sell_shares = self.is_valid_numeric(self, line[39:48])
                valid_indicative_price = self.is_valid_price(self, line[49:57])
                valid_auction_only_price = self.is_valid_price(
                    self, line[59:68])

                return valid_timestamp and valid_stock_symbol and valid_auction_type and valid_reference_price and valid_buy_shares and valid_sell_shares and valid_indicative_price and valid_auction_only_price
            elif msgType == "J":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[10:17])
                valid_auction_type = line[18] == "O" or line[18] == "C" or line[18] == "H" or line[18] == "I"
                valid_price = self.is_valid_price(self, line[19:28])
                valid_shares = self.is_valid_numeric(self, line[29:38])
                return valid_timestamp and valid_stock_symbol and valid_auction_type and valid_price and valid_shares
            elif msgType == "R":
                valid_timestamp = self.is_valid_timestamp(self, line[1:8])
                valid_stock_symbol = self.is_valid_printable_ASCII(
                    self, line[9:17])
                valid_retail_price_improvement = line[18] == "B" or line[
                    18] == "S" or line[18] == "A" or line[18] == "N"
                return valid_timestamp and valid_stock_symbol and valid_retail_price_improvement
            else:
                return False
        except:
            return False

    @classmethod
    def process_file(self, lines):
        for line in lines:
            # Allow for blank lines
            if line != '':
                if self.is_valid_line(self, line):
                    try:
                        msgType = line[9]
                        newKey = self.translation.get(msgType)
                        self.data[newKey] += 1
                    except:
                        return None
                else:
                    return None

        return self.data
