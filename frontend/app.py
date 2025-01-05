# streamlitの画面
import streamlit as st
import datetime
import json
import requests
import pandas as pd


page = st.sidebar.selectbox('Choose your page!',['利用者登録', '会議室登録', '会議室予約'])

if page=='利用者登録':
    st.title('利用者登録画面')

    with st.form('users'):
        user_name: str = st.text_input('利用者名',max_chars=12)
        data = {
            'user_name':user_name
        }
        submit_button = st.form_submit_button(label='利用者登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/users'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('利用者登録完了')
        st.write(res.status_code)
        st.json(res.json())

elif page=='会議室登録':
    st.title('会議室登録画面')
    with st.form('rooms'):
        # room_id:int = random.randint(0, 10)
        room_name: str = st.text_input('会議室名',max_chars=12)
        capacity: int = st.number_input('定員数', step=1)
        data = {
            'room_name': room_name,
            'capacity': capacity
        }
        submit_button = st.form_submit_button(label='会議室登録')

    if submit_button:
        url = 'http://127.0.0.1:8000/rooms'
        res = requests.post(
            url,
            data=json.dumps(data)
        )
        if res.status_code == 200:
            st.success('会議室登録完了')
        
        st.json(res.json())

elif page=='会議室予約':
    st.title('会議室予約画面')
    
    # 利用者一覧を取得する。
    url_users = 'http://127.0.0.1:8000/users'
    res = requests.get(url_users)
    users = res.json()
    # 利用者名をキーとして、利用者IDをバリューに設定
    users_name = {}
    for user in users:
        users_name[user['user_name']] = user['user_id']
    
    # 会議室一覧取得
    st.write('## 会議室一覧')
    url_rooms = 'http://127.0.0.1:8000/rooms'
    res = requests.get(url_rooms)
    rooms = res.json()
    rooms_name = {}
    for room in rooms:
        rooms_name[room['room_name']] = {
            'room_id': room['room_id'],
            'capacity': room['capacity']
        }
    df_rooms = pd.DataFrame(rooms)
    df_rooms.columns = ['会議室名', '定員', '会議室ID']
    st.table(df_rooms)
    
    # 予約一覧取得
    st.write('## 予約一覧')
    url_booking = 'http://127.0.0.1:8000/booking'
    res = requests.get(url_booking)
    bookings = res.json()
    # print(bookings)
    
    if bookings:
        
        df_bookings = pd.DataFrame(bookings)
        
        # 辞書型の作成
        users_id = {}
        for user in users:
            users_id[user['user_id']] = user['user_name']
            
        rooms_id = {}
        for room in rooms:
            rooms_id[room['room_id']] = {
                'room_name': room['room_name'],
                'capacity': room['capacity']
            }
        
        # IDを各値に変更する(ラムダ関数を使用)
        to_user_name = lambda x: users_id[x]
        to_room_name = lambda x: rooms_id[x]['room_name']
        # datetimeのフォーマット変換
        to_datetime = lambda x: datetime.datetime.fromisoformat(x).strftime('%Y/%m/%d %H:%M')
        
        # 特定の列に適用させる
        df_bookings['user_id'] = df_bookings['user_id'].map(to_user_name)
        df_bookings['room_id'] = df_bookings['room_id'].map(to_room_name)
        df_bookings['start_datetime'] = df_bookings['start_datetime'].map(to_datetime)
        df_bookings['end_datetime'] = df_bookings['end_datetime'].map(to_datetime)
        
        df_bookings = df_bookings.rename(columns={
            'user_id': '予約者名',
            'room_id': '会議室名',
            'booked_num': '予約人数',
            'start_datetime': '開始時刻',
            'end_datetime': '終了時刻',
            'booking_id': '予約番号'
        })
        
        st.table(df_bookings)
    
    else:
        st.write('現在、予約されている会議室はございません。')    
    
    st.write('## 会議室予約フォーム')
    with st.form('booking'):
        # booking_id:int = random.randint(0, 10)
        user_name: str = st.selectbox('予約者名',users_name.keys())
        room_name: str = st.selectbox('会議室名', rooms_name.keys())
        booked_num: int = st.number_input('予約人数',step=1, min_value=1)
        date = st.date_input('日付の入力', min_value=datetime.date.today())
        start_time = st.time_input('チェックイン時間: ', value=datetime.time(hour=9, minute=0))
        end_time = st.time_input('チェックアウト時間: ', value=datetime.time(hour=20, minute=0))
        
        submit_button = st.form_submit_button(label='予約登録')

    if submit_button:
        user_id: int = users_name[user_name]
        room_id: int = rooms_name[room_name][ 'room_id']
        capacity: int = rooms_name[room_name]['capacity']
        
        data = {
            'user_id': user_id,
            'room_id': room_id,
            'booked_num': booked_num,
            'start_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=start_time.hour,
                minute=start_time.minute
            ).isoformat(),
            'end_datetime': datetime.datetime(
                year=date.year,
                month=date.month,
                day=date.day,
                hour=end_time.hour,
                minute=end_time.minute
            ).isoformat()
        }
        
        # 定員より多い予約人数の場合
        if booked_num > capacity:
            st.error(f'{room_name}の定員は、{capacity}名です。{capacity}名以下の人数のみ受け付けております。')
        # 開始時刻 >= 終了時刻
        elif start_time >= end_time:
            st.error('開始時刻が終了時刻を超えています')
        elif start_time < datetime.time(hour=9, minute=0, second=0) or end_time > datetime.time(hour=20, minute=0, second=0):
            st.error('利用時間は9:00~20:00です。')
            
        else:
            #会議室予約
            url = 'http://127.0.0.1:8000/booking'
            res = requests.post(
                url,
                data=json.dumps(data)
            )
            if res.status_code == 200:
                st.success('予約完了')
            elif res.status_code == 404 and res.json()['detail'] == 'Already booked !':
                st.error('指定の時刻にはすでに予約が入っています。')
                
            st.json(res.json())

