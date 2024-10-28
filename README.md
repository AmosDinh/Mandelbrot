# Mandelbrot Set Visualizer

## How to Run

1. **Install Dependencies**:
   ```bash
   pipenv install --python=3.8
   pipenv shell 
   pip install eel
   pip install pandas 
   pip install pillow 
   ```

2. **Install GCC**:
   - For macOS users, you can use Homebrew:
     ```bash
     brew install gcc
     ```

3. **Navigate to the App Directory**:
   ```bash
   cd app/
   ```

4. **Update Commands in `handlefrontend.py`**:
   Change the two commands in `handlefrontend.py` to the following:
   ```python
   command1 = r'''cd "/Users/amos/Programming/MathPictures/app/" && g++-14 makeimg.cpp -o makeimg -I/opt/homebrew/opt/gmp/include -L/opt/homebrew/opt/gmp/lib -lgmp -lquadmath && "/Users/amos/Programming/MathPictures/app/"makeimg'''
   command2 = """python makeimg.py """ + str(max_iter)
   ```

5. **Run the Frontend**:
   ```bash
   python handlefrontend.py
   ```
   This will open the visualizer in your browser.

## Navigation

To navigate through the Mandelbrot set visualizer, use the arrow keys on your keyboard:
- **Left Arrow (←)**: Go back to the previous view.
- **Up Arrow (↑)**: Generate a high-resolution image of the current view.
- **Right Arrow (→)**: Move forward to the next view.
- **Down Arrow (↓)**: Currently not assigned to any action.

You can also click on the main image to create an indicator element that shows the coordinates of your click, and the visualizer will update based on the clicked position.

## Play Around with the Colors

In `app/makeimg.py`, you can experiment with different color schemes. For example:

in app/makeimg.py
e.g.: 

### Interesting ones 
r, g, b = (img/12)*255-250, (img/15)*255-250, (img/7)*255-250
#r, g, b = (img/12)*255*0, (img/15)*255*0, (img/7)*255

### flash/thunder
#r, g, b = (img/12)*20, (img/20)*100, (img/k)*255
#r, g, b = (img/12)*25, (img/20)*75, (img/k)*255


## Some pictures 

![Image 1](pictures/1639070595.461803.png)
![Image 2](pictures/1639070606.568746.png)
![Image 3](pictures/1639070607.741991.png)
![Image 4](pictures/1639073546.503952.png)
![Image 5](pictures/1639073918.610709.png)
![Image 6](pictures/1639074278.779958.png)
![Image 7](pictures/1639074296.970081.png)
![Image 8](pictures/1639074332.041203.png)
![Image 9](pictures/1639074357.501485.png)
![Image 10](pictures/1639074373.883678.png)
![Image 11](pictures/1639074397.286159.png)
![Image 12](pictures/1639074426.533002.png)
![Image 13](pictures/1639074499.935029.png)
![Image 14](pictures/1639074553.888472.png)
![Image 15](pictures/1639074592.500105.png)
![Image 16](pictures/1639074631.675422.png)
![Image 17](pictures/1639074676.57048.png)
![Image 18](pictures/1639074720.082191.png)
![Image 19](pictures/1639074760.703167.png)
![Image 20](pictures/1639074869.61541.png)
![Image 21](pictures/1639074911.571322.png)
![Image 22](pictures/1639074943.380764.png)
![Image 23](pictures/1639074981.440699.png)
![Image 24](pictures/1639075190.383948.png)
![Image 25](pictures/1639075339.229666.png)
![Image 26](pictures/1639075532.240123.png)
![Image 27](pictures/1639075617.899322.png)
![Image 28](pictures/1639075643.927251.png)
![Image 29](pictures/1639075673.313429.png)
![Image 30](pictures/1639075685.308091.png)
![Image 31](pictures/1639075696.670374.png)
![Image 32](pictures/1639075719.493465.png)
![Image 33](pictures/1639075773.220888.png)
![Image 34](pictures/1639075846.027033.png)
![Image 35](pictures/1639075876.464574.png)
![Image 36](pictures/1639076003.254242.png)
![Image 37](pictures/1639076042.476685.png)
![Image 38](pictures/1639076098.841196.png)
![Image 39](pictures/1639076126.709522.png)
![Image 40](pictures/1639076209.870843.png)
![Image 41](pictures/1639076251.936124.png)
![Image 42](pictures/1639076277.797244.png)
![Image 43](pictures/1639076312.235478.png)
![Image 44](pictures/1639076406.700503.png)
![Image 45](pictures/1639076438.176674.png)
![Image 46](pictures/1639076467.181352.png)
![Image 47](pictures/1639076527.928269.png)
![Image 48](pictures/1639076582.48365.png)
![Image 49](pictures/1639076610.244758.png)
![Image 50](pictures/1639076643.308115.png)
![Image 51](pictures/1639076734.350588.png)
![Image 52](pictures/1639076793.99751.png)
![Image 53](pictures/1639076834.79592.png)
![Image 54](pictures/1639076865.876942.png)
![Image 55](pictures/1639076877.797803.png)
![Image 56](pictures/1639076887.141983.png)
![Image 57](pictures/1639076905.43112.png)
![Image 58](pictures/1639076920.901638.png)
![Image 59](pictures/1639076954.054655.png)
![Image 60](pictures/1639076982.373591.png)
![Image 61](pictures/1639077039.859203.png)
![Image 62](pictures/1639077082.981824.png)