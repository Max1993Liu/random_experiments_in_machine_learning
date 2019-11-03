import streamlit as st
import numpy as np
import time


progress_bar = st.progress(0)
status_text = st.empty()  # as a placeholder
chart = st.line_chart(np.random.randn(10, 2))

for i in range(100):
  progress_bar.progress(i)

  new_rows = np.random.randn(10, 2)

  status_text.text('The last random number is %s' % new_rows[-1, 1])

  chart.add_rows(new_rows)

  time.sleep(0.1)

status_text.text('done')
st.balloons()

