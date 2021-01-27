# -*- coding: utf-8 -*-
# Copyright (c) 2021, Tridz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random

class Customer(Document):
	pass
'''
	def codeGenerator(self):

		##Random code is generated using upper and lower case alphabets,numbers and last four digits of new customer's phone number

		code_name=self.phone_number[-4:] ##slice last 4 digits of customer phone number
				
		upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
		numbers = "1234567890"
		lower = "qwertyuiopasdfghjklzxcvbnm"
		total = upper+numbers+lower
		length = 8  ##length of code is defined to 8 
		self.referral = "".join(random.sample(total,length)) ##randomly generates code
		self.referral_code=self.referral+code_name ##last four digits of phone number is added to the randomly generated code
		return self.referral_code
		
	def before_save(self):
		customer_doc = frappe.db.get_all('Customer',fields=['customer','referral_id','phone_number','referred_by', 'name'])

		for d in customer_doc:
			if not d['referral_id']:
				self.referral_id = self.codeGenerator() ##randomly generated code passed to referral id field of new customer upon submission of document

		##if new customer is created using existing customers referral code, phone number of existing customer whose referral id is used will be passed to referred by field of new customer
		

		for i in customer_doc:
			if self.enter_referral_code:
				if i['referral_id'] == self.enter_referral_code: ##checks if enterd referral code matches with existing referral ids 
					self.referred_by = i['phone_number']  ##if it is matched, phone number of existing customer whose referral id is used will be passed to referred by field of new customer
					self.customer =i['name'] ##customer id of existing customer is passed to the name field of doc
				
				##upon creation of new customer who used referral id's of existing customers,new customers mobile number is added to the referred to table of existing customer whose referral id is used by new customer.
					doc=frappe.get_doc('Customer',self.customer)

					doc.append('referred_to', {
						'parent_field':'referred_to',
						'mobile_number': self.phone_number	
					})
					doc.save()

		validate_doc = frappe.db.get_list("Customer",filters={'phone_number': self.phone_number})
		if validate_doc:
			y = validate_doc[0]['name']
			b = frappe.get_doc("Customer", y)
			b.number_of_attempts = int(b.number_of_attempts) + 1
			self.val = 1
			self.phone_number = 0
			b.save()


	# def before_save(self):
	# 	validate_doc = frappe.db.get_list("Customer",filters={'phone_number': self.phone_number})
	# 	if validate_doc:
	# 		y = validate_doc[0]['name']
	# 		b = frappe.get_doc("Customer", y)
	# 		b.number_of_attempts = int(b.number_of_attempts) + 1
	# 		self.val = 1
	# 		self.phone_number = 0
	# 		b.save()

	def after_insert(self):
		if self.val == 1:
			frappe.throw("Mobile Number already registered")

'''
			

							
				

		



	

		

		

	
	
		


	
