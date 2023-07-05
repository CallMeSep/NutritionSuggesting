import pandas as pd
import numpy as np
import Person as ps
import streamlit as st
df = pd.read_excel("output.xlsx")
st.title('Hệ thống tư vấn dinh dưỡng cho người cao tuổi')
col1, col2, col3 = st.columns(3)
st.sidebar.write('Nhập thông số cơ thể')
height = st.sidebar.number_input('Nhập chiều cao', min_value=130,max_value=210)
weight = st.sidebar.number_input('Nhập cân nặng', min_value=40,max_value=200)
age = st.sidebar.slider('Bạn bao nhiêu tuổi?', 50, 100, 60)
gender = st.sidebar.selectbox(
    'Giới tính',
    ('Male', 'Female'))

disease = st.sidebar.selectbox(
    'Chọn bệnh nền bạn đang mắc',
    ('Gout', 'Tieu duong', 'Loang xuong','Tao bon','Mo mau','Thi giac'))

st.sidebar.write('Bạn bị bệnh: ', disease)

meal = st.sidebar.slider('Số bữa ăn trong ngày bạn muốn ăn: ', 1, 5, 3)

profile = ps.Profile(height, weight, age, gender, disease, meal,df)
with col1:
    if 130 <= profile.height <= 210:
        bmi = np.ceil(profile.bmi)
        st.header(f'BMI: {bmi}')
    else:
        st.error('Kiểm tra lại chiều cao')
with col2:

    if profile.bmi < 18.5:
        text = 'Bạn bị còi xương'
    elif 18.5 <= profile.bmi <= 24.9:
        text = 'BMI của bạn an toàn'
    elif 25 <= profile.bmi <= 29.9:
        text = 'Thừa cân'
    elif 30 <= profile.bmi < 39.9:
        text = 'Béo phì nhẹ'
    elif 40 <= profile.bmi < 50:
        text = 'Béo phì nặng'
    else:
        text = 'Kiểm tra lại cân nặng bạn nhập'
    if text != 'Kiểm tra lại cân nặng bạn nhập':
        st.header(f'{text}')
    else:
        st.error(f'{text}')

with col3:
    luongnuoc = weight * 30
    st.header(f'Bạn nên uống {luongnuoc/1000} lít nước 1 ngày')
loikhuyen = 'Lời khuyên: '
if disease ==  'Gout':
    loikhuyen += 'Uống nhiều nước, bổ sung chất xơ. Nên ăn đạm từ thịt trắng và cá'
elif disease == 'Tieu duong':
    loikhuyen += 'Bổ sung:  Chất xơ, chất béo thực vật'
elif disease == 'Loang xuong':
    loikhuyen += 'Bổ sung: chất béo, tăng cường canxi và Vitamin D'
elif disease == 'Tao bon':
    loikhuyen += 'Bổ sung: chất xơ, nước, hoa quả'
elif disease == 'Mo mau':
    loikhuyen += 'Bổ sung: Chất xơ. Nên ăn hải sản thay thế cho thịt. '
elif disease == 'Thi giac':
    loikhuyen += 'Bổ sung: Bổ sung vitamin A, vitamin B6'
chatdam, tinhbot, trangmieng,rau = profile.meal_cal()



st.write(loikhuyen)
col4, col5 = st.columns(2)
col6, col7 = st.columns(2)
with col4:
    st.write('Món thịt chính')
    st.dataframe(chatdam[['Thực Phẩm', 'Khẩu phần (gam)']])
with col5:
    st.write('Tinh bột chính')
    st.dataframe(tinhbot[['Thực Phẩm', 'Khẩu phần (gam)']])
with col6:
    st.write('Rau')
    st.dataframe(rau['Thực Phẩm'])
with col7:
    st.write('Món tráng miệng')
    st.dataframe(trangmieng[['Thực Phẩm', 'Khẩu phần (gam)','Vitamin A(IU )'	,'Vitamin B6(Mg )',	'Vitamin B12(Mcg)',	'Calcium(Mg )',	'Magnesium(Mg )'	,'Iron(Mg )']])

