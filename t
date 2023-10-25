class Customer(BaseModel):
    num_of_cust = 0
    acct_num = ""
    
    def __init__(self, first, last, dob, sex, email, acct_type, phone="", addr="", mid=""):
        if name_check(first) and name_check(last) and valid_dob(dob) and acct_check(acct_type) and phone_check(phone) and addr_check(addr) and mid_check(mid):
            super().__init__()
            self.first = first
            self.last = last
            self.dob = dob
            self.sex = sex
            self.email = email
            self.mid = ""
            self.phone = ""
            self.addr = ""
            Customer.num_of_cust += 1
            self.create_acct(acct_type)
        
        
    
    
    def create_acct(self, acct_type):
        random_number = random.randint(0, 999999999)
        if acct_type == 'savings':
            acct_number = '1' + str(random_number).zfill(9)
        elif acct_type == 'current':
            acct_number = '0' + str(random_number).zfill(9)
        self.acct_num = acct_number
        return f"This is your acct number {acct_number}"
        
        
class Account(Customer):
    all_accts = []
    
    def __init__(self, customer):
        if isinstance(customer, Customer):
            self.id = customer.id
            self.acct_num = customer.acct_num
            self.acct_bal = 0
            self.tid_list = []
            Account.all_accts.append(self)
        else:
            return "Kindly provide a valid bank user"
        
        
    def deposit(self, amt):
        
        if isinstance(amt, float) or isinstance(amt, int):
        
            self.acct_bal += amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Credit", str(amt)]})
        else:
            return "Pls provide a valid amount"
        
    def withdraw(self, amt):
                
        if isinstance(amt, float) or isinstance(amt, int):
            if amt > self.acct_bal:
                return "Request declined, Insufficient Balance"

            self.acct_bal -= amt
            tid = uuid.uuid4()
            self.tid_list.append({str(tid): ["Debit", str(amt)]})
        else:
            return "Pls provide a valid amount"
        
    def transfer(self, amt, acct_number):
        
        if not isinstance(amt, float) and not isinstance(amt, int):
            return "Pls enter a valid amount"
        
        for obj in Account.all_accts:
            if self.acct_num == acct_number:
                return "Transaction not allowed"
            if obj.acct_num == acct_number:
                if amt > self.acct_bal:
                    return "Request declined, Insufficient Balance"
                else:
                    obj.acct_bal += amt
                    tid = uuid.uuid4()
                    obj.tid_list.append({str(tid): ["Credit", str(amt)]})
                    break
        else:
            return "acct not found"
            
        self.acct_bal -= amt
        self.tid_list.append({str(tid): ["Debit", str(amt)]})
        
