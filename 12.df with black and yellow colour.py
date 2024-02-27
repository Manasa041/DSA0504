import pandas as pd
import numpy as np

# Create DataFrame with random values
data = pd.DataFrame(np.random.randn(10, 4))

# Define custom function for rendering
def custom_render(val):
    return f'<td style="background-color: black; color: yellow">{val}</td>'

# Apply custom rendering to each cell (using map instead of applymap)
styled_df = data.style.map(custom_render)

# Print styled DataFrame
print(styled_df.to_string())
