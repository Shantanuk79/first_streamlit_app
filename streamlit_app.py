import streamlit
import pandas

streamlit.title('🥣 Perfect Omelette Recipe')
streamlit.header('Ingredients Required')
streamlit.text('🐔 2 Eggs')
streamlit.text('🍞 1 Tsp Butter')
streamlit.text('Salt to taste')
streamlit.text('🥗 Preferred spices and chillis')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

