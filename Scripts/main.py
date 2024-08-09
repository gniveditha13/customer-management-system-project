import streamlit as st
import mysql.connector
import pandas as pd
import datetime

st.set_page_config(page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDP2dn1_yW23cez9mGeyJdjtuuMMozgjreIE_pkYuQiLQ1Lplwe480ZTuccPAK3YYa7FY&usqp=CAU",page_title="Cusomer Management System")
st.markdown("<h1 style='text-align: center; color:orange'>CUSTOMER MANAGEMENT SYSTEM</h1>",unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center'>Welcome to Customer Mangement System!!</h6>",unsafe_allow_html=True)
custom_css="""
    <style>
    .st-b8 {
        background-color:orange;
        color:white;
         font-weight: bold;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
choice=st.sidebar.selectbox("MENU",("Home","Admin"))

if(choice=="Home"):
        st.image("https://cdn.dribbble.com/users/8619169/screenshots/16192755/media/188ce2fd1f246d546a189132510750e1.gif")      

elif(choice=="Admin"):
        if "islogin" not in st.session_state:
                st.session_state["islogin"]=False
        admin_id=st.text_input("Enter admin id: ")
        admin_email=st.text_input(label="Email: ",
                        max_chars=30,
                        placeholder="enter email here",)
        admin_pwd=st.text_input(
                label="Password: ",
                max_chars=20,
                placeholder="password here",
                type="password")
        btn=st.button("Login")
        if(btn):
             mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
             c=mydb.cursor()
             c.execute("select * from admin_details")
             mydata=c.fetchall()
             for i in mydata:
                     if(i[0]==admin_id and i[2]==admin_email and i[3]==admin_pwd):
                             st.session_state["islogin"]=True
                             break
             if(not st.session_state["islogin"]):
                     st.error("Incorrect ID or Password")
        if(st.session_state["islogin"]==True):
                st.success("Login Successfull..!!")
                choice2=st.sidebar.selectbox("Explore More",("--Choose here--","Customer Details","Categories","Products","Orders","Ordered Item Details"))

                if(choice2=="Customer Details"):
                        custchoice=st.selectbox("Select the required features:-",("--Select--","All Cutomers Record","Add New Customer Details","Search Customer Details","Update Customer Details","Delete Customer Record"))

                        if(custchoice=="All Cutomers Record"):
                                Viewbtn=st.button("Display record")
                                if(Viewbtn):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("select * from customer_details")
                                        st.subheader("Customer Details: ")
                                        custcolumns=("ID","First Name","Last Name","DOB","Email","Password","Phone number","Address","State","Country","Availability")
                                        custdata=c.fetchall()
                                        df=pd.DataFrame(data=custdata,columns=custcolumns)
                                        st.dataframe(df)

                        elif(custchoice=="Add New Customer Details"):
                                st.header("Enter customer details:")
                                cus_id=st.text_input("Customer id:")
                                cus_fname=st.text_input("First name: ")
                                cus_lname=st.text_input("Last name: ")
                                cus_dob=st.date_input("DOB: ",
                                                      value=datetime.date(1995,5,13))
                                cus_email=st.text_input("Email id: ")
                                cus_pwd=st.text_input("Password: ")
                                cus_phno=st.text_input("Phone number: ")
                                cus_address=st.text_input("Address: ")
                                cus_state=st.text_input("State: ")
                                cus_country=st.text_input("Country: ")
                                cus_availability=st.text_input("Availability: ")
                                addbtn=st.button("Submit")
                                if(addbtn):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("insert into customer_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(cus_id,cus_fname,cus_lname,cus_dob,cus_email,cus_pwd,cus_phno,cus_address,cus_state,cus_country,cus_availability))
                                        mydb.commit()
                                        st.success("Customer details added successfully!")

                        elif(custchoice=="Search Customer Details"):
                                st.subheader("Fill the details to fetch particular customer details: ")
                                cus_id=st.text_input("Customer id:")
                                fetchbtn=st.button("Search")
                                if(fetchbtn):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("Select * from customer_details where cust_id=%s",(cus_id,))
                                        cusdata=c.fetchall()[0]
                                        st.subheader("_Coustomer details:_")
                                        st.write("**Customer Id:**  ",cusdata[0])
                                        st.write("**First Name:**  ",cusdata[1])
                                        st.write("**Last Name:**  ",cusdata[2])
                                        st.write("**Email:**  ",cusdata[4])
                                        st.write("**Phone Number:**  ",cusdata[6])
                                        st.write("**Address:**  ",cusdata[7])
                                        st.write("**Country:**  ",cusdata[9])


                                        
                        elif(custchoice=="Update Customer Details"):
                                st.subheader("Fill the details to update particular customer details: ")
                                cus_id=st.text_input("Customer id:")
                                cus_phno=st.text_input("Phone number: ")
                                cus_address=st.text_input("Address: ")
                                cus_availability=st.text_input("Enter whether the customer available or not:")
                                updatebtn=st.button("Update")
                                if(updatebtn):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("update customer_details set phone=%s,address=%s,availability=%s where cust_id=%s",(cus_phno,cus_address,cus_availability,cus_id))
                                        mydb.commit()
                                        st.success("Updated successfully!")

                        elif(custchoice=="Delete Customer Record"):
                                cus_id=st.text_input("Customer id:")
                                dltbtn=st.button("Delete record")
                                if(dltbtn):
                                         mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                         c=mydb.cursor()
                                         c.execute("delete from customer_details where cust_id=%s",(cus_id,))
                                         mydb.commit()
                                         st.success("Customer data deleted successfully!")

                elif(choice2=="Categories"):
                        catchoice=st.radio("Select required category:- ",("Electronics","Fashion & Beauty","Home Decor","Sports & Fitness"))
                        
                        if(catchoice=="Electronics"):
                                elec_choice=st.selectbox("Click dropdown to view Electronic products:-",("--View here--","Laptops","Smart Phones","Televisions","Smart Watches","Headphones"))
                        elif(catchoice=="Fashion & Beauty"):
                               fb_choice=st.selectbox("Click dropdown to view Fashion & Beauty Products:-",("--View here--","Women's Clothing","Men's Clothing","Kid's Fashion","Beauty & Makeup","Footwear","Jewellery"))
                        elif(catchoice=="Home Decor"):
                               hd_choice=st.selectbox("Click dropdown to view Home Decor Products:-",("--View here--","Home Decor","Home Storage","Indoor Lightening","Garden & Outdoor Decor","Handloom & Handcrafts"))
                        elif(catchoice=="Sports & Fitness"):
                                sf_choice=st.selectbox("Click dropdown to view Sports & Fitness Products:-",("--View here--","Fitness & Sports Equipments","Sports Clothing","Sports Shoes","Health Drinks"))
                                

                elif(choice2=="Products"):    
                    prodchoice=st.selectbox("Select required option:- ",("--Select--","View All Products","Add New Products","Search Product","Update Product","Delete Products"))
                    
                    if(prodchoice=="View All Products"):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("select * from product_details")
                                        st.subheader("Product Details: ")
                                        prodcolumns=("ID","Name","Description","Price","In Stock")
                                        proddata=c.fetchall()
                                        df=pd.DataFrame(data=proddata,columns=prodcolumns)
                                        st.dataframe(df)

                    elif(prodchoice=="Add New Products"):
                            st.header("Enter product details to add new product")
                            prod_id=st.text_input("Product id: ")
                            prod_name=st.text_input("Name: ")
                            prod_desc=st.text_input("Description: ")
                            prod_price=st.text_input("Price per unit: ")
                            prod_instock=st.number_input(
                                    label="In stock quantity: ",
                                    max_value=100,
                                    value=0,
                                    step=0)
                            addprod=st.button("Add Product")
                            if(addprod):
                                    mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                    c=mydb.cursor()
                                    c.execute("insert into product_details values(%s,%s,%s,%s,%s)",(prod_id,prod_name,prod_desc,prod_price,prod_instock))
                                    c=mydb.commit()
                                    st.success("Product added successfully..!")

                    elif(prodchoice=="Search Product"):
                            st.header("Enter product details to search the product")
                            prod_id=st.text_input("Product id: ")
                            searchprod=st.button("Search")
                            if(searchprod):
                                    mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                    c=mydb.cursor()
                                    c.execute("Select * from product_details where prod_id=%s",(prod_id,))
                                    proddata=c.fetchall()[0]
                                    st.subheader("Product details:")
                                    st.write("**Product Id:**  ",proddata[0])
                                    st.write("**Name:**  ",proddata[1])
                                    st.write("**Description:**  ",proddata[2])
                                    st.write("**Price:**  ",proddata[3])
                                    st.write("**In Stock:**  ",proddata[4])
                                    
                                    
                    elif(prodchoice=="Update Product"):
                            st.header("Enter product details to update the product")
                            prod_id=st.text_input("Product id: ")
                            prod_desc=st.text_input("Description: ")
                            prod_price=st.text_input("Price per unit: ")
                            prod_instock=st.number_input(label="In stock quantity: ",
                                                       max_value=100,
                                                       value=0,
                                                       step=0)
                            updateprod=st.button("Update")
                            if(updateprod):
                                    mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                    c=mydb.cursor()
                                    c.execute("update product_details set prod_description=%s,price=%s,in_stock=%s where prod_id=%s",(prod_desc,prod_price,prod_instock,prod_id))
                                    c=mydb.commit()
                                    st.success("Product updated successfully..!")

                    elif(prodchoice=="Delete Products"):
                         st.header("Enter product details to delete the product")
                         prod_id=st.text_input("Product id: ")   
                         dltprod=st.button("Delete product")
                         if(dltprod):
                                mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                c=mydb.cursor()
                                c.execute("delete from product_details where prod_id=%s",(prod_id,))
                                c=mydb.commit()
                                st.success("Product deleted successfully..!")

                elif(choice2=="Orders"):
                       ord_details_choice=st.selectbox("Select required option:-",("--Select--","View Orders","Add New Order","Update Order Status","Cancel Order"))

                       if(ord_details_choice=="View Orders"):
                                mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                c=mydb.cursor()
                                c.execute("select * from ord_details")
                                st.subheader("Orders details: ")
                                ordcolumns=("Order Id","Customer Id","Order Date","Total Ammount","Payment Method","Order Status")
                                orddata=c.fetchall()
                                df=pd.DataFrame(data=orddata,columns=ordcolumns)
                                st.dataframe(df)
                                
                       elif(ord_details_choice=="Add New Order"):
                               st.subheader("Enter order details to add new order ")
                               ord_id=st.text_input("Order Id: ")
                               cus_id=st.text_input("Customer Id: ")
                               ord_date=st.date_input("Ordered Date: ",value=datetime.date(2024,5,13))
                               tot_amt=st.text_input("Total amount: ")
                               payment_method=st.text_input("Payment Type: ")
                               ord_status=st.text_input("Status: ")
                               addord=st.button("Add")
                               if(addord):
                                       mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                       c=mydb.cursor()
                                       c.execute("insert into ord_details values(%s,%s,%s,%s,%s,%s)",(ord_id,cus_id,ord_date,tot_amt,payment_method,ord_status))
                                       c=mydb.commit()
                                       st.success("Order inserted successfully..!")
                               

                       elif(ord_details_choice=="Update Order Status"):
                                st.subheader("Enter order details to update the order ")
                                ord_id=st.text_input("Order Id: ")
                                ord_status=st.text_input("Status: ")
                                updateord=st.button("Update")
                                if(updateord):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("update ord_details set ord_status=%s where ord_id=%s",(ord_status,ord_id))
                                        c=mydb.commit()
                                        st.success("Updated status successfully..!")

                       elif(ord_details_choice=="Cancel Order"):
                                st.header("Enter order details to cancel the product")
                                ord_id=st.text_input("Order id: ")   
                                cancelord=st.button("Cancel")
                                if(cancelord):
                                        mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                        c=mydb.cursor()
                                        c.execute("delete from ord_details where ord_id=%s",(ord_id,))
                                        c=mydb.commit()
                                        st.success("Order cancelled successfully..!")

                       
                elif(choice2=="Ordered Item Details"):
                          item_details_choice=st.selectbox("Select required option:-",("View Ordered Items","Delete Details"))

                          if(item_details_choice=="View Ordered Items"):
                                  
                                mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                c=mydb.cursor()
                                c.execute("select * from ordered_items_details")
                                st.subheader("Ordered items record: ")
                                orditemcolumns=("Order Item Id","Order Id","Product Id","Quantity Purchased","Unit Price")
                                orditemdata=c.fetchall()
                                df=pd.DataFrame(data=orditemdata,columns=orditemcolumns)
                                st.dataframe(df)

                          elif(item_details_choice=="Delete Details"):
                               st.header("Enter ordered item details to delete")
                               item_id=st.text_input("Ordered item id: ")   
                               dltitem=st.button("Delete")
                               if(dltitem):
                                          mydb=mysql.connector.connect(host="localhost",user="root",password="nivi24",database="customer_management_system")
                                          c=mydb.cursor()
                                          c.execute("delete from ordered_item_details where ord_item_id=%s",(item_id,))
                                          c=mydb.commit()
                                          st.success("Deleted successfully..!")


           


