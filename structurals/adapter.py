"""
    Adapter:
        is a structural design pattern that allows objects with incompatible interfaces to collaborate. 
"""

import json
import xmltodict


class ExternalPaymentGateway:
    def get_payment_data_xml(self):
        return '<payment><amount>100.00</amount><currency>USD</currency></payment>'

class InternalPaymentProcessor:
    def process_payment_json(self, payment_data):
        return f"Processed payment: {json.dumps(payment_data)}"

class PaymentAdapter:
    def __init__(self, external_payment_gateway):
        self.external_payment_gateway = external_payment_gateway

    def get_payment_data_json(self):
        xml_data = self.external_payment_gateway.get_payment_data_xml()
        json_data = xmltodict.parse(xml_data)
        return json_data


external_payment_gateway = ExternalPaymentGateway()
payment_adapter = PaymentAdapter(external_payment_gateway)
payment_data_json = payment_adapter.get_payment_data_json()

internal_payment_processor = InternalPaymentProcessor()
result = internal_payment_processor.process_payment_json(payment_data_json)

print(result)
