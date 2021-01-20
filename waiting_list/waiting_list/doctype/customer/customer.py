# -*- coding: utf-8 -*-
# Copyright (c) 2021, Tridz and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random

class Customer(Document):
	def codeGenerator(self):
		
		code_name=self.phone_number[-4:]
				
		upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
		numbers = "1234567890"
		lower = "qwertyuiopasdfghjklzxcvbnm"
		total = upper+numbers+lower
		length = 8
		self.referral = "".join(random.sample(total,length))
		self.referral_code=self.referral+code_name
		return self.referral_code
		
	def before_submit(self):
		self.referral_id = self.codeGenerator()
		customer_doc = frappe.db.get_all('Customer',fields=['customer','referral_id','phone_number','referred_by', 'name'])
	
		for i in customer_doc:
			if self.enter_referral_code:
				if i['referral_id'] == self.enter_referral_code:
					self.referred_by = i['phone_number']
					self.customer =i['name']
				

					doc=frappe.get_doc('Customer',self.customer)

					doc.append('referred_to', {
						'parent_field':'referred_to',
						'mobile_number': self.phone_number
					
					
					})
					doc.save()

		# child_tab =frappe.new_doc('Referred To')
		# child.update({
		# 	'mobile_number':self
		# })
		# doc.items.append(child_tab)


		# doc = frappe.get_doc({
    	# 'doctype': 'Referred To',
    	# 'parent': 'CUST - 0122',
		# #'mobile_number': self.referred_by
		# })
		# doc.insert()

		#doc = frappe.get_doc('Referred_to',self.referred_by)
				# referred_by_obj = frappe.db.get_value('Customer',{ "customer": i['customer']})		
				# referred_by_obj =frappe.get_value('Customer', i['customer'])
				# frappe.throw(i['customer'])
				# referred_doc=frappe.get_doc('Customer',self.referred_by)
				# frappe.throw(self.referred_by)
				# refto = referred_doc.referred_to
				# for d in refto:
				# 	d.customer_name = self.customer
				# 	d.mobile_number = self.phone_number
				# referred_by_customer_doc = frappe.db.set_value('Referred To',self.customer,'customer_name')	

				

				

				
				

		



	

		

		

	
	
		


	
