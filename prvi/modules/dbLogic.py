from modules import dbConfig

def getAll(koda = ""):
    
    # sql = """
    # SELECT * FROM tabela;
    # """.format(koda)
    
    try:
        # cursor.execute(sql)
        # r = cursor.fetchone()
        # obj = None
        # if r:
            # obj = NewObj(r[0], r[1], r[2], r[3], r[4], r[5], r[6], helper.dateToHTML(r[7]), r[8], r[9], r[10], r[11], r[12], r[13], r[14], r[15], r[16], r[17])
        # return obj
        
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.close()
        mydb.close()
        return True
    except:
        return False
    finally:
        pass