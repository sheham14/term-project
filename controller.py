from mysql_functions import *

def addProduct(pname, pdesc, vid, pqty, pprice):
    sql = f"INSERT INTO `easy_cheese`.`products` (`name`, `product_desc`, `vendor_id`, `qty`, `price`) VALUES ('{pname}', '{pdesc}', '{vid}', '{pqty}', '{pprice}');"
    return executeQueryAndCommit(sql)


def getAllProducts():
    sql = f"select * from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)


def getProductNameByID(pid):
    sql = f"SELECT * from `easy_cheese`.`products` where product_id = {pid}"
    prodInfo = executeQueryAndReturnResult(sql)[1][0]
    print('prodinfo', prodInfo)
    data = {'prod_id': prodInfo[0], 'name': prodInfo[1], 'desc': prodInfo[2], 'vid': prodInfo[3], 'qty': prodInfo[4], 'price': prodInfo[5]}
    print(data)
    return(data)


def getProductIdsAndNames():
    sql = f"select product_id, name from `easy_cheese`.`products`;"
    return executeQueryAndReturnResult(sql)


def updateProduct(pid, name, desc, vid, qty, price):
    sql = f"UPDATE `easy_cheese`.`products` SET name = '{name}', product_desc = '{desc}', vendor_id = {vid}, qty = {qty}, price = {price} where product_id = {pid};"
    return executeQueryAndCommit(sql)

def addCustomer(fname,lname, address, email, phone):
    sql = f"INSERT INTO `easy_cheese`.`customers` (`first_name`, `last_name`, `address`, `email_address`, `phone_number`) VALUES ('{fname}', '{lname}', '{address}', '{email}', '{phone}');"
    return executeQueryAndCommit(sql)

def editCustomer(cid, fname,lname, address, email, phone):
    sql = f"UPDATE `easy_cheese`.`customers` SET `first_name` = '{fname}', `last_name` = '{lname}', `address` = '{address}', `email_address` = '{email}', `phone_number` = '{phone}' WHERE (`customer_id` = '{cid}');"
    return executeQueryAndCommit(sql)

def getInvoices():
    sql = f"select * from `easy_cheese`.`invoices`;"
    return executeQueryAndReturnResult(sql)

def getActiveCustomers():
    sql = f"SELECT customer_id, date FROM easy_cheese.invoices where date >= date_sub(now(), Interval 1 month);"
    return executeQueryAndReturnResult(sql)

def getOutOfStock():
    sql = f"SELECT * FROM easy_cheese.products where in_store_qty = 0;"
    return executeQueryAndReturnResult(sql)