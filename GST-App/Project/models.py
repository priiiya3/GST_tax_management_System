from datetime import datetime
from Project import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_of_registration = db.Column(db.DateTime, default=datetime.utcnow)
    role = db.Column(db.Enum("Tax_Payer", "Accountant"), default="Tax_Payer")

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.email}', '{self.date_of_registration}','{self.role}')"


class TaxPayer(db.Model):
    id = db.Column(db.ForeignKey(User.id), primary_key=True)
    gst_num = db.Column(db.String(15), unique=True)
    pan_num = db.Column(db.String(10), unique=True)
    business_name = db.Column(db.String(500), nullable=False)
    date_of_registration = db.Column(db.DateTime, default=datetime.utcnow)
    constitution = db.Column(db.Enum("Individual", "Partnership", "Company", "HUF"))
    address = db.Column(db.String(500))

    def __repr__(self):
        return f"Tax-Payer('{self.id}','{self.gst_num}', '{self.pan_num}', '{self.business_name}', '{self.date_of_registration}', '{self.constitution}', '{self.address}')"


class Tax(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    associated_payer = db.Column(db.ForeignKey(TaxPayer.id))
    business_name = db.Column(db.ForeignKey(TaxPayer.business_name))
    gst_num = db.Column(db.ForeignKey(TaxPayer.gst_num))
    pan_num = db.Column(db.ForeignKey(TaxPayer.pan_num))
    title = db.Column(db.String(100))
    total_amount = db.Column(db.String(15))
    transaction_type = db.Column(db.Enum("Interstate", "Intrastate"))
    GST = db.Column(db.String(15))
    CGST = db.Column(db.String(15))
    IGST = db.Column(db.String(15))
    SGST = db.Column(db.String(15))
    Penalty = db.Column(db.String(15))
    net_income = db.Column(db.String(15))
    total_tax = db.Column(db.String(15))
    issued_by = db.Column(db.String(100))
    due_date = db.Column(db.Date)

    def __repr__(self):
        return f"Tax('{self.gst_num}', '{self.total_tax}', '{self.due_date}')"
