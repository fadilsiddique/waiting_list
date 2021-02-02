from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import random



@frappe.whitelist()
def test_method():
    return("hello3")

def code_generator(mobile_number):
    code_name=mobile_number[-4:] # slice last 4 digits of customer phone number				
    upper, numbers, lower = "QWERTYUIOPASDFGHJKLZXCVBNM", "1234567890", "qwertyuiopasdfghjklzxcvbnm"
    total = upper+numbers+lower
    length = 8  # length of code is defined to 8 
    referral = "".join(random.sample(total,length)) # randomly generates code
    referral_code=referral+code_name # last four digits of phone number is added to the randomly generated code
    return referral_code

@frappe.whitelist()
def create_customer(mobile_number, vehicle, refer_code=None):
    referral_id = code_generator(mobile_number)  # Create  referral id for the user

    # Adds +1 to field number_of_attempts if a customer with the same mobile number already exists in the database.
    validate_doc = frappe.db.get_list("Customer",filters={'phone_number': mobile_number})
    if validate_doc:
        cus_id = validate_doc[0]['name']
        b = frappe.get_doc("Customer", cus_id)
        b.number_of_attempts = int(b.number_of_attempts) + 1
        b.save()
        return_val = {"alert": "Already Registered", "refer_id": b.referral_id}
        return (return_val)
    # If the passed mobile number is not in the database, a new customer is created.
    else:
        #frappe.throw("Hello")
        cus_doc = frappe.new_doc("Customer")
        cus_doc.phone_number = mobile_number
        cus_doc.vehicle_name = vehicle
        cus_doc.referral_id = referral_id
        cus_doc.insert()
        if refer_code: # Add the referrer id and number to the doc if referral code exist
            referred_customer = frappe.db.get_list('Customer',filters={'referral_id': refer_code}, fields=['name', 'phone_number'])
            if referred_customer:
                cus_doc.enter_referral_code = refer_code
                cus_doc.referred_by = referred_customer[0]['phone_number']
                cus_doc.customer = referred_customer[0]['name']
                customer_name = referred_customer[0]['name']
                parent_doc = frappe.get_doc("Customer", customer_name) # Adds the customer number to the referrer doc table(Refferd To)
                parent_doc.append('referred_to', {
                    'parent_field':'referred_to',
                    'mobile_number': mobile_number,
                    'customer_id': cus_doc.name
                })
                parent_doc.save()
                cus_doc.save()
        return_val = {"refer_id": cus_doc.referral_id}
        return return_val
    
    
