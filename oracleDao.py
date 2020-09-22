import cx_Oracle



# now = datetime.now()
# print(now)  # 2018-07-28 12:11:32.669083
#
# nowDate = now.strftime('%Y-%m-%d')
# print(nowDate)  # 2018-07-28
#
# nowTime = now.strftime('%H:%M:%S')
# print(nowTime)  # 12:11:32
#
# nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
# print(nowDatetime)  # 2018-07-28 12:11:32


def select():
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = "select entry_id, en_car, en_time, ex_time from entry_info_view"
    cursor.execute(sql)
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()


def insert(t):
    print(t)
    print(type(t))
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """insert into entry_info_view (entry_id, en_car, en_time, res_name)
          values (entry_info_seq.nextval, :1, sysdate, '경기 상송마을 주공아파트')"""
    cursor.execute(sql, (t,))
    cursor.close()
    conn.commit()
    conn.close()


def update(t):
    print(t)
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """update entry_info_view 
        set ex_time = sysdate where en_car = :1"""
    cursor.execute(sql, (t,))
    cursor.close()
    conn.commit()
    conn.close()


def hpSearchStartDate(t):
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            select to_timestamp(to_char(start_date, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            from hp_book_view where hp_name = (select hp_name from hp where res_name = '경기 상송마을 주공아파트')
            and car_num = :1
            and start_date
            between to_timestamp(to_char(sysdate - 60/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            and to_timestamp(to_char(sysdate + 60/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
        """
    cursor.execute(sql, (t,))
    returner = cursor.fetchone()
    date = returner[0]
    print(str(date))
    cursor.close()
    conn.commit()
    conn.close()
    return date


def scsSearchStartDate(t):
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            select to_timestamp(to_char(start_date, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            from scs_book_view where scs_name = (select scs_name from scs where res_name = '경기 상송마을 주공아파트')
            and car_num = :1
            and start_date
            between to_timestamp(to_char(sysdate - 10/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            and to_timestamp(to_char(sysdate + 10/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
        """
    cursor.execute(sql, (t,))
    returner = cursor.fetchone()
    date = returner[0]
    print(str(date))
    cursor.close()
    conn.commit()
    conn.close()
    return date


def hpSubPlace():
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            update hp_ch_pl_view set place = place - 1
            where res_name = '경기 상송마을 주공아파트'
        """
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def scsSubPlace():
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            update scs_ch_pl_view set scs_amount = scs_amount - 1
            where res_name = '경기 상송마을 주공아파트'
        """
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def hpSearchEndDate(t):
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            select to_timestamp(to_char(end_date, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            from hp_book_view where hp_name = (select hp_name from scs where res_name = '경기 상송마을 주공아파트')
            and car_num = :1
            and start_date
            between to_timestamp(to_char(sysdate - 360/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            and to_timestamp(to_char(sysdate + 360/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
        """
    cursor.execute(sql, (t,))
    returner = cursor.fetchone()
    date = returner[0]
    print(str(date))
    cursor.close()
    conn.commit()
    conn.close()
    return date


def scsSearchEndDate(t):
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            select to_timestamp(to_char(start_date, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            from scs_book_view where scs_name = (select scs_name from scs where res_name = '경기 상송마을 주공아파트')
            and car_num = :1
            and start_date
            between to_timestamp(to_char(sysdate - 360/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
            and to_timestamp(to_char(sysdate + 360/24/60, 'yyyy-mm-dd hh24:mi:ss'), 'yyyy-mm-dd hh24:mi:ss')
        """
    cursor.execute(sql, (t,))
    returner = cursor.fetchone()
    date = returner[0]
    print(str(date))
    cursor.close()
    conn.commit()
    conn.close()
    return date


def hpAddPlace():
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            update hp_ch_pl_view set place = place - 1
            where res_name = '경기 상송마을 주공아파트'
        """
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()


def scsAddPlace():
    conn = cx_Oracle.connect("test4/test4@localhost:1521/xe")
    cursor = conn.cursor()
    sql = """
            update scs_ch_pl_view set scs_amount = scs_amount - 1
            where res_name = '경기 상송마을 주공아파트'
        """
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()