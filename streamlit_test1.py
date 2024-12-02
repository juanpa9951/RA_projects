import streamlit as st
import pandas as pd

@st.cache_data(ttl=5)  # Cache the data for 10 seconds
def load_data(file_path):
    return pd.read_csv(file_path)

file_path=r"C:\Users\jplop\Documents\PythonScripts\file2.csv"
st.write("hello juanito")
st.text_input("hablaaame omeeee")
st.write("que paso puesss")
data = load_data(file_path)
st.write(data)


# import streamlit as st
# import pandas as pd
# import os
# import time
#
# file_path = r"C:\Users\jplop\Documents\PythonScripts\file2.csv"
#
# @st.cache_data
# def load_data(file_path):
#     return pd.read_csv(file_path)
#
# # Monitor file changes
# def get_last_modified_time(file_path):
#     return os.path.getmtime(file_path)
#
# # Track the last modification time
# if 'last_modified' not in st.session_state:
#     st.session_state['last_modified'] = get_last_modified_time(file_path)
#
# current_modified = get_last_modified_time(file_path)
#
# if current_modified != st.session_state['last_modified']:
#     st.session_state['last_modified'] = current_modified
#     st.experimental_rerun()
#
# # Load and display data
# data = load_data(file_path)
# st.dataframe(data)



# import streamlit as st
# import pandas as pd
# import os
#
# file_path=r"C:\Users\jplop\Documents\PythonScripts\file2.csv"
#
# @st.cache_data
# def load_data(file_path, last_modified):
#     # Use last_modified as a cache key to invalidate cache when the file updates
#     return pd.read_csv(file_path)
#
# # Get the last modified time of the file
# def get_last_modified_time(file_path):
#     return os.path.getmtime(file_path)
#
# # Check file modification time
# last_modified = get_last_modified_time(file_path)
#
# # Load and display the data
# data = load_data(file_path, last_modified)
# st.dataframe(data)






# import streamlit as st
# import pandas as pd
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import time
#
# class FileChangeHandler(FileSystemEventHandler):
#     def __init__(self, callback):
#         self.callback = callback
#
#     def on_modified(self, event):
#         if event.src_path.endswith("data.csv"):
#             self.callback()
#
# # Callback to reload the app
# def file_updated():
#     st.experimental_rerun()
#
# # Monitor file changes
# observer = Observer()
# event_handler = FileChangeHandler(callback=file_updated)
# observer.schedule(event_handler, ".", recursive=False)
# observer.start()
#
# # Load and display data
# file_path = r"C:\Users\jplop\Documents\PythonScripts\file2.csv"
# data = pd.read_csv(file_path)
# st.dataframe(data)
#
# # Stop the observer when the app closes
# st.on_event("shutdown", observer.stop)





#
# import streamlit as st
# import pandas as pd
#
# file_path = "file2.csv"
#
# # Button to reload data
# if st.button("Refresh Data"):
#     data = pd.read_csv(file_path)
#     st.write("Data refreshed!")
# else:
#     data = pd.read_csv(file_path)
#
# st.dataframe(data)




# import streamlit as st
# import pandas as pd
# import os
#
# file_path = "file2.csv"
#
# # Get the last modified time of the file
# def get_last_modified_time(file_path):
#     return os.path.getmtime(file_path)
#
# # Initialize session state for last modified time
# if 'last_modified' not in st.session_state:
#     st.session_state['last_modified'] = get_last_modified_time(file_path)
#
# # Check if the file has been updated
# current_modified = get_last_modified_time(file_path)
# if current_modified != st.session_state['last_modified']:
#     st.session_state['last_modified'] = current_modified
#     st.experimental_rerun()
#
# # Load the data
# data = pd.read_csv(file_path)
# st.dataframe(data)
