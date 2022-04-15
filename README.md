<h1>GST TAX MANAGEMENT SYSTEM</h1>

# Introduction </h2>
Different business owners can view and pay their pending taxes and Accountants can issue taxes to different businesses.<br>
### There are 3 roles.<br><br>

## 1. Admin
#### -Admin can view all the information and control users.<br>
### Testing:
1. To open admin panel go to: 'Server-address / admin'. For this repo go to: (http://127.0.0.1:9696/admin/)
2. Enter Username: admin ,   Password = password
3.The admin can see everyone's taxes.
4. Accountet Setting: From Admin Panel, go to User Table and change role of Account we created to Accountant from Tax-Payer.</l>


## 2. Accountant
#### -The Accountants can look over all businesses and issue a tax-receipt.
### Testing:
The accountant account can be created only by admin. 
1. Create a user account.(dont need to register bussiness in this case)
2. open the admin panel: (http://127.0.0.1:9696/admin/)
3. Open the User Table and update the function of craeted user account to Accountant from Tax-Payer.
4. To Edit data of Tax-Payer and issue tax: Login as accountant and all data realated to registered users bussiness could be seen. Accountant can edit and update data from here.


## 3. Tax Payer
#### - The Tax Payers can look over and revise its tax until the due date is passed.
### Testing:
1. SignUp from Home page to create a tax-payer account.
2. Register the Bussiness
3. On successful registration, user will be redirected to other page with Welcome message, name and due tax (on first login it will show "No Due" text)


## Steps to Run :

1. Clone the repo
2. Open terminal inside GST-App folder
3. Run the commands:

(if testing on local machine try port no.: 9696 . If any error encounters, please change port number.)


```
docker image build -t GST-App .

docker run -p 9696:9696 -d GST-App
```


## Sample accounts for testing:

#### TAX PAYER account:
Name: Tax Payer <br>
Email: tax-payer@gmail.com <br>
Password: 123

#### ACCOUNTANT account:
Name: Accountant <br>
Email: accountant@gmail.com <br>
Password: 123
