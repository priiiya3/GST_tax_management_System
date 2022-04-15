<h1>GST TAX MANAGEMENT SYSTEM</h1>
Different business owners can view and pay their pending taxes and Accountants can issue taxes to different businesses.
There are 3 roles.<br><br>
<l>1-<h1>Admin</h1>-Admin can view all the information and control users.</l><br>
<l>2-<h1>Accountant</h1>-The Accountants can look over all businesses and issue a tax-receipt.</l><br>
<l>3-<h1>Tax Payer</h1>- The Tax Payers can look over and revise its tax until the due date is passed.</l><br>
<br>
<br>

<h1>Steps to Run :</h1>
<br>
<l>1- Clone the repo</l><br>
<l>2- Open terminal inside GST-App folder</l><br>
<l>3- Run the commands:</l><br>

```
docker image build -t gst-flask-app .

docker run -p 2000:5000 -d gst-flask-app
```

<h1>For Testing</h1>

```
To Create Tax-Payer Account:
<l>Home >> Create Account >> Enter email, name and password</l>

```

