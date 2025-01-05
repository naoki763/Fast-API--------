import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Sample')
## 基本的な使い方
# # streamlitの実行時、ブラウザ上に下記の（）内を表示する
# st.write('Streamlit Sample')
# # マークダウン記法
# st.markdown("""
#             # 見出し１
#             ## 見出し２
#             ### 見出し３
#             - 箇条書き１
#             - 箇条書き２
#             - 箇条書き３
#             """)
# # コード記法
# st.code('a=123')
# st.code("""
#         import numpy as np
#         import pandas as pd
#         a=123
#         pd.DataFrame()
#         """)

# # DataFrame
# df = pd.DataFrame({
#     '１列目':[1,2,3,4],
#     '２列目':[-1,-2,-3,-4],
# })
# st.dataframe(df.style.highlight_max(axis=0))
# #dictionary(json)
# st.json({
#     'data':{
#         'name':'abc',
#         'age':123
#     }
# })

# # チャートエレメント（graph)
# # st.write(np.random.randn(20, 3))
# df = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c']
# )
# # ラインチャート
# st.line_chart(df)
# # エリアチャート
# st.area_chart(df)
# # ばーチャート
# st.bar_chart(df)

# input widgets
# button
# if st.button('Click'):
#     st.write('Thanks Clicked!')
# # checkbox
# if st.checkbox('Click'):
#     st.write('Thanks Clicked!')
# # multiselect
# options = st.multiselect(
#     "What are your favorite colors",
#     ["Green", "Yellow", "Red", "Blue"],#選択肢
#     ["Yellow", "Red"],#デフォルト値
# )
# st.write(f'選択肢：{options}')
# # slider
# number = st.slider('Pick a Num', 0, 100, 40)
# st.write(f'Number:{number}')

# layouts & Containers
# sidebar
number = st.sidebar.slider('Pick a Num', 0, 100, 40)
st.sidebar.write(f'Number:{number}')
# columns
left_col, right_col = st.columns(2)#列数
left_col.slider('Pick a Num in Left', 0, 100, 40)
right_col.slider('Right here')